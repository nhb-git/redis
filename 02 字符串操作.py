#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/2/2020  11:21 AM 
# 文件名称   ：02 字符串操作.PY
import redis


# 建立redis连接池
redis_pool = redis.ConnectionPool(host='192.168.238.129', port=6379)
r = redis.Redis(connection_pool=redis_pool)

# nx: 当键name不存在时才会执行设置
# r.set('name', 'niu2', nx=True)

# 键name不存在时执行设置操作
# r.setnx('name', 'hai')

# 设置5s后过期
# r.setex('name', 5, 'bao')

# 设置5ms后过期
# r.psetex('name', 5, 'niu')

# 批量设置
# r.mset({'k1': 'k1', 'k2': 'k2'})
# print(r.mget(['k1', 'k2']))

# 获取字符串部分的值
# r.set('k1', 'niu')
# print(r.getrange('k1', 0, 1))

# 设置字符串部分的值
# r.setrange('k1', 2, 'ha')

# 返回字符串的字节长度
# print(r.get('k1'))
# print(r.strlen('k1'))

# 数字字符串自增
# r.incr('age', 2)

# 数字字符串自减
# r.decr('age')
# print(r.get('age'))

# 字符串追加
# r.append('k9', 'append')
# print(r.get('k9'))

