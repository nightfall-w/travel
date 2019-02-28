import hashlib
from utils.common import getConfig
from red_travel.settings import SECRET_KEY


def hash_str(str_data):
    """
    """
    if not isinstance(str_data, str):
        return None
    hash_obj = hashlib.md5()
    hash_obj.update(str_data.encode(encoding='utf-8'))
    str_hash = hash_obj.hexdigest()
    return str_hash


def hash_sign(current_time):
    accountSid = getConfig('MiaoDi', 'accountSid')
    auth_token = getConfig('MiaoDi', 'auth_token')
    sign = hash_str(accountSid + auth_token + current_time)
    return sign


def hash_verification_code(verification_code):
    hash_verification_code = hash_str(verification_code + SECRET_KEY)
    return hash_verification_code
