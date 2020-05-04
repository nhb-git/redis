#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/3/2020  07:06 PM 
# 文件名称   ：redis的发布和订阅.PY
import redis


r = redis.Redis(host='192.168.238.129')
r.publish('fm104.5', 'hello niuhaibao')
