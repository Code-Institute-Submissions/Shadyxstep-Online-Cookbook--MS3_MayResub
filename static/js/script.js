/*
    vanilla JavaScript for MaterializeCSS initialization
*/

document.addEventListener('DOMContentLoaded', function () {
    let sidenavs = document.querySelectorAll(".sidenav");
    let sidenavsInstance = M.Sidenav.init(sidenavs, { edge: "right" });
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, options);
});