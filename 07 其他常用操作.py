#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/3/2020  06:24 PM 
# 文件名称   ：07 其他常用操作.PY
import redis


# 和redis建立连接
r_pool = redis.ConnectionPool(host='192.168.238.129', port=6379)
r = redis.Redis(connection_pool=r_pool)

# 其他操作
# 查看redis里面存着的key名称
# print(r.keys())

# 过滤以k开头的key名称
# print(r.keys(pattern='z*'))

# 删除某个key
# r.delete('name')

# 判断某一个key是否存在
# print(r.exists('name'))

# 给某个key设置过期时间
# r.expire('ke', 5)
# print(r.keys())

# 随机取得一个key
# print(r.randomkey())

# 查看key对应值的类型
# print(r.type('z1'))

# 取出所有键
# print(r.scan())
print(r.scan_iter(match='z*'))
