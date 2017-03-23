#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/3/18
import unittest
import functools


def rb(text, pattern, start=0):
    len_text, len_par = len(text), len(pattern)
    if len_par > len_text:
        return -1
    NUM, PRIME, NUM_L = 2 ** 7 - 1, 2 ** 13 - 1, 1
    for _ in range(len_par):
        NUM_L = (NUM_L * NUM) % PRIME
    hash_par = functools.reduce(lambda total, char: (total * NUM + ord(char)) % PRIME, pattern, 0)
    hash_new = functools.reduce(lambda total, char: (total * NUM + ord(char)) % PRIME, text[start:start+len_par], 0)
    if hash_par == hash_new:
        return 0
    for i in range(start + 1, len_text - len_par + 1):
        hash_new = (hash_new * NUM + ord(text[i+len_par-1]) - ord(text[i-1]) * NUM_L) % PRIME
        if hash_par == hash_new:
            for pos in range(len_par):
                if text[i + pos] != pattern[pos]:
                    break
            if pos == len_par - 1:
                return i - start
    return -1


class RabinKarpTest(unittest.TestCase):
    def test_rb(self):
        self.assertEqual(rb('aababacb', 'abab', start=1), 0)

    def test_rb2(self):
        self.assertEqual(rb('bacb', 'acb'), 1)

    def test_rb3(self):
        self.assertEqual(rb('aababcabababbacb', 'bcababab'), 4)


if __name__ == '__main__':
    unittest.main()
