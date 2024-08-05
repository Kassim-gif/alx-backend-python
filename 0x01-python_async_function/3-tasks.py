#!/usr/bin/env python3
'''Task tha 3's module.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates tha asynchronous tasks of wait_random.
    '''
    return asyncio.create_task(wait_random(max_delay))
