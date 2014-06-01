# -*- coding: utf-8 -*-

import sys


def transformation(string):
    ret = []
    for char in string:
        number = ord(char)
        ret.append(bin(number)[2:].zfill(8))
    return ret


if __name__ == '__main__':
    print(' '.join(transformation(sys.argv[1])))
