document.addEventListener("DOMContentLoaded", function() {

  if (document.querySelectorAll('[data-bss-baguettebox]').length > 0) {
    baguetteBox.run('[data-bss-baguettebox]', {
      animation: 'slideIn'
    });
  }

  var mySwiper = new Swiper('.swiper-container', {
    loop: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true
    },
    paginationClickable: true,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev'
    }
  });

});