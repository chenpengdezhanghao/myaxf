$(function () {


     var topswiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        loop: true,
        autoplay:1000,
    });

    var mustbuySwiper = new Swiper('#mustbuySwiper', {

        slidesPerView: 3,
        spaceBetween: 5,
        loop: true,

    });
})