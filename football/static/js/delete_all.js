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

$("#delete").click(function(event) {
    // stop link from acting normally
    event.preventDefault();
    var numteams = getCookie("teams");
    if(confirm("Are you sure you want to delete all your teams?")){
        for (var x=numteams; x>0; x--){
            var team = "team"+x;
            var teamname = "teamname"+x;
            setCookie(team, "", -1);
            setCookie(teamname, "", -1);
        }
        setCookie("teams", '', -1);
        var url = "/team/new/";
        window.location.assign(url);
    }
})