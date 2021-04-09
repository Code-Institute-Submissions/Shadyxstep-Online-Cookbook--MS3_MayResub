import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Directs visitor to landing page
@app.route("/")
def index():
    return render_template("index.html")


# Function to gather all sets of recipe data
# (C[R]UD) Read function
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/breakfast")
def breakfast():
    recipes = list(mongo.db.recipes.find())
    return render_template("breakfast.html", recipes=recipes)


@app.route("/lunch")
def lunch():
    recipes = list(mongo.db.recipes.find())
    return render_template("lunch.html", recipes=recipes)


@app.route("/dinner")
def dinner():
    recipes = list(mongo.db.recipes.find())
    return render_template("dinner.html", recipes=recipes)


@app.route("/beverages")
def beverages():
    recipes = list(mongo.db.recipes.find())
    return render_template("beverages.html", recipes=recipes)


# Search function using recipe category/name
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# Register Function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Login Function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username is already in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password entered
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesnt exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab sessions users username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# Logout function
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    flash("See you next time!")
    session.pop("user")
    return redirect(url_for("login"))


# CREATE Recipe Function ([C]RUD)
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "img_url": request.form.get("img_url"),
            "ingredients": request.form.get("ingredients"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "method_1": request.form.get("method_1"),
            "method_2": request.form.get("method_2"),
            "method_3": request.form.get("method_3"),
            "method_4": request.form.get("method_4"),
            "method_5": request.form.get("method_5"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added.")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("recipe_type", 1)
    return render_template("add_recipe.html", categories=categories)


# UPDATE Recipe function (CR[U]D)
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "img_url": request.form.get("img_url"),
            "ingredients": request.form.get("ingredients"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "method_1": request.form.get("method_1"),
            "method_2": request.form.get("method_2"),
            "method_3": request.form.get("method_3"),
            "method_4": request.form.get("method_4"),
            "method_5": request.form.get("method_5"),
            "description": request.form.get("description"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated.")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("recipe_type", 1)
    return render_template(
        "edit_recipe.html",
        recipe=recipe,
        categories=categories
        )


# DELETE Recipe function (CRU[D])
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


# Reads Categories & Recipes for Manage Recipes Page
@app.route("/get_categories")
def get_categories():
    recipes = list(mongo.db.recipes.find().sort("category_name", 1))
    return render_template("categories.html", recipes=recipes)


# Manage breakfast recipes
@app.route("/breakfast_categories")
def breakfast_categories():
    recipes = list(mongo.db.recipes.find().sort("category_name", 1))
    return render_template("breakfast_categories.html", recipes=recipes)


# Manage lunch recipes
@app.route("/lunch_categories")
def lunch_categories():
    recipes = list(mongo.db.recipes.find().sort("category_name", 1))
    return render_template("lunch_categories.html", recipes=recipes)


@app.route("/dinner_categories")
def dinner_categories():
    recipes = list(mongo.db.recipes.find().sort("category_name", 1))
    return render_template("dinner_categories.html", recipes=recipes)


@app.route("/beverage_categories")
def beverage_categories():
    recipes = list(mongo.db.recipes.find().sort("category_name", 1))
    return render_template("beverage_categories.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
