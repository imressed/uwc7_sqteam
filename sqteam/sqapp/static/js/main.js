 $(window).bind("load", function () {
    var footer = $("#footer");
    var pos = footer.position();
    var height = $(window).height();
    height = height - pos.top;
    height = height - footer.height();
    if (height > 0) {
        footer.css({
            'margin-top': height + 'px'
        });
    }
});

$(document).ready(function (){
    $("#start_search").click(function (){
        //$(this).animate(function(){
            $('html, body').animate({
                scrollTop: $("#results").offset().top
            }, 800);
        //});
    });
    $("#love").hover(function(){
        $(".logo-icon").css("color", "red");
        }, function(){
        $(".logo-icon").css("color", "black");
    });
    $("#proj2sub").click(function(e) {

        $("#proj2sub").removeAttr("href");
        $("#proj2sub").addClass("disabled");
        $("#proj2sub").html("Subscribed <i class='fi-check icon-font'></i>");
    });
});