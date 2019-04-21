# coding=utf-8
import re
import os
import uuid
import base64
from Logging import logger
from celery_tasks.SMS.tasks import request_to_chit_platform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from red_travel.settings import MEDIA_ROOT
from rest_framework.response import Response
from rest_framework.views import APIView
from user.form import userRegister
from user.models import Auth_profile
from utils.common import create_verification


# Create your views here.
class UserLogin(APIView):
    def dispatch(self, request, *args, **kwargs):
        """
        请求到来之后，都要执行dispatch方法，dispatch方法根据请求方式不同触发 get/post/put等方法

        注意：APIView中的dispatch方法有好多好多的功能
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        phone_pat = re.compile(
            r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
        if not all([username, password]):
            return Response({'success': False, 'message': '用户名密码不正确'})
        if re.match(phone_pat, username):
            try:
                username = Auth_profile.objects.get(
                    phone_number=username).user_obj.name
            except Auth_profile.DoesNotExist:
                return Response({'success': False, 'message': '用户名密码不正确'})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'success': False, 'message': '用户名密码不正确'})
        else:
            login(request, user)
            return Response(
                {'success': True, 'message': '登录成功', 'username': username})

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')


class UserLogout(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'success': True, 'message': '注销成功'})


class UserRegister(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # 获取手机号
        phone_number = request.GET.get('phone_number', None)
        register_username = request.GET.get('register_username', None)
        if register_username and not phone_number:
            if User.objects.filter(username=register_username):
                return Response(
                    {'return_code': False, 'return_value': '用户名已经存在'})
            else:
                return Response(
                    {'return_code': True, 'return_value': '用户名未使用'})
        if not register_username and not phone_number:
            return Response({'return_code': True, 'return_value': '用户名未使用'})
        if not phone_number:
            return Response({'return_code': False, 'return_value': '手机号不能为空'})
        try:
            user_phone = Auth_profile.objects.get(phone_number=phone_number)
        except BaseException:
            user_phone = None
        # 如果手机号已经存在 表示已经被注册 向用户返回错误信息
        if user_phone:
            return Response(
                {'return_code': False, 'return_value': '该手机号已经被注册'})
        else:
            verification_code = create_verification()  # 产生一个6位的随机验证码
            request.session[phone_number] = verification_code
            request.session.set_expiry(60 * 5)
            request_to_chit_platform.delay(
                phone_number, verification_code)  # 向第三方平台发送该手机号验证码的请求
        return Response({'return_code': True})

    def post(self, request, *args, **kwargs):
        '''获取必要的参数'''
        phone_number = request.POST.get('phone_number', None)
        username = request.POST.get('register_username', None)
        password = request.POST.get('register_password', None)
        input_verification_code = request.POST.get("verification_code", None)
        session_verification_code = request.session.get(phone_number, None)
        logger.debug("phone_number:{}".format(phone_number))
        logger.debug("username:{}".format(username))
        logger.debug("password:{}".format(password))
        logger.debug("verification_code:{}".format(input_verification_code))
        logger.debug("session_verification_code:{}".format(
            session_verification_code))

        # 检查表单数据
        f = userRegister(request.POST)
        if not f.is_valid():
            return Response({'return_code': False,
                             'return_type': 'param_error',
                             'return_value': f.errors})
        if input_verification_code != session_verification_code:
            pass
            return Response({'return_code': False,
                             'return_type': 'verification_code_error',
                             'return_value': '验证码不正确'})
        else:
            try:
                user = User.objects.create_user(username=username)
            except BaseException:
                return Response({'return_code': False,
                                 'return_type': 'username_exist',
                                 'return_value': '用户名已经存在'})
            user.set_password(password)
            user.save()
        head_photo = request.session.get('head_photo', None)
        if head_photo:
            Auth_profile.objects.create(
                phone_number=phone_number,
                user_obj=user,
                head_photo=head_photo)
            del request.session['head_photo']
        else:
            Auth_profile.objects.create(
                phone_number=phone_number, user_obj=user)
        del request.session[phone_number]
        return Response({'return_code': True, 'return_value': '注册成功！'})

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')


class Set_password(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        phone_number = request.GET.get('phone_number', None)
        verification_code = create_verification()  # 产生一个6位的随机验证码
        request.session[phone_number] = verification_code
        request.session.set_expiry(300)
        request_to_chit_platform.delay(
            phone_number, verification_code)  # 向第三方平台发送该手机号验证码的请求
        return Response({'return_code': True})

    def post(self, request, *args, **kwargs):
        request_type = request.POST.get('request_type')
        if request_type == "check_phone":
            phone = request.POST.get('phone', None)
            if phone:
                try:
                    Auth_profile.objects.get(phone_number=phone)
                except Auth_profile.DoesNotExist:
                    return Response({'isExist': False})
                return Response({'isExist': True})
            return Response({'isExist': False})
        elif request_type == "check_verification_code":
            verification_code = request.POST.get('verification_code')
            phone = request.POST.get('phone')
            cache_verification_code = request.session.get(phone, None)
            if verification_code == cache_verification_code:
                return Response({'return_code': True})
            return Response({'return_code': False})
        elif request_type == "set_password":
            phone = request.POST.get('phone', None)
            new_password = request.POST.get('password', None)
            if not all([new_password, phone]):
                return Response({'return_code': False})
            try:
                user = Auth_profile.objects.get(phone_number=phone).user_obj
            except Exception:
                return Response({'return_code': False})
            user.set_password(new_password)
            return Response({'return_code': True})


class Update_photo(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        photo = request.POST.get('imgData', None)
        if photo:
            data = base64.b64decode(photo.split(',')[1])
            photo_name = uuid.uuid1()
            path = os.path.join(MEDIA_ROOT,
                                'head_portrait/{}.jepg'.format(photo_name))
            with open(path, 'wb') as f:
                f.write(data)
            request.session['head_photo'] = '/media/head_portrait/{}.jepg'.format(
                photo_name)
        return Response({'return_code': True})

