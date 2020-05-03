#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/2/2020  11:02 AM 
# 文件名称   ：01 redis的连接方式.PY
import redis


# 基本连接
# r = redis.Redis(host='192.168.238.129', port=6379)
# r.set('age', 98)
# print(r.get('age'))

# redis连接池连接
redis_pool = redis.ConnectionPool(host='192.168.238.129', port=6379)
r = redis.Redis(connection_pool=redis_pool)
r.set('age', 30)
print(r.get('age'))
