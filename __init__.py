#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import *


def int_to_tuple(x: int) -> tuple[int]:
    result = ()
    d = floor(log10(x))
    for i in range(d + 1):
        result = (x % 10 ** (i + 1) // 10 ** i,) + result
    return result


def is_self_descriptive(x: int) -> bool:
    tup = int_to_tuple(x)
    for i in tup:
        if tup[i] != tup.count(i):
            break
    else:
        return True
    return False


if __name__ == "__main__":
    for num in (2_019, 2_020, 6_210_001_000):
        print(f"{num} {'is' if is_self_descriptive(num) else 'is not'} self descriptive")

    # 2019 is not self descriptive
    # 2020 is self descriptive
    # 6210001000 is self descriptive
