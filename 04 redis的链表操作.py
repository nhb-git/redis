#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/3/2020  11:54 AM 
# 文件名称   ：redis的链表操作.PY
import redis

# 和redis建立连接并生成redis对象
r_pool = redis.ConnectionPool(host='192.168.238.129', port=6379)
r = redis.Redis(connection_pool=r_pool)

# 链表操作
# 新建一个链表，参数顺序和redis链表对象顺序不一定相同
# r.lpush('scores', 78, 99, 43, 88)

# 新建一个链表，参数顺序和redis链表对象顺序相同
# r.rpush('order_scores', 66, 55, 44, 33)

# 添加元素到已有链表的左侧
# r.lpushx('order_scores', 100)

# 添加元素到已有链表的右侧，链表不存在则该命令不起作用
# r.rpushx('order_scores', 22)

# 将元素插入到已有链表的指定位置
# r.linsert('order_scores', 'BEFORE', 55, 56)

# 通过索引设置值
# r.lset('order_scores', 0, 99)

# 通过值删除元素
# r.lrem('order_scores', count=0, value=99)

# 删除链表最左侧的元素
# r.lpop('order_scores')

# 删除链表最右侧的元素
# r.rpop('order_scores')

# 通过索引获取元素
# print(r.lindex('order_scores', 3))

# 截断部分值
# r.ltrim('order_scores', 1, 3)

# 查看链表中的值
# print(r.lrange('scores', 0, -1))
print(r.lrange('order_scores', 0, -1))

# 查看链表中元素的个数
# print(r.llen('order_scores'))
