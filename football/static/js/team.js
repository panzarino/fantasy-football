// function to set a cookie
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires + "; path=/";
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

$("#teamform").submit(function(event) {
    // stop form from submitting normally
    event.preventDefault();
    // get form data
    $("body").addClass("loading");
    var teamdata = $(this).serialize();
    var teamnum = $("#teamnum").val();
    var cookiename = "team"+teamnum;
    // set cookie
    setCookie(cookiename, teamdata, 360);
    var teamname = $("#teamname").val();
    var teamnamecookiename = "teamname"+teamnum
    setCookie(teamnamecookiename, teamname, 360);
    setCookie("teams", teamnum, 360);
    var url = "/team/"+teamnum;
    window.location.assign(url);
})