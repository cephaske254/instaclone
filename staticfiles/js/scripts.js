$(document).ready(function () {
  setTimeout(() => {
    $('ul.errorlist').slideUp(500, function () {
      $(this.remove())
    });
  }, 2500);

  $('.popup').fadeOut(7000, function () {
    $(this).remove()
  })

})