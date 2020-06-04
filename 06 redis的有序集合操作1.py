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
# print(redis_obj.zcount('scores', 1, 4))

# 自增有序集合中某个键对应的分数，在n1对应分数的基础上+3
# redis_obj.zincrby('scores', 3, 'n1')

# 按照索引取值
# print(redis_obj.zrange('scores', 0, 1))

# 查找值对应的分数
# print(redis_obj.zscore('scores', 'n1'))

# 查看值的排行，返回索引
# print(redis_obj.zrank('scores', 'n1'))

# 按照值删除有序集合中的元素
# redis_obj.zrem('scores', 'n1')

# 按照索引范围或者排名删除有序集合中的元素
# redis_obj.zremrangebyrank('scores', 0, 1)

# 并操作
# redis_obj.zadd('z1', {'n1': 3, 'n2': 4, 'n5': 6})
# redis_obj.zunionstore('z5', ('scores', 'z1'), aggregate=min())
# redis_obj.zadd('z1', {'n1': 1, 'n2': 2, 'n3': 3})
# redis_obj.zadd('z2', {'n1': 2, 'n4': 4, 'n5': 5})
# redis_obj.zunionstore('z3', ('z1', 'z2'), aggregate=min())

# 交集操作
# redis_obj.zinterstore('z4', ('z1', 'z2'))

# 查看有序集合的值
# print(redis_obj.zscan('scores'))
# print(redis_obj.zscan('z4'))
