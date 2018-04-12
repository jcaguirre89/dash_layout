$(window).scroll(function () {
  console.log($(window).scrollTop())
  if ($(window).scrollTop() >=10) {
    $('.header').addClass('header-fixed');
  }
  if ($(window).scrollTop() < 10) {
    $('.header').removeClass('header-fixed');
  }
});