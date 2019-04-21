$(function () {
    "use strict";


    /**
     * introLoader - Preloader
     */
    $("#introLoader").introLoader({
        animation: {
            name: 'gifLoader',
            options: {
                ease: "easeInOutCirc",
                style: 'dark bubble',
                delayBefore: 500,
                delayAfter: 0,
                exitTime: 300
            }
        }
    });


    /**
     * Sticky Header
     */
    $(".container-wrapper").waypoint(function () {
        $(".navbar").toggleClass("navbar-sticky-function");
        $(".navbar").toggleClass("navbar-sticky");
        return false;
    }, {offset: "-20px"});


    /**
     * Main Menu Slide Down Effect
     */

    // Mouse-enter dropdown
    $('#navbar li').on("mouseenter", function () {
        $(this).find('ul').first().stop(true, true).delay(350).slideDown(500, 'easeInOutQuad');
    });

    // Mouse-leave dropdown
    $('#navbar li').on("mouseleave", function () {
        $(this).find('ul').first().stop(true, true).delay(100).slideUp(150, 'easeInOutQuad');
    });


    /**
     * Effect to Bootstrap Dropdown
     */
    $('.bt-dropdown-click').on('show.bs.dropdown', function (e) {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown(500, 'easeInOutQuad');
    });
    $('.bt-dropdown-click').on('hide.bs.dropdown', function (e) {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp(250, 'easeInOutQuad');
    });


    /**
     * Icon Change on Collapse
     */
    $('.collapse.in').prev('.panel-heading').addClass('active');
    $('.bootstarp-accordion, .bootstarp-toggle').on('show.bs.collapse', function (a) {
        $(a.target).prev('.panel-heading').addClass('active');
    })
        .on('hide.bs.collapse', function (a) {
            $(a.target).prev('.panel-heading').removeClass('active');
        });


    /**
     * Slicknav - a Mobile Menu
     */
    $('#responsive-menu').slicknav({
        duration: 300,
        easingOpen: 'easeInExpo',
        easingClose: 'easeOutExpo',
        closedSymbol: '<i class="fa fa-plus"></i>',
        openedSymbol: '<i class="fa fa-minus"></i>',
        prependTo: '#slicknav-mobile',
        allowParentLinks: true,
        label: ""
    });


    /**
     * Smooth scroll to anchor
     */
    $('a.anchor[href*=#]:not([href=#])').on("click", function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: (target.offset().top - 120) // 70px offset for navbar menu
                }, 1000);
                return false;
            }
        }
    });


    /**
     * Sign-in Modal
     */
    var $formLogin = $('#login-form');
    var $formLost = $('#lost-form');
    var $formRegister = $('#register-form');
    var $divForms = $('#modal-login-form-wrapper');
    var $Retrieve = $('#Retrieve-form');
    var $set_passwd = $('#set_passwd_form');
    var $modalAnimateTime = 300;

    $('#login_register_btn').on("click", function () {
        modalAnimate($formLogin, $formRegister)
    });
    $('#register_login_btn').on("click", function () {
        modalAnimate($formRegister, $formLogin);
    });
    $('#login_lost_btn').on("click", function () {
        modalAnimate($formLogin, $formLost);
    });
    $('#lost_login_btn').on("click", function () {
        modalAnimate($formLost, $formLogin);
    });
    $('#lost_register_btn').on("click", function () {
        modalAnimate($formLost, $formRegister);
    });

    $('#retrieve_login_btn').on("click", function () {
        modalAnimate($Retrieve, $formLogin);
    });
    $('#retrieve_register_btn').on("click", function () {
        modalAnimate($Retrieve, $formRegister);
    });
    $("#last_step_btn").on("click", function () {
        modalAnimate($Retrieve, $formLost)
    });
    $("#set_passwd_login_btn").on("click", function () {
        modalAnimate($set_passwd, $formLogin)
    });
    $("#set_passwd_register_btn").on("click", function () {
        modalAnimate($set_passwd, $formRegister)
    });
    function modalAnimate($oldForm, $newForm) {
        var $oldH = $oldForm.height();
        var $newH = $newForm.height();
        $divForms.css("height", $oldH);
        $oldForm.fadeToggle($modalAnimateTime, function () {
            $divForms.animate({height: $newH}, $modalAnimateTime, function () {
                $newForm.fadeToggle($modalAnimateTime);
            });
        });
    }


    /**
     * select2 - custom select
     */
    $(".select2-single").select2({allowClear: true});
    $(".select2-no-search").select2({dropdownCssClass: 'select2-no-search', allowClear: true});
    $(".select2-multi").select2({});


    /**
     * Show more-less button
     */
    $('.btn-more-less').on("click", function () {
        $(this).text(function (i, old) {
            return old == 'Show more' ? 'Show less' : 'Show more';
        });
    });


    /**
     *  Arrow for Menu has sub-menu
     */
    $(".navbar-arrow > ul > li").has("ul").children("a").append("<i class='arrow-indicator fa fa-angle-down'></i>");
    $(".navbar-arrow ul ul > li").has("ul").children("a").append("<i class='arrow-indicator fa fa-angle-right'></i>");


    /**
     *  Placeholder
     */
    $("input, textarea").placeholder();


    /**
     * Bootstrap tooltips
     */
    $('[data-toggle="tooltip"]').tooltip();


    /**
     * responsivegrid - layout grid
     */
    $('.grid').responsivegrid({
        gutter: '0',
        itemSelector: '.grid-item',
        'breakpoints': {
            'desktop': {
                'range': '1200-',
                'options': {
                    'column': 20,
                }
            },
            'tablet-landscape': {
                'range': '1000-1200',
                'options': {
                    'column': 20,
                }
            },
            'tablet-portrate': {
                'range': '767-1000',
                'options': {
                    'column': 20,
                }
            },
            'mobile-landscape': {
                'range': '-767',
                'options': {
                    'column': 10,
                }
            },
            'mobile-portrate': {
                'range': '-479',
                'options': {
                    'column': 10,
                }
            },
        }
    });


    /**
     * Payment Option
     */
    $("div.payment-option-form").hide();
    $("input[name$='payments']").on("click", function () {
        var test = $(this).val();
        $("div.payment-option-form").hide();
        $("#" + test).show();
    });


    /**
     * Raty - Rating Star
     */
    $.fn.raty.defaults.path = '/static/images/raty';

    // Default size star
    $('.star-rating').raty({
        round: {down: .2, full: .6, up: .8},
        half: true,
        space: false,
        score: function () {
            return $(this).attr('data-rating-score');
        }
    });

    // Read onlu default size star
    $('.star-rating-read-only').raty({
        readOnly: true,
        round: {down: .2, full: .6, up: .8},
        half: true,
        space: false,
        score: function () {
            return $(this).attr('data-rating-score');
        }
    });

    // Smaller size star
    $('.star-rating-12px').raty({
        path: "/static/images/raty",
        starHalf: 'star-half-sm.png',
        starOff: 'star-off-sm.png',
        starOn: 'star-on-sm.png',
        readOnly: true,
        round: {down: .2, full: .6, up: .8},
        half: true,
        space: false,
        score: function () {
            return $(this).attr('data-rating-score');
        }
    });

    // White color default size star
    $('.star-rating-white').raty({
        path: '/static/images/raty',
        starHalf: 'star-half-white.png',
        starOff: 'star-off-white.png',
        starOn: 'star-on-white.png',
        readOnly: true,
        round: {down: .2, full: .6, up: .8},
        half: true,
        space: false,
        score: function () {
            return $(this).attr('data-rating-score');
        }
    });


    /**
     * readmore - read more/less
     */
    $('.read-more-div').readmore({
        speed: 220,
        moreLink: '<a href="#" class="read-more-div-open">Read More</a>',
        lessLink: '<a href="#" class="read-more-div-close">Read less</a>',
        collapsedHeight: 45,
        heightMargin: 25
    });


    /**
     * ionRangeSlider - range slider
     */

    // Price Range Slider
    $("#price_range").ionRangeSlider({
        type: "double",
        grid: true,
        min: 0,
        max: 1000,
        from: 200,
        to: 800,
        prefix: "$"
    });

    // Star Range Slider
    $("#star_range").ionRangeSlider({
        type: "double",
        grid: false,
        from: 1,
        to: 2,
        values: [
            "<i class='fa fa-star'></i>",
            "<i class='fa fa-star'></i> <i class='fa fa-star'></i>",
            "<i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i>",
            "<i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i>",
            "<i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i>"
        ]
    });

    // 输入手机号input边框颜色变化
    $('#add_phone').focus(function () {
        $(this).css({'border': '1px solid #D65049', 'color': '#555555'});
    }).blur(function () {
        $(this).css('border', '1px solid #CCCCCC');
    });
    $('#verification_code').focus(function () {
        $(this).css({'border': '1px solid #D65049', 'color': '#555555'});
    }).blur(function () {
        $(this).css('border', '1px solid #CCCCCC');
    });

    $('#submit').click(function () {
        //检查手机号
        var phone_number = $('#add_phone').val();
        var REGEX_MOBILE_EXACT = "^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\\d{8}$";
        var re_ret = phone_number.match(REGEX_MOBILE_EXACT);
        if (re_ret === null) {
            $('#add_phone').attr({'value': '', 'placeholder': '请输入正确的手机号'});
            return false;
        }
        //检查验证码格式
        var code = $("#code").val();
        var REGEX_CODE_EXACT = /^\d{6}$/;
        var re_code_ret = code.match(REGEX_CODE_EXACT);
        if (re_code_ret === null) {
            $("#code").attr({'value': '', 'placeholder': '请输入6位数字验证码'});
            return false;
        }
        // 检查用户名
        var register_username = $("#register_username").val();
        var REGEX_username_EXACT = /^[a-zA-Z0-9_-]{6,16}$/;
        var re_username_ret = register_username.match(REGEX_username_EXACT);
        if (re_username_ret === null) {
            $('#register_username').attr({'value': '', 'placeholder': '请输入至少6位用户名'});
            return false;
        } else {
            var re_str = /[a-z]/i;
            if (!re_str.test(register_username)) {
                $('#register_username').attr({'value': '', 'placeholder': '用户名至少包含一位字母'});
                return false;
            }
        }
        // 检查密码格式以及一致性
        var first_password = $('#register_password').val();
        var REGEX_passwd_EXACT = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,16}$/;
        var re_passwd_ret = first_password.match(REGEX_passwd_EXACT);
        if (re_passwd_ret === null) {
            $('#register_password').attr({'value': '', 'placeholder': '请输入至少8位数字字母组成的密码'});
            return false;
        }
        if ($('#repeat_password').val() !== first_password) {
            $('#repeat_password').attr({'value': '', 'placeholder': '密码不一致，请确认！'});
            return false;
        }

        // 上传头像
        var update_result = Update_photo()
    });


    //上传头像功能
    function Update_photo() {
        var cas = $('#tailoringImg').cropper('getCroppedCanvas', {width: 50, height: 50});//获取被裁剪后的canvas
        var base64url = cas.toDataURL('image/png'); //转换为base64地址形式
        $.ajax({
            url: '/purview/update_photo/',
            type: 'POST',
            data: {
                'imgData': base64url
            },
            async: false,
            dataType: 'json',
            success: function (data) {
                console.log(data)
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(jqXHR);
                console.log(textStatus);
                console.log(errorThrown)
            }
        })
    }

    // 检查用户名是否存在
    $('#register_username').focus(function () {
        $(this).attr({'placeholder': "请输入用户名"});
    }).blur(function () {
        var register_username = $(this).val();
        $.ajax({
            type: 'GET',
            url: '/purview/register/',
            data: {'register_username': register_username},
            dataType: 'json',
            success: function (msg) {
                if (msg.return_code !== true) {
                    $('#register_username').attr({'value': '', 'placeholder': msg.return_value});
                }
            }
        });
    });

    // 重新发送注册验证码计时器
    var clock = '';
    var nums = 60;
    var button_obj = null;
    $('#addSendCode').click(function () {
        var phone_number = ($('#add_phone').val());
        if (phone_number === '') {
            return false;
        }
        var REGEX_MOBILE_EXACT = "^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\\d{8}$";
        var re_ret = phone_number.match(REGEX_MOBILE_EXACT);
        if (re_ret === null) {
            $('#add_phone').attr({'value': '', 'placeholder': '请输入正确的手机号'});
            return false;
        }
        $.ajax({
            type: 'GET',
            url: '/purview/register/',
            data: {'phone_number': phone_number},
            dataType: 'json',
            success: function (msg) {
                if (msg.return_code !== true) {
                    $('#add_phone').attr({'value': '', 'placeholder': msg.return_value});
                }
                else {
                    $("#addSendCode").attr("disabled", true).css('background-color', '#CCCCCC');
                    button_obj = $("#addSendCode")
                    clock = setInterval(doLoop, 1000); //一秒执行一次
                }
            }
        })
    });

    // 定时时间内的检查
    function doLoop() {
        nums--;
        if (nums > 0) {
            button_obj.attr('value', nums + '秒后可重新获取');
        } else {
            clearInterval(clock); //清除js定时器
            button_obj.attr({"disabled": false, 'value': '重新发送验证码'}).css('background-color', '#F56961');
            nums = 60; //重置时间
        }
    }

    function login(username, password, token) {
        $.ajax({
            type: 'POST',
            url: '/purview/login/',
            data: {'username': username, 'password': password},
            dataType: 'json',
            beforeSend: function (request) {
                request.setRequestHeader("Authorization", 'JWT ' + token);
            },
            success: function (data) {
                if (!data.success) {
                    $('#login_password').attr({'value': '', 'placeholder': data.message});
                } else {
                    $('.glyphicon').click();
                    location.reload(true)
                }
            }
        })
    }

    // 登录前获取JWT token
    function get_jwt_token(username, password, remember_me) {
        if (!username) {
            return "username_is_none"
        }
        if (!password) {
            return false
        }
        $.ajax({
            type: 'POST',
            url: '/purview/api-token-auth/',
            data: {'username': username, 'password': password},
            dataType: 'json',
            success: function (data) {
                var token = data.token;
                if (remember_me) {
                    // 记住我
                    localStorage.clear();
                    sessionStorage.clear();
                    localStorage.token = data.token;
                    localStorage.username = data.username;
                    localStorage.user_id = data.user_id;
                    localStorage.head_photo = data.head_photo;
                } else {
                    // 不记住
                    sessionStorage.clear();
                    localStorage.clear();
                    sessionStorage.token = data.token;
                    sessionStorage.username = data.username;
                    sessionStorage.user_id = data.user_id;
                    sessionStorage.head_photo = data.head_photo
                }
                login(username, password, token)
            },
            error: function (data) {
                $('#login_password').attr({'value': '', 'placeholder': "用户名密码不正确"});
            }
        });
    }

    // 点击按钮出发登录
    $("#login-submit").click(function () {
        var username = $("#login_username").val();
        var password = $("#login_password").val();
        var remember_me = $('#remember_me_checkbox').attr("checked");
        var result = get_jwt_token(username, password, remember_me);
        if (result === "username_is_none") {
            $('#login_username').attr({'value': '', 'placeholder': "用户名不能为空"});
        }
    });

    // 限制回车键作用
    $("#login_password").keydown(function (event) {
        if (event.keyCode === 13) {
            return false
        }
    });

    $("#login_username").keydown(function (event) {
        if (event.keyCode === 13) {
            return false
        }
    });

    // 注册请求的返回结果处理
    $("#register-form").ajaxForm(function (data) {
        if (data.return_code) {
            swal({
                    title: "注册成功！",
                    text: "去登录？",
                    type: "success",
                    showCancelButton: true
                },
                function (isTrue) {
                    if (isTrue) {
                        $('#register_login_btn').click();
                    } else {
                        $('#close').click();
                    }
                });
        }
        else {
            if (data.return_type === 'param_error' || data.return_type === 'img_type_error') {
                swal({
                    title: data.return_value,
                    type: "error"
                })
            } else if (data.return_type === 'verification_code_error') {
                $("#code").attr({'value': '', 'placeholder': data.return_value});
            } else if (data.return_type === 'username_exist') {
                $('#register_username').attr({'value': '', 'placeholder': data.return_value});
            }
        }
    });

    // 用户登出
    $('.user-logout').click(function () {
        var token = localStorage.token;
        if (!token) {
            token = sessionStorage.token;
        }
        $.ajax({
            type: 'post',
            url: '/purview/logout/',
            dataType: 'json',
            beforeSend: function (request) {
                request.setRequestHeader("Authorization", 'JWT ' + token);
            },
            success: function (data) {
                localStorage.clear();
                sessionStorage.clear();
                window.location.href = '/'
            }
        })
    });

    // 找回密码手机号验证
    $("#send_phone").click(function () {
        var phone_number = $('#lost_phone').val();
        if (phone_number === '') {
            return false;
        }
        var REGEX_MOBILE_EXACT = "^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\\d{8}$";
        var re_ret = phone_number.match(REGEX_MOBILE_EXACT);
        if (re_ret === null) {
            $("#check_phone_info").html("请输入正确的手机号");
            return false;
        }
        $.ajax({
            type: "post",
            url: "/purview/set_password/",
            dataType: 'json',
            data: {'phone': phone_number, 'request_type': "check_phone"},
            success: function (data) {
                if (data.isExist) {
                    modalAnimate($formLost, $Retrieve);
                    $('#set_passwd_SendCode').click()
                } else {
                    $("#check_phone_info").html("该手机号未被注册")
                }
            },
            error: function () {
                $("#check_phone_info").html("验证失败，请重试")
            }
        })
    });

    $("#lost_phone").focus(function () {
        $("#check_phone_info").html("验证码将会发送至你的注册手机")
    });
    $("#verification_code").focus(function () {
        $("#check_verification_code_info").html("验证码已发送至你的注册手机")
    });
    $("#password").focus(function () {
        $("#set_passwd_info").html("请设置新密码")
    });

    // 发送修改密码请求定时器
    $('#set_passwd_SendCode').click(function () {
        var phone_number = $('#lost_phone').val();
        $.ajax({
            type: 'GET',
            url: '/purview/set_password/',
            data: {'phone_number': phone_number},
            dataType: 'json',
            success: function (msg) {
                if (msg.return_code !== true) {
                    $('#lost_phone').attr({'value': '', 'placeholder': msg.return_value});
                }
                else {
                    $("#set_passwd_SendCode").attr("disabled", true).css('background-color', '#CCCCCC');
                    button_obj = $("#set_passwd_SendCode")
                    clock = setInterval(doLoop, 1000); //一秒执行一次
                }
            }
        });
    });

    // 提交验证码
    $("#send_verification_code").click(function () {
        var verification_code = $("#verification_code").val();
        var phone = $('#lost_phone').val();
        var REGEX_CODE_EXACT = /^\d{6}$/;
        var re_code_ret = verification_code.match(REGEX_CODE_EXACT);
        if (!re_code_ret) {
            $("#check_verification_code_info").text('请输入6位数字验证码')
        } else {
            $.ajax({
                type: 'post',
                url: '/purview/set_password/',
                data: {
                    'verification_code': verification_code,
                    'request_type': 'check_verification_code',
                    'phone': phone
                },
                dataType: 'json',
                success: function (msg) {
                    if (msg.return_code !== true) {
                        $('#check_verification_code_info').html("验证码不正确")
                    } else {
                        modalAnimate($Retrieve, $set_passwd)
                    }
                }
            })
        }
    });

    // 设置新密码
    $("#send_new_password").click(function () {
        var password = $("#password").val();
        var confirm_password = $("#confirm_password").val();
        if (password != confirm_password) {
            alert(password);
            alert(confirm_password);
            $("#set_passwd_info").html("密码不一致，请重新输入")
        } else {
            var REGEX_passwd_EXACT = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,16}$/;
            if (!password.match(REGEX_passwd_EXACT)) {
                $("#set_passwd_info").html("请输入至少8位数字字母组成的密码")
            } else {
                var phone = $('#lost_phone').val();
                $.ajax({
                    type: 'post',
                    url: '/purview/set_password/',
                    data: {'request_type': 'set_password', 'phone': phone, 'password': password},
                    dataType: 'json',
                    success: function (msg) {
                        if (!msg.return_code) {
                            $("#set_passwd_info").html("修改未成功，请重试")
                        } else {
                            swal({
                                    title: "密码修改成功！",
                                    text: "去登录？",
                                    type: "success",
                                    showCancelButton: true
                                },
                                function (isTrue) {
                                    if (isTrue) {
                                        $('#set_passwd_login_btn').click();
                                    } else {
                                        $('#close').click();
                                    }
                                })
                        }
                    }
                })
            }
        }
    });

    /**
     * slick
     */
    $('.gallery-slideshow').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        speed: 500,
        arrows: true,
        fade: true,
        asNavFor: '.gallery-nav'
    });
    $('.gallery-nav').slick({
        slidesToShow: 7,
        slidesToScroll: 1,
        speed: 500,
        asNavFor: '.gallery-slideshow',
        dots: false,
        centerMode: true,
        focusOnSelect: true,
        infinite: true,
        responsive: [
            {
                breakpoint: 1199,
                settings: {
                    slidesToShow: 7,
                }
            },
            {
                breakpoint: 991,
                settings: {
                    slidesToShow: 5,
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 5,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 3,
                }
            }
        ]
    });


    /**
     * Back To Top
     */
    $(window).scroll(function () {
        if ($(window).scrollTop() > 500) {
            $("#back-to-top").fadeIn(200);
        } else {
            $("#back-to-top").fadeOut(200);
        }
    });
    $('#back-to-top').on("click", function () {
        $('html, body').animate({scrollTop: 0}, '800');
        return false;
    });
    /**
     * Instagram
     */
//		function createPhotoElement(photo) {
//			var innerHtml = $('<img>')
//			.addClass('instagram-image')
//			.attr('src', photo.images.thumbnail.url);

//			innerHtml = $('<a>')
//			.attr('target', '_blank')
//			.attr('href', photo.link)
//			.append(innerHtml);

//			return $('<div>')
//			.addClass('instagram-placeholder')
//			.attr('id', photo.id)
//			.append(innerHtml);
//		}

//		function didLoadInstagram(event, response) {
//			var that = this;
//			$.each(response.data, function(i, photo) {
//			$(that).append(createPhotoElement(photo));
//			});
//		}

//		$(document).ready(function() {
//
//			$('#instagram').on('didLoadInstagram', didLoadInstagram);
//			$('#instagram').instagram({
//			count: 20,
//			userId: 302604202,
//			accessToken: '735306460.4814dd1.03c1d131c1df4bfea491b3d7006be5e0'
//			});

//		});

});