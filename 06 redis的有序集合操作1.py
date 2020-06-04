#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/4/2020  8:16 AM 
# 文件名称   ：06 redis的有序集合操作1.py
import redis


# 使用连接池建立redis对象
redis_pool = redis.ConnectionPool(host='192.168.137.130', port=6379, password='123456')
redis_obj = redis.Redis(connection_pool=redis_pool)

# 有序集合的操作
# 新建有序集合
# redis_obj.zadd('scores', {'n1': 1, 'n2': 2, 'n3': 3, 'n5': 5})

# 查看有序集合中的元素个数
# print(redis_obj.zcard('scores'))

# 获取在排序区间的值个数
print(redis_obj.zcount('scores', 1, 4))

# 查看有序集合的值
print(redis_obj.zscan('scores'))
