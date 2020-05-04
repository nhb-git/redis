#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/3/2020  06:57 PM 
# 文件名称   ：08 管道.PY
import redis


# 和redis建立连接
r_pool = redis.ConnectionPool(host='192.168.238.129', port=6379)
r = redis.Redis(connection_pool=r_pool)

# 创建管道对象
pipe = r.pipeline(transaction=True)

pipe.set('name1', 'niu')
pipe.set('sex', 'male')

pipe.execute()
