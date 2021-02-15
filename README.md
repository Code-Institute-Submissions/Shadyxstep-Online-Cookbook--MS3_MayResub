# <a href="https://online-cookbook-ms3.herokuapp.com/">Snacc</a>

![responsive_screenshot](static/img/ms3responsive.PNG)

This [project](https://online-cookbook-ms3.herokuapp.com/) is my third milestone project in Full Stack Software Development course run by [Code Institute](https://codeinstitute.net/)

Want to store your favourite recipes all in one place?
This website allows you to share your favourite recipes! You can also see recipes that other user's have submitted.
Create, read, update & delete recipes once you register on site.
You can also browse recipes on the database by category - Breakfast, Lunch, Dinner & Beverages!
 
## UX
 
This website is made for people who love to cook & want an easy solution to storing their favourite recipes all in one place.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

"**_As a user, I would like to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: *view the site* from **any device** *(mobile, tablet, desktop)*.
- :white_check_mark: *view all recipes* as a **Guest**.
- :white_check_mark: *manage recipes* as a **User**
- :white_check_mark: *sort/order recipes* by **recipe name, breakfast type, lunch type, dinner type, beverage type**.
- :white_check_mark: *search recipes* by **recipe name, recipe type**.
- :white_check_mark: **limit** the number of *recipes* to display by category type, or see *all recipes*.
- :white_check_mark: *create* my **own profile**.
- :white_check_mark: *create* my **own recipes**.
- :white_check_mark: *add* my **own recipes**.
- :white_check_mark: *edit* my **own recipes**.
- :white_check_mark: *delete* my **own recipes**.
- :white_check_mark: be able to **log out**.


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features

**Register Account** 
- Anybody can register for free and create their own unique account. There is built-in authentication and authorization to check certain criteria is met before an account is validated. All passwords are hashed for security purposes!

**Log In to Account**
- If you are an existing user I have built an authorization feature that checks if the hashed passowrd & username match whats in the database.

**Log Out of Account**
- Existing users can choose to log out if they are finished using the website. 

**View all recipes**
- Both registered users & guests can view the existing recipes available on the site. 

**Search all recipes**
- Both registered users & guests can search existing recipes available on site via text input.

**Filter recipes**
- Both registered users & guests can filter existing recipes available on site by recipe type, e.g breakfast, lunch, dinner.

**Manage recipes**
- Registered users can access the manage recipes page which allows for updating current recipes in database or deleting recipes (provided the user has created the recipe they wish to delete). 

**Add recipes**
- [**C**RUD] Registered users can create / add new recipes to the website. Certain defensive programming functions have been implemented such as having the required attribute on multiple input fields whilst adding a recipe. No submission goes through unless input requirements are met.

![Create_crud](static/img/create-crud-functionality.PNG)

**View recipes**
-[C**R**UD] Both guest & registered users can view recipes on site. By clicking the expandable 'Click for more' element under a recipe, 
the user can view all associated data with that recipe ranging from recipe name, prep / cook time, ingredients to how to steps

![Read_crud](static/img/read-crud-functionality.PNG)

**Edit/Update recipes**
-[CR**U**D] Registered users can update recipes on the current database. Flash message lets user know if a recipe has been successfully updated.

![Update_crud](static/img/update-crud-functionality.PNG)

**Delete recipes**
-[CRU**D**] Only registered users can utilize the delete feature on the website. Defensive programming function has been implemented so that users can only delete recipes on the website that they have created using their profile. 

![Delete_crud](static/img/delete-crud-functionality.PNG)

**Admin**
-There is an admin profile which allows full access to CRUD functions on the website.
    -Admin can edit/delete any recipe from the database

### Features Left to Implement

- More features regarding users control over their profiles.
    -Enable to delete their account on site.
    -Enable user to change passwords if they wish.
    -Enable users to filter recipes to those only they have submitted.

-Allergens, Nutritional information
    -Added information to each recipe

-Extra sort methods
    -Add more filter criteria so users can filter by cuisine/nutrition/allergens.

-Extra pagination for all recipes page

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [GitHub](https://github.com/) 
    - Used as remote storage of my code online.

- [GitPod](https://gitpod.io/) 
    - Used as my primary IDE for coding

## Frontend Technologies

- [HTML](https://en.wikipedia.org/wiki/HTML) 
    - Used as the base for markup text.

- [CSS](https://en.wikipedia.org/wiki/CSS) 
    - Used as the base for cascading styles.

- [JQuery](https://en.wikipedia.org/wiki/JQuery) 
    - Used as the primary JavaScript functionality

- [MaterializeCSS](https://materializecss.com/)
    - Used as primary overall design framework.

- [FontAwesome](https://fontawesome.com/)
    - Used to enhance frontend styling using prebuilt icons.

- [AnimateCSS](https://animate.style/)
    - Used for animated CSS customization.

## Backend Technologies

-**Flask**

- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) 
    -Used as web framework

- [Jinja 2.10](http://jinja.pocoo.org/docs/2.10/) 
    - Used for templating with Flask.

- [Werkzeug 0.16](https://werkzeug.palletsprojects.com/en/0.16.x/) 
    - Used for password hashing, authentication, and authorization.

-**Heroku**

- [Heroku](https://www.heroku.com) 
    - Used for app hosting.

-**Python**

- [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.

- [MongoDB Atlas](https://www.mongodb.com/) - Used to store my database in the 'cloud'.

- [PyMongo 3.8.0](https://api.mongodb.com/python/current/) - Used as the Python API for MongoDB.

- [Python dotenv](https://github.com/theskumar/python-dotenv) - Used to get/set values in `.env` file.

## Testing

**Creating an Account**

I've created several of my own personal accounts through the development process in order to confirm authentication and validation worked as expected, along with the master *admin* account.
I have tested by also registering using a username that already exists in the database to ensure further authentication & validation.
Friends using the website have let me know they did not have any issues with registering a unique account
![create_account_testing](static/img/testing-create-account.PNG)

**Add | Edit | Delete a Recipe**

I have been adding, updating & deleting recipes using the website throughout the development of this project. 
There are no issues regarding any of these features. Users are required to fill out input fields when creating/updating recipes as a defensive programming practice to encourage quality submissions.
Flash messages let the user know if a recipe has been created, updated or deleted successfully.

**Pagination**

The pagination method on this website is used primarily to filter recipes by recipe category (breakfast, lunch, dinner)
I had a few issues implementing this feature but they were all simple issues regarding the syntax of urls called in the app.py file.

**Navigation**

I have included certain criteria that hides certain navigation links to guest users.
Guest users are unable to directly access the manage recipes tab which allows for ease of updating recipes on the database.
I have tested this by creating multiple accounts & visiting the website as a guess off multiple different devices to ensure hidden nav links are working as intended.

**Log in** 

I have tested the log in feature several times over the course of creating this project, including multiple times right before project submission.
There are no issues regarding logging in with existing credentials in the database, nor were there any issues reported by friends/family who have registered and used the site.
If the username or password is entered incorrectly, a flash message will show up saying 'Incorrect username or password' which is a defensive programming feature that 
discourages malicious users brute forcing a login by guessing usernames + passwords.

**Log Out** 

I have tested the log out feature several times over the course of creating this project.
I found that there are no issues regarding the logging out function nor have a received any reports of issues from friends/family who have used the site.

**Responsiveness**

I have tested responsiveness of this website for small/medium & large devices throughout development using online resource [Am I Responsive?](http://ami.responsivedesign.is/#)
The website seems to be fully responsive according to the website and across multiple devices tested ranging from small smartphones, ipads & large desktops.

## Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) - Unfortunately this validator is redundant regarding this project. The reason being that this HTML validator doesn't understand
Jinja templating syntax. There are a lot of errors present in my IDE also regarding doctype not being declared as Jinja is using a single html document to template the majority of the website
using "{% extends "base.html" %}{% block content %}{% endblock %}.
-Aside from the errors displaying, the code in this project is perfectly validated through localhost & the live application on Heroku.

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - I have 33 parsing errors when I run the code through this validator, however every single parsing error is due to the validator not
recognizing elements imported using [AnimateCSS](https://animate.style/) & [MaterializeCSS](https://materializecss.com/). Aside from this, the CSS code is validating fine.
![css_parse_errors](static/img/cssparsingerrors.PNG)

**JavaScript**
- [JShint](https://jshint.com/)
    -"There is only one function in this file.
        It takes no arguments.
        This function contains 6 statements.
        Cyclomatic complexity number for this function is 1.

        One undefined variable
        13	$
        14	$
        15	$
        16	$
        17	$
        18	$
        19	$

**Python**
- [PEP8 Online](http://pep8online.com/)
    - App.py files are completely PEP8 compliant!
    - env.py has one non pep8 compliant line, the URL for MONGODB_URI

## Deployment

### Local Deployment

Please note - in order to run this project locally on your own system, you will need the following installed:
- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- Any IDE such as [Microsoft Visual Studio Code](https://code.visualstudio.com). or [GitPod](https://code.gitpod.io).
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
- [MongoDB](https://www.mongodb.com) to develop your own database either locally or remotely on MongoDB Atlas.

Next, there's a series of steps to take in order to proceed with local deployment:

- Clone this GitHub repository by either clicking the green *Clone or download* button and downloading the project as a zip-file (remember to unzip it first), or by entering the following into the Git CLI terminal:
    - `git clone https://github.com/Shadyxstep/Online-Cookbook--MS3`.
- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
- Create a `.env` file with your credentials. An example can be found [here](https://github.com/Shadyxstep/Online-Cookbook--MS3/blob/master/.env_sample). Be sure to include your *MONGO_URI* and *SECRET_KEY* values.
- Create a `.flaskenv` file and add the following entries:
    - `FLASK_APP=run.py`
    - `FLASK_ENV=development`
- Install all requirements from the [requirements.txt](https://github.com/Shadyxstep/Online-Cookbook--MS3/blob/master/requirements.txt) file using this command:
    - `sudo -H pip3 -r requirements.txt`
- Sign up for a free account on [MongoDB](https://www.mongodb.com) and create a new Database called **cook_book**. The *Collections* in that database should be as follows:

**recipes**

_id: <ObjectId>
category_name: <string>
recipe_name: <string>
img_url: <string>
prep_time: <string>
cook_time: <string>
ingredients: <string>
method_1: <string>
method_1: <string>
method_1: <string>
method_1: <string>
method_1: <string>
description: <string>
created_by: <string>

**users**

_id: <ObjectId>
username: <string>
password: <string>

**categories**

_id: <ObjectId>
category_name: <string>

### Remote Deployment

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`
    - My file can be found [here](https://github.com/Shadyxstep/Online-Cookbook--MS3/blob/master/requirements.txt).
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python run.py > Procfile`
    - My file can be found [here](https://github.com/Shadyxstep/Online-Cookbook--MS3/blob/master/Procfile).
3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:
    - **IP** : `0.0.0.0`
    - **PORT** : `8080`
    - **MONGO_URI** : `<link to your Mongo DB>`
    - **SECRET_KEY** : `<your own secret key>`
    - **MY_ADDRESS** : `<your own email address>`
    - **SEND_TO** : `<recipient email address>`
    - **PASSWORD** : `<you own email password>`
5. Your app should be successfully deployed to Heroku at this point.

## Credits

### Content
- The recipe data used for this site were obtained from

[BBCGoodFood](https://www.bbcgoodfood.com/) Plenty of high quality meal recipes.

### Media
- The photos used in this site were obtained from 

-[Unsplash](https://unsplash.com/) Free high quality stock images

### Acknowledgements

- I received inspiration for this project from 

-[Tim Nelson](https://github.com/TravelTimN/)
    -Found his tutorials in data centric development module of the course to be very informative and easy to understand.
    -Tried to follow his formatting style for his README files in his numerous projects.