/*
    JQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $('select').formSelect();
    $(".dropdown-trigger").dropdown();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 1,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});