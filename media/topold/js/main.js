$(document).ready(function () {
  //Stuck block
  var stuck = $("#stuck");
  $(window).scroll(function () {
    if ($(window).scrollTop() > 200) {
      //>700px from the top stuck show
      stuck.addClass("stuck--active");
      /*$(".stuck__block-img-gift").addClass("animate__bounceIn");*/
    } else {
      //<700px from the top stuck hide
      stuck.removeClass("stuck--active");
      /*$(".stuck__block-img-gift").removeClass("animate__bounceIn");*/
    }
  });
});  

