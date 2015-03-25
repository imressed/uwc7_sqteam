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
    $("#proj1sub").click(function(e) {

        $("#proj1sub").removeAttr("href");
        $("#proj1sub").addClass("disabled");
        $("#proj1sub").html("Subscribed <i class='fi-check icon-font'></i>");
    });
    $("#login-button").click(function(event) {
                event.preventDefault();

                var login_form = $("#login-form");
                var csrftoken = $.cookie('csrftoken');
                $.ajax({
                    type: "POST",
                    url: login_form.attr("action"),
                    data: {
                        username: login_form.find("input[name=username]").val(),
                        password: login_form.find("input[name=password]").val(),
                        csrfmiddlewaretoken: csrftoken
                    }
                })
                .done(function(msg) {
                    console.log(msg)
                    if(msg.success == true) {
                        $("#modal-login").attr("aria-hidden","true");
                        $("body").find("input[name=subscribe]").val($("#login-form").find("input[name=username]").val());
                        $("body").find("input[name=subscribe]").hide();

                    } else {
                        $("#login-errors").empty().show();
                        $.each(msg.errors, function(field, error) {
                            if(field == "__all__") {
                                $("#login-errors").append(
                                        $("<p>" + error + "</p>")
                                );
                            } else {
                                $("#login-errors").append(
                                        $("<p>" + field + ": " + error + "</p>")
                                );
                            }
                        });

                    }
                });
            });

    $("#signup-button").click(function(event) {
                event.preventDefault();

                var signup_form = $("#signup-form");
                var csrftoken = $.cookie('csrftoken');
                $.ajax({
                    type: "POST",
                    url: signup_form.attr("action"),
                    data: {
                        email: signup_form.find("input[name=email]").val(),
                        password: signup_form.find("input[name=password]").val(),
                        csrfmiddlewaretoken: csrftoken
                    }
                })
                .done(function(msg) {
                    console.log(msg)
                    if(msg.success == true) {
                        window.location = msg.next;
                    } else {
                        $("#signup-errors").empty().show();
                        $.each(msg.errors, function(field, error) {
                            if(field == "__all__") {
                                $("#signup-errors").append(
                                        $("<p>" + error + "</p>")
                                );
                            } else {
                                $("#signup-errors").append(
                                        $("<p>" + field + ": " + error + "</p>")
                                );
                            }
                        });

                    }
                });
            });
});