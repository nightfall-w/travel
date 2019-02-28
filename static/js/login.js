//????
function page_login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    get_jwt_token(username, password);
}

function get_jwt_token(username, password) {
    if (!username) {
        $("#username").attr({'value': '', 'placeholder': "用户名不能为空"});
        return false
    }
    if (!password) {
        return false
    }
    $.ajax({
        type: 'POST',
        url: '/purview/api-token-auth/',
        data: $("#form_login").serialize(),
        dataType: 'json',
        success: function (data) {
            var token = data.token;
            localStorage.clear();
            sessionStorage.clear();
            localStorage.token = data.token;
            localStorage.username = data.username;
            localStorage.user_id = data.user_id;
            login(username, password, token)
        },
        error: function () {
            $('.form-login-error').show()
        }
    });
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
                $('#password').attr({'value': '', 'placeholder': data.message});
            }else {
                var next = GetQueryString("next");
                if (!next){
                    window.location.href='/index/'
                }else {
                    window.location.href=next;
                }
            }
        }
    })
}

$('input:text').each(function () {
   $(this).click(function () {
       $('.form-login-error').hide()
   })
});

function GetQueryString(name)
{
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);//search,查询？后面的参数，并匹配正则
     if(r!=null)return  unescape(r[2]); return null;
}

$('#password').keydown(function (event) {
    if (event.keyCode == 13){
        page_login()
    }
});