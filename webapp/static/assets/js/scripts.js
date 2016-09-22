/*
* Template: Uniquebiz
* Author: TrendyTheme
* Version: 1.0
* Design and Developed by: TrendyTheme
*/

jQuery(function ($) {

   //"use strict";


    /* ======= Preloader ======= */
    (function () {
        $('#status').fadeOut();
        $('#preloader').delay(200).fadeOut('slow');
    }());


    /* ======= Sticky Menu ======= */
    $('.navbar-custom').sticky({
        topSpacing: 0
    });


    /* === jQuery for page scrolling feature - requires jQuery Easing plugin === */
    $('a.page-scroll').on('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });

    
    /* === Collaps mobile menu when click on anchor === */
    $('.navbar-custom a.page-scroll').on('click', function(event) {
        $('.navbar-custom').find('.navbar-collapse').removeClass('in');
    });

    
    /* === Home Carousel === */
    $('#tt-carousel').carousel({
      interval: false,
      pause: "false"
    })


    /* === magnificPopup === */
    if ($('.tt-lightbox').length > 0) {

        $('.tt-lightbox').magnificPopup({
            type: 'image',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            fixedContentPos: false
            // other options
        });
    }


    if ($('.popup-youtube').length > 0) {
        $('.popup-youtube').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });
    }


    /* === Progress Bar === */
    $('.progress').on('inview', function(event, visible, visiblePartX, visiblePartY) {
        if (visible) {
            $.each($('div.progress-bar'),function(){
                $(this).css('width', $(this).attr('aria-valuenow')+'%');
            });
            $(this).off('inview');
        }
    });


    /* === Counter === */
    $('.counter-section').on('inview', function(event, visible, visiblePartX, visiblePartY) {
        if (visible) {
            $(this).find('.timer').each(function () {
                var $this = $(this);
                $({ Counter: 0 }).animate({ Counter: $this.text() }, {
                    duration: 2000,
                    easing: 'swing',
                    step: function () {
                        $this.text(Math.ceil(this.Counter));
                    }
                });
            });
            $(this).off('inview');
        }
    });


    /* ======= Latest Work Carousel ======= */
    $('.work-carousel').owlCarousel({
        loop:true,
        margin:30,
        autoplay:true,
        nav:false,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:4
            }
        }
    });


    /* === Mail Chimp subscription form settings === */

    if ($('.mailchimp').length > 0) {
        function mailchimpCallback(resp) {
             if (resp.result === 'success') {
                $('.subscription-success').html('<i class="fa fa-check"></i>' + resp.msg).fadeIn(1000);
                $('.subscription-error').fadeOut(500);
                
            } else if(resp.result === 'error') {
                $('.subscription-error').html('<i class="fa fa-times"></i>' + resp.msg).fadeIn(1000);
            }  
        }

$('.mailchimp').ajaxChimp({
            callback: mailchimpCallback,
            //replace bellow url with your own mailchimp form post url inside the url: "---".
            //to learn how to get your own URL, please check documentation file.
            url: "http://trendytheme.us9.list-manage.com/subscribe/post?u=85ba3666ffb519396fbe64dc5&amp;id=6a5ead803c" 
        }); 
        
    }


    /* ======= Contact Form ======= */
    $('#contactForm').on('submit',function(e){

        e.preventDefault();

        var $action = $(this).prop('action');
        var $data = $(this).serialize();
        var $this = $(this);

        $this.prevAll('.alert').remove();

        $.post( $action, $data, function( data ) {

            if( data.response=='error' ){

                $this.before( '<div class="alert alert-danger">'+data.message+'</div>' );
            }

            if( data.response=='success' ){

                $this.before( '<div class="alert alert-success">'+data.message+'</div>' );
                $this.find('input, textarea').val('');
            }

        }, "json");
    });


    /* ======= GOOGLE MAP ======= */
    $('#world-map-markers').vectorMap({
        map: 'world_mill_en',
        scaleColors: ['#C8EEFF', '#77a86d'],
        normalizeFunction: 'polynomial',
        hoverOpacity: 0.7,
        hoverColor: true,
        zoomOnScroll: false,
        markerStyle: {
          initial: {
            fill: '#77a86d',
            stroke: '#383f47'
          }
        },
        backgroundColor: '#eee',
        markers: [
          {latLng: [40.71, -74.00], name: 'New York, USA'},
          {latLng: [41.90, 12.49], name: 'Rome, Italy'},
          {latLng: [23.81, 90.41], name: 'Dhaka, Bangladesh'},
          {latLng: [19.07, 72.87], name: 'Mumbai, India'},
          {latLng: [51.50, -0.127], name: 'London, England'},
          {latLng: [-15.79, -47.88], name: 'Brasília, Brazil'},
          {latLng: [-33.86, 151.20], name: 'Sydney, Australia'},
        ]
    });


});