# coding=utf-8
from django import forms


class userRegister(forms.Form):
    phone_number = forms.CharField(min_length=11, max_length=11, required=True,
                                   error_messages={'required': '手机号不能为空'})
    register_username = forms.CharField(min_length=6, max_length=15, required=True,
                                        error_messages={'required': '用户名不能为空'})
    register_password = forms.CharField(min_length=8, max_length=20, required=True,
                                        error_messages={'required': '密码不能为空'})
    repeat_password = forms.CharField(min_length=8, max_length=20, required=True,
                                      error_messages={'required': '确认密码不能为空'})
    verification_code = forms.CharField(min_length=6, max_length=6, required=True,
                                        error_messages={'required': '验证码不能为空'})
