#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/3/2020  02:42 PM 
# 文件名称   ：06 redis的有序集合操作.PY
import redis


# 和redis建立连接
r_pool = redis.ConnectionPool(host='192.168.238.129', port=6379)
r = redis.Redis(connection_pool=r_pool)

# 有序集合操作
# 新建有序集合
# r.zadd('z', {'n1': 1, 'n2': 2, 'n3': 5, 'n4': 4})

# 查看有序集合中的元素个数
# print(r.zcard('z'))

# 获取在排序区间之间的值个数
# print(r.zcount('z', 1, 4))
# print(r.zcount('z', 1, 2))

# 自增有序集合中某个值对应的分数
# print(r.zincrby('z', 3, 'n1'))

# 按照索引范围取值
# print(r.zrange('z', 0, 1))

# 查找值对应的分数
# print(r.zscore('z', 'n1'))

# 查看值的排行
# print(r.zrank('z', 'n3'))

# 按照值删除集合中的某个元素
# r.zrem('z', 'n3')

# 按排名删除集合中的元素
# r.zremrangebyrank('z', 0, 1)

# 并操作
# r.zadd('z1', {'n1': 1, 'n2': 2, 'n3': 3})
# r.zadd('z2', {'n1': 2, 'n4': 4, 'n5': 5})
# r.zunionstore('z3', ('z1', 'z2'), aggregate=min())

# 交集操作
r.zinterstore('z4', ('z1', 'z2'))

# 查看有序集合的值
print(r.zscan('z4'))
