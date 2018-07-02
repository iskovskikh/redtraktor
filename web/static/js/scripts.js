$(document).ready(function(e) {
    var $header = $('header');
	var $headerOffsetTop = $header.data('offset-top');
	var $headerStuck = $header.data('stuck');


	/*Small Header slide down on scroll
	*******************************************/
	if($(window).width() >= 500){
		$(window).on('scroll', function(){
				if($(window).scrollTop() > $headerOffsetTop ){
					$header.addClass('small-header');
				} else {
					$header.removeClass('small-header');
				}
				if($(window).scrollTop() > $headerStuck ){
					$header.addClass('stuck');
				} else {
					$header.removeClass('stuck');
				}
		});
	}

});