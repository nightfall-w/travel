import os
import random
import string
import redis
import configparser


def getConfig(section, key):
    root_path = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(root_path, 'red_travel', 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_path)
    try:
        value = config.get(section, key)
        return value
    except Exception:
        return ''


def create_verification():
    verification_code = ''
    for i in range(6):
        verification_code += random.choice(string.digits)
    return verification_code


redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=6, decode_responses=True)
