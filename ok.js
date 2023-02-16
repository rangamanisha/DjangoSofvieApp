$('.btn').on('click', function() {
    var $this = $(this);
  $this.submit('loading');
    setTimeout(function() {
       $this.submit('reset');
   }, 8000);
});