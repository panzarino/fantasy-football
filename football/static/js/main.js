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

// prints sidebar data
$(document).ready(function(){
    var numteams = getCookie("teams");
    if (numteams != ""){
        numteams = parseInt(numteams);
        for (var x=0; x<numteams; x++){
            var teamnum = x+1;
            var cookiename = "teamname"+teamnum;
            var teamname = getCookie(cookiename);
            var str = '<li>\n<a href="/teams/'+teamnum+'/" onclick = $("#menu-close").click(); >'+teamname+'</a>\n</li>';
            $("#sidebar-ul").append(str);
        }
    }
})