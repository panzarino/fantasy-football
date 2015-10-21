$("#searchform").submit(function(event) {

  /* stop form from submitting normally */
  event.preventDefault();

  /* get some values from elements on the page: */
  var $form = $( this );
  var url = $form.attr( "action" );
  //before send
  $("body").addClass("loading");

  /* Send the data using post */
  var posting = $.get(url , $( "#searchform" ).serialize() );

  /* Alerts the results */
  posting.done(function( data ) {
     //use data
     $("body").removeClass("loading");
     document.write(data)

  });
});