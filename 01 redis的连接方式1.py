#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/8/2020  12:48 PM 
# 文件名称   ：01 redis的连接方式1.py.PY
import redis


# 基本连接
# r = redis.Redis(host='192.168.238.129', port=6379)
# print(r.get('age'))

# 连接池连接
r_pool = redis.ConnectionPool(host='192.168.238.129', port=6379)
r = redis.Redis(connection_pool=r_pool)
print(r.get('age'))
