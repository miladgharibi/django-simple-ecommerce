$(document).ready(function (){

    // change header intro text by time
    function changeHeaderTextAnimation(element){
        let strings = ['Hey Everyone', 'Welcome', 'To', 'Django Ecommerce ;)'];
        let index = 0
        setInterval(function (){
            if (index <= strings.length){
                $(element).text(strings[index]);
                index ++;
            } else {
                index = 0;
            }
        }, 1000);
    };

    changeHeaderTextAnimation('.header-text');


    $('.header-btn').on('click', function (){
        let ofs = $('.products-title');
        let ofst = Math.round(ofs.offset().top) - 60;
        $("html, body").animate({ scrollTop: `${ofst}px` });
    });


    $('.about-link').on('click', function (){
        let ofs = $('.about');
        let ofst = Math.round(ofs.offset().top) - 60;
        $("html, body").animate({ scrollTop: `${ofst}px` });
    });

});