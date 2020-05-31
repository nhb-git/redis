#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/31/2020  11:24 PM 
# 文件名称   ：04 redis的链表操作1.py
import redis


# 建立redis对象
connection_pool_obj = redis.ConnectionPool(host='192.168.137.128', port=6379, password='123456')
redis_obj = redis.Redis(connection_pool=connection_pool_obj)

# 新建一个链表对象，添加的顺序不一定和链表对象中的顺序一致
# redis_obj.lpush('list', 65, 75, 85, 95)

# 新建一个链表对象，添加的值顺序和链表对象中存放的顺序一致
# redis_obj.rpush('scores', 65, 75, 85, 95)

# 添加元素到已有链表的左侧，链表不存在时操作不起作用
# redis_obj.lpushx('scores', 33)

# 添加元素到已有链表的右侧，链表不存在时操作不起作用
# redis_obj.rpushx('scores', 105)

# 将元素插入到已有链表的指定位置
# redis_obj.linsert('scores', 'BEFORE', 33, 23)

# 按照索引设置元素
# redis_obj.lset('scores', 1, 25)

# 通过元素值删除元素
# redis_obj.lrem('scores', count=0, value=23)

# 删除链表最左侧的元素
# redis_obj.lpop('scores')

# 删除链表最右侧的元素
# redis_obj.rpop('scores')

# 通过索引获取元素值
# print(redis_obj.lindex('scores', 3))

# 截断链表中的部分值， 链表只保留索引从1到3的元素
# redis_obj.ltrim('scores', 1, 3)

# 查看链表中元素的个数
# print(redis_obj.llen('scores'))

# 查看链表对象的值
# print(redis_obj.lrange('list', 0, -1))
# print(redis_obj.lrange('scores', 0, -1))
