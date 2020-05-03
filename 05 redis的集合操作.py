#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/3/2020  01:59 PM 
# 文件名称   ：05 redis的集合操作.PY
import redis


# 和redis建立连接
r_pool = redis.ConnectionPool(host='192.168.238.129', port=6379)
r = redis.Redis(connection_pool=r_pool)


# 新建集合
# r.sadd('set_scores', 78, 99, 25, 44, 33, 99)
# r.sadd('set_scores1', 44, 33, 99, 76, 55)

# 查看集合中的元素个数
# print(r.scard('set_scores'))
# print(r.scard('set_scores1'))

# 取多个集合的交集
# print(r.sinter('set_scores', 'set_scores1'))

# 取多个集合的并集
# print(r.sunion('set_scores', 'set_scores1'))

# 取集合的差集
# print(r.sdiff('set_scores', 'set_scores1'))

# 判断某个值是否在集合中
# print(r.sismember('set_scores', 99))
# print(r.sismember('set_scores1', 77))

# 随机删除集合中的一个值
# r.spop('set_scores')

# 随机从集合中取出几个值
# print(r.srandmember('set_scores', 3))

# 从集合中删除某个元素
# r.srem('set_scores', 99)

# 通过迭代器取集合中的值
print(r.sscan_iter('set_scores'))
for i in r.sscan_iter('set_scores'):
    print(i)

# 查看集合元素
print(r.smembers('set_scores'))
print(r.smembers('set_scores1'))
