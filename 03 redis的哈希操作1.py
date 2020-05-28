#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/3/2020  11:05 AM 
# 文件名称   ：redis的哈希操作.PY
import redis


# 和redis建立连接
redis_pool = redis.ConnectionPool(host='192.168.137.131', port=6379, password='123456')
r = redis.Redis(connection_pool=redis_pool)

# 创建哈希兑下，哈希对象名称，键+值
# r.hset('infos', 'name', 'niu')

# 批量写入哈希对象的键+值
# r.hmset('infos1', {'name': 'niu', 'age': 30})

# 批量获取哈希对象中的某几个键值
# print(r.hmget('infos1', 'name', 'age'))

# 获取整个哈希对象的所有键的值
# print(r.hgetall('infos1'))

# 查看哈希对象中的某个键
# print(r.hget('infos1', 'name'))

# 计算哈希对象键值对数
# print(r.hlen('infos1'))

# 获取哈希对象中的所有键
# print(r.hkeys('infos1'))

# 获取哈希对象所有的值
# print(r.hvals('infos1'))

# 判断哈希对象中是否存在指定的键
# print(r.hexists('infos1', 'name'))
