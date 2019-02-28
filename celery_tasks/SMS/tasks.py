#coding=utf-8
import requests
import datetime
import time
from celery_tasks.main import app
from utils.hash import hash_sign
from utils.common import getConfig

@app.task(name="request_to_chit_platform")
def request_to_chit_platform(phone_number, verification_code):
    """

    :param phone_number: 目标手机号
    :param verification_code: 验证码
    :return:
        True:发送成功
        False:发送失败
    """
    api = getConfig('MiaoDi', 'api')
    accountSid = getConfig('MiaoDi', 'accountSid')
    templateid = getConfig('MiaoDi', 'templateid')
    timeout_s = getConfig('MiaoDi', 'timeout')
    param = '{},{}'.format(verification_code, timeout_s)
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    sign = hash_sign(timestamp)
    data = {
        'accountSid': accountSid, 'templateid': templateid, 'param': param,
        'to': phone_number, 'timestamp': timestamp, 'sig': sign
    }
    print(api)
    print(data)
    response = requests.post(url=api, data=data)
    ret_json = response.text
    print(ret_json)
    ret_dict = eval(ret_json)

    if ret_dict.get('respCode') != '00000':
        return False
    else:
        return True