#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/8/2020  12:54 PM 
# 文件名称   ：02 字符串操作1.py.PY
import redis


# 和redis建立连接
r_pool = redis.ConnectionPool(host='192.168.238.129', port=6379)
r = redis.Redis(connection_pool=r_pool)

# 操作字符串
# r.set('name', 'hai')

# nx: 当键存在时不会执行设置，键不存在时执行设置
# r.set('name', 'hai1', nx=True)
# r.set('name1', 'hai1', nx=True)
# r.setnx('name', 'hai1')

# 设置字符串对象5s后过期
# r.set('name', 'bao', ex=5)
# r.setex('name', 10, 'hai')

# 设置字符串对象5ms后过期
# r.set('name', 'hai', px=5)
# r.psetex('name', 5, 'bao')

# 批量设置字符串对象
# r.mset({'name': 'niu', 'name1': 'bao'})

# 批量获取字符串对象, 返回的结果为列表
# print(r.mget(['name', 'name1']))

# 计算字符串对象的字节长度
# print(r.strlen('name'))

# 数字字符串自增
# print(r.incr('age'))
# print(r.incr('age', 3))

# 数字字符串自减
# r.decr('age')
# r.decr('age', 3)

# 获取对象
# print(r.get('age'))
# print(r.get('name1'))
