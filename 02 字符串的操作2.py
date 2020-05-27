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
# r.setnx('age', 33)

# 设置字符串5s后过期
# r.set('name', 'niu', ex=5)
# r.setex('name', 10, 'niu')

# 设置字符串对象5ms后过期
# r.set('name', 'niu', px=5)
# r.psetex('name', 5, 'niu')

# 批量设置字符串对象
# r.mset({'name': 'niu', 'age': 33})

# 批量获取字符串对象，返回值是个列表
# print(r.mget(['name', 'age']))

# 计算字符串对象的字节长度
# print(r.strlen('name'))

# 数字字符串自增，未设置时默认自增步长为1
# r.incr('age', 3)
# r.incr('age2', 4)

# 数字字符串自减
# r.decr('age', 3)
# r.decr('age3')  # 默认自增步长为-1

# 删除字符串对象
# r.delete('age')

# 查看设置的内容
# print(r.get('age'))
# print(r.get('age3'))
# print(r.get('name'))
