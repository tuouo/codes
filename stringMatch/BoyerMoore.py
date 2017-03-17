#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/3/17
"""
BoyerMooreStringSearch
http://blog.jobbole.com/52830/?repeat=w3tc
"""
import unittest
from collections import defaultdict


def bm(text, pattern, start=0):
    len_text, len_tar = len(text), len(pattern)
    if len_tar > len_text:
        return -1
    bad_char = generate_char(pattern)
    good_suffix = generate_suffix_shift(pattern)
    pos = len_tar - 1 + start
    while pos < len_text:
        t, p = pos, len_tar - 1
        while p >= 0 and text[t] == pattern[p]:
            t, p = t - 1, p - 1
        if p == -1:
            return t + 1 - start
        pos += max(bad_char[text[t]] - (len_tar - 1 - t), good_suffix[len_tar - p])
    return -1


def generate_char(pattern):
    len_par = len(pattern)
    skip = defaultdict(lambda: len_par)
    for i in range(len_par - 1):
        skip[pattern[i]] = len_par - 1 - i
    return skip


def generate_suffix_shift(pattern):
    len_par = len(pattern)
    suffix = generate_suffix_better(pattern)
    # when suffix have no corresponding prefix
    skip = [len_par - 1] * len_par
    skip[len_par - 1] = len_par
    # when suffix have partial prefix
    for i in reversed(range(len_par)):
        if suffix[i] == i + 1:
            for j in range(len_par - 1 - i):
                if skip[j] == len_par:
                    skip[j] == len_par - 1 - i
    # when suffix can be found pre
    for i in range(len_par - 1):
        skip[len_par - 1 - suffix[i]] = len_par - 1 - i
    return skip


def generate_suffix(pattern):
    len_par = len(pattern)
    suffix = [len_par] * len_par
    for i in reversed(range(len_par - 1)):
        # j = 0
        # while j <= i and pattern[i - j] == pattern[len_par - 1 - j]:
        #     j += 1
        # suffix[i] = j
        j = i
        while j >= 0 and pattern[i] == pattern[len_par - 1 - i + j]:
            j -= 1
        suffix[i] = i - j
    return suffix


def generate_suffix_better(pattern):
    len_par = len(pattern)
    suffix = [len_par] * len_par
    f = g = len_par - 1  # last matched end pos, last missed pos
    for i in reversed(range(len_par - 1)):
        if i > g and suffix[(len_par - 1) - (f - i)] < i - g:
            suffix[i] = suffix[len_par - 1 - f + i]
        else:
            g, f = min(i, g), i
            while g >= 0 and pattern[g] == pattern[len_par - 1 - f + g]:
                g -= 1
            suffix[i] = f - g
    return suffix


class BMTest(unittest.TestCase):
    def test_bmh(self):
        self.assertEqual(bm('aababacb', 'ababac', start=1), 0)

    def test_bmh2(self):
        self.assertEqual(bm('aababacb', 'acb'), 5)

    def test_bmh3(self):
        self.assertEqual(bm('aababcabababbacb', 'bcababab'), 4)


if __name__ == '__main__':
    unittest.main()
