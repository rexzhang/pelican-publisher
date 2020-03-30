#!/usr/bin/env python
# coding=utf-8


from celery import shared_task


@shared_task
def demo_task():
    print('demo task')
