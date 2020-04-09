#!/usr/bin/env python
# coding=utf-8

import json

import redis


def get_pending_task_list():
    r = redis.Redis()
    raw_task_info_list = r.lrange('celery', -100, 100)

    task_info_list = list()
    for raw_task_info in raw_task_info_list:
        j = json.loads(raw_task_info)
        task_info = {
            'id': j['headers']['id'],
            'info': j['headers']['argsrepr'],
        }
        task_info_list.append(task_info)

    return task_info_list
