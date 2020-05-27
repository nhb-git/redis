#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/27/2020  1:25 PM
# 文件名称   ：02 字符串的操作2.py.py
import redis


# 连接redis
redis_pool = redis.ConnectionPool(host='192.168.137.131', port=6379, password='123456')
r = redis.Redis(connection_pool=redis_pool)

# 字符串操作
# 当键不存在时才会执行的操作
# r.set('age', 31)
# r.set('age', 32, nx=True)
r.setnx('age', 33)
print(r.get('age'))
