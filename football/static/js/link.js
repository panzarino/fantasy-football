$(".loading-link").click(function(event){
    $("body").addClass("loading");
    event.preventDefault();
    var url = $(this).attr("href");
    window.location.assign(url);
})