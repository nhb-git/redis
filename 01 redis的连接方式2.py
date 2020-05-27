#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/27/2020  1:15 PM 
# 文件名称   ：01 redis的连接方式2.py
import redis


# 基本连接，连接无法复用，每次请求都需要建立新连接
# r = redis.Redis(host='192.168.137.131', port=6379, password='123456')
# r.set('age', 99)
# print(r.get('age'))

# 连接池
redis_pool = redis.ConnectionPool(host='192.168.137.131', port=6379, password='123456')
r = redis.Redis(connection_pool=redis_pool)
r.set('age', 30)
print(r.get('age'))
