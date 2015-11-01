#！/usr/bin/env/python3
# -*- coding: utf-8 -*-
"simulation of Java Bitset"
# https://www.python.org/dev/peps/pep-0237/
# import sys
# print(sys.maxsize)

class BitSet(object):
    def __init__(self, nbits):
        self.nbits = nbits

    def __init__(self):
    	self.nbits = BITS_PER_WORD