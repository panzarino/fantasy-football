  // function to show the player points
  function getPlayerPoints(url, output){
    var posting = $.get(url);
      posting.done(function(data) {
        $(output).html(data);
      });
  }

  // function to call the player points function
  $(document).ready(function(){
    // loading icon while data loads
    $(".points").html("<img src='/static/img/loading.gif'>");
    var scoring = $("#scoring").text();
    var qbnum = $(".qb-points").length;
    for (var x=1; x<=qbnum; x++){
      var getname = "#qbname"+x;
      var getpoints = "#qbpoints"+x;
      var position = "QB";
      var name = $(getname).text();
      var url = "/points/?name="+name+"&scoring="+scoring+"&position="+position;
      getPlayerPoints(url, getpoints);
    }
    var qbnum = $(".rb-points").length;
    for (var x=1; x<=qbnum; x++){
      var getname = "#rbname"+x;
      var getpoints = "#rbpoints"+x;
      var position = "RB";
      var name = $(getname).text();
      var url = "/points/?name="+name+"&scoring="+scoring+"&position="+position;
      getPlayerPoints(url, getpoints);
    }
    var qbnum = $(".wr-points").length;
    for (var x=1; x<=qbnum; x++){
      var getname = "#wrname"+x;
      var getpoints = "#wrpoints"+x;
      var position = "WR";
      var name = $(getname).text();
      var url = "/points/?name="+name+"&scoring="+scoring+"&position="+position;
      getPlayerPoints(url, getpoints);
    }
    var qbnum = $(".te-points").length;
    for (var x=1; x<=qbnum; x++){
      var getname = "#tename"+x;
      var getpoints = "#tepoints"+x;
      var position = "TE";
      var name = $(getname).text();
      var url = "/points/?name="+name+"&scoring="+scoring+"&position="+position;
      getPlayerPoints(url, getpoints);
    }
 })