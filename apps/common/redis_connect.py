# -*- coding: UTF-8 -*-
import redis
from apps.settings import REDIS_IP, REDIS_PORT, REDIS_PASSWD


class RedisConnect(object):
    def __init__(self):
        # pool = redis.ConnectionPool(host=str(redis_ip), port=int(redis_port), password=str(redis_passwd), decode_responses=True)
        pool = redis.ConnectionPool(host=str(REDIS_IP), port=int(REDIS_PORT), password=str(REDIS_PASSWD))
        self.redis = redis.Redis(connection_pool=pool)

    def get(self, key):
        try:
            res = self.redis.get(key)
            return res
        except Exception as e:
            return False

    def set(self, key, value, ttl=None):
        try:
            self.redis.set(key, value, ex=ttl)
        except Exception as e:
            print(str(e))
            return False
        return True
