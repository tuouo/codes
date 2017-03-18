#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/3/18
import unittest
from collections import defaultdict


def sunday(text, pattern, start=0):
    len_text, len_par = len(text), len(pattern)
    if len_par > len_text:
        return -1
    skip = generate_char(pattern)
    pos = start
    while pos < len_text - len_par + 1:
        off = 0
        while off < len_par and text[pos + off] == pattern[off]:
            off += 1
        if off == len_par:
            return pos - start
        pos += skip[text[pos + len_par]] + 1 if pos+len_par < len_text and text[pos + len_par] in skip else len_par + 1
    return -1


def generate_char(pattern):
    len_par = len(pattern)
    skip = defaultdict(lambda: len_par)
    for i in range(len_par):
        skip[pattern[i]] = len_par - 1 - i
    return skip


class SundayTest(unittest.TestCase):
    def test_sunday(self):
        self.assertEqual(sunday('aababacb', 'ababac', start=1), 0)

    def test_sunday2(self):
        self.assertEqual(sunday('aababacb', 'acb'), 5)

    def test_sunday3(self):
        self.assertEqual(sunday('aababcabababbacb', 'bcababab'), 4)


if __name__ == '__main__':
    unittest.main()
