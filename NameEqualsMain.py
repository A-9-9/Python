#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module'

__author__ = "Ken"

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello world.")
    elif len(args) == 2:
        print("Hello %s" % args[1])
    else:
        print("Too many arguments.")
# executed in command line(the main file), compiler will set __name__ = __main__
# if we import the module, it won't be the main file
# so we can execute some extra instruction when we exe this file in command line.
if __name__ == "__main__":
    print('Execute by command line.')
    test()

__password = '123456'
def _check(n):
    return __password == n
def login(n):
    print("Success" if _check(n) else "Failure")