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
    // verification for browsers like safari
    var ref = $(this).find("[required]");
    var good = true;
    $(ref).each(function(){
        if ($(this).val() == '')
        {
            alert("Not all fields are filled out!");
            good = false;
            return false;
        }
    });
    if (good == true){
        // get form data
        $("body").addClass("loading");
        var teamdata = $(this).serialize();
        var teamnum = $("#teamnum").val();
        // set cookies
        for (var x=(teamnum-1); x>0; x--){
            // resets the expiration date so all teams expire at same time
            var team = "team"+x;
            var resetteamdata = getCookie(team);
            if (resetteamdata!=""){
                setCookie(team, resetteamdata, 180);
            }
            var teamname = "teamname"+x;
            var teamnamedata = getCookie(teamname);
            if (teamnamedata!=""){
                setCookie(teamname, teamnamedata, 180);
            }
        }
        var cookiename = "team"+teamnum;
        setCookie(cookiename, teamdata, 180);
        var teamname = $("#teamname").val().replace(/ /g,"_");;
        var teamnamecookiename = "teamname"+teamnum;
        setCookie(teamnamecookiename, teamname, 180);
        setCookie("teams", teamnum, 180);
        var url = "/team/"+teamnum;
        window.location.assign(url);
    }
})

// sets scoring when page loads
$(document).ready(function(){
    var scoring = $("#scoring").text();
    if (scoring != ""){
        var scoring_id = "#"+scoring;
        $(scoring_id).attr("checked", true);
    }
    else{
        $("#standard").attr("checked", true);
    }
})