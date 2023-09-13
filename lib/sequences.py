#!/usr/bin/env python3

from cgi import print_arguments


def print_fibonacci(length):
    if length == 0:
        fibonacci = []
    elif length == 1:
        fibonacci = [0]
    elif length == 2:
        fibonacci = [0,1]
    else:
        fibonacci = [0,1]
        i = 2
        while i < length:
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
            i += 1
    print(fibonacci)
        