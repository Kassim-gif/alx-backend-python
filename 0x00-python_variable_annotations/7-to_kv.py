#!/usr/bin/env python3
'''Task 7's module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts tha key and its value to a tuple of tha key and
    tha square of its value.
    '''
    return (k, float(v**2))
