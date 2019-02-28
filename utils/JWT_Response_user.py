# -*- coding:utf-8 -*-
from django.contrib.auth.backends import ModelBackend
from user.models import User, auth_profile
import re


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }


def get_user_by_account(account):
    """
    根据帐号获取user对象
    :param account: 账号，可以是用户名，也可以是手机号
    :return: User对象 或者 None
    """
    phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
    try:
        if re.match(phone_pat, account):
            # 帐号为手机号
            user = auth_profile.objects.get(phone_number=account).user_obj
        else:
            # 帐号为用户名
            user = User.objects.get(username=account)
    except (User.DoesNotExist, auth_profile.DoesNotExist):
        return None
    else:
        return user


class UsernameMobileAuthBackend(ModelBackend):
    """
    自定义用户名或手机号认证
    """

    def authenticate(self, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user is not None and user.check_password(password):
            return user
        else:
            return None
