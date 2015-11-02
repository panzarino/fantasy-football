// function to set a cookie
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

// function to read cookie data
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}

// sets default scoring when page loads
$(document).ready(function(){
    var scoring = getCookie("scoring");
    if (scoring != ""){
        var scoring_id = "#"+scoring;
        $(scoring_id).attr("checked", true);
    }
    else{
        $("#standard").attr("checked", true);
    }
})

// on form submit
$("#searchform").submit(function(event) {

    // stop form from submitting normally
    event.preventDefault();
    // display loading icon
    $("body").addClass("loading");
    // get form data
    var $form = $(this);
    var url = $form.attr("action");
    
    // set scoring type cookie
    var scoring = $('input:radio[name=scoring]:checked').val();
    // sets cookie for 1 year
    setCookie("scoring", scoring, 180);
    
    // get form data
    var searchdata = $("#searchform").serialize();
    // Send the data using get
    var posting = $.get(url , searchdata);
        /* Alerts the results */
    posting.done(function( data ) {
        // replace page content
        $("body").removeClass("loading");
        document.write(data)
        // change url
        var url = "/search/results/?"+searchdata;
        window.history.pushState({},"Results", url);
    });
});