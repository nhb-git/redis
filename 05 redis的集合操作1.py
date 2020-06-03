#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/3/2020  12:58 PM 
# 文件名称   ：05 redis的集合操作1.py
import redis


# redis连接池
redis_pool = redis.ConnectionPool(host='192.168.137.131', port=6379, password='123456')
redis_obj = redis.Redis(connection_pool=redis_pool)

# redis对象的集合操作
# redis_obj.sadd('scores', 45, 55, 65, 75)
redis_obj.sadd('scores1', 85, 97, 45)

# 查看集合中元素的个数
# print(redis_obj.scard('scores'))

# 取多个集合的交集
# print(redis_obj.sinter('scores', 'scores1'))

# 取多个集合的并集
# print(redis_obj.sunion('scores', 'scores1'))

# 取两个集合的差集
# print(redis_obj.sdiff('scores', 'scores1'))

# 判断某个值是否在集合中
# print(redis_obj.sismember('scores', 45))

# 随机删除集合中的一个值
# redis_obj.spop('scores')

# 随机从集合中取出几个值
# print(redis_obj.srandmember('scores', 2))

# 从集合中删除某个值
# redis_obj.srem('scores', 75)

# 迭代器获取集合中的值
for item in redis_obj.sscan_iter('scores'):
    print(item)

# 查看集合中的对象
print(redis_obj.smembers('scores'))
