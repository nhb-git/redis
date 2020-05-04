#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/3/2020  07:14 PM 
# 文件名称   ：09 redis 消息订阅消费者.PY
import redis


r = redis.Redis(host='192.168.238.129')
pub = r.pubsub()

pub.subscribe('fm104.5')
pub.parse_response()

while 1:
    msg = pub.parse_response()
    print(msg)
