#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/3/2020  11:05 AM 
# 文件名称   ：redis的哈希操作.PY
import redis


# 和redis建立连接
r_pool = redis.ConnectionPool(host='192.168.238.129', port=6379)
r = redis.Redis(connection_pool=r_pool)

# 写入哈希对象
# r.hset('infos', 'name', 'niu')

# 查看哈希对象某一个键对应的值
# print(r.hget('infos', 'name'))

# 批量写入哈希对象
# r.hmset('infos1', {'age': 30, 'name': 'niu', 'sex': 'male'})

# 取出整个哈希对象
# print(r.hgetall('infos1'))

# 取出哈希对象的某几个键
# print(r.hmget('infos1', 'age', 'name'))

# 计算哈希对象有几个键值对
# print((r.hlen('infos1')))

# 获取哈希对象所有的键
# print(r.hkeys('infos1'))

# 获取哈希对象所有的值
# print(r.hvals('infos1'))

# 判断哈希对象中是否存在某个指定的键
# print(r.hexists('infos1', 'age'))

# 删除哈希对象中的某一个键值对
# r.hdel('infos1', 'age')
# print(r.hgetall('infos1'))

# 哈希对象的某一个键对应的值自增
# r.hincrby('infos1', 'age', 2)
# print(r.hgetall('infos1'))

# 生成器获取大哈希对象
# for item in r.hscan_iter('infos1', match='a*'):
#     print(item)
