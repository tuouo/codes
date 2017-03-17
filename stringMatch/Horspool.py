#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
import unittest
from collections import defaultdict


def horspool(text, pattern, start=0):
    len_text, len_tar = len(text), len(pattern)
    if len_tar > len_text:
        return -1
    skip = defaultdict(lambda: len_tar)
    for i in range(len_tar - 1):
        skip[pattern[i]] = len_tar - 1 - i

    pos = len_tar - 1 + start
    while pos < len_text:
        t, p = pos, len_tar - 1
        while p >= 0 and text[t] == pattern[p]:
            t, p = t - 1, p - 1
        if p == -1:
            return t + 1 - start
        pos += skip[text[pos]]
    return -1


class HorspoolTest(unittest.TestCase):
    def test_bmh(self):
        self.assertEqual(horspool('aababacb', 'ababac', start=1), 0)

    def test_bmh2(self):
        self.assertEqual(horspool('aababacb', 'acb'), 5)


if __name__ == '__main__':
    unittest.main()
