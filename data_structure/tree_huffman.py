#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: young
# date: 2019/11/22
import heapq
import unittest
from data_structure.node import HuffmanNode as Node


class HuffmanTree(Node):
    CODE_LEFT, CODE_RIGHT = '0', '1'

    def __init__(self, freq):
        self.root = self.build_tree(freq)
        self.code_hidden = {}  # init in method gen_code
        self.gen_code(self.root, "")
        if len(self.code_hidden) == 1:
            for key in self.code_hidden:
                self.code_hidden[key] = self.CODE_LEFT

    @staticmethod
    def build_tree(freq):
        count, h = 0, []
        for key, value in freq.items():
            count += 1
            heapq.heappush(h, (value, key, Node(value, key, count)))

        while len(h) != 1:
            a = heapq.heappop(h)
            b = h[0]
            count += 1
            obj = Node(a[0] + b[0], None, count)
            obj.left, obj.right = a[2], b[2]
            h[0] = (obj.freq, obj.data, obj)
            heapq.heapify(h)

        root = h[0]
        root = root[2]  # contains root object
        return root

    def gen_code(self, obj, already):
        if obj is None:
            return
        elif obj.data is not None:
            self.code_hidden[obj.data] = already

        self.gen_code(obj.left, already + self.CODE_LEFT)
        self.gen_code(obj.right, already + self.CODE_RIGHT)

    def decode(self, s):
        result, cur = [], self.root
        for b in s:
            if b == self.CODE_LEFT:
                cur = cur.left
            else:
                cur = cur.right
            if cur.data is not None:
                result.append(cur.data)
                cur = self.root
        return ''.join(map(str, result))


class TestHuffmanTree(unittest.TestCase):
    def setUp(self):
        from collections import defaultdict
        nums = 'AAABC'
        freq = defaultdict(int)
        for char in nums:
            freq[char] += 1
        self.tree = HuffmanTree(freq)
        self.codes = {'B': '00', 'C': '01', 'A': '1'}

    def test_code(self):
        self.assertEqual(self.tree.code_hidden, self.codes)
        codes, nums = '1001011', 'ABACA'
        self.assertEqual(self.tree.decode(codes), nums)


if __name__ == '__main__':
    unittest.main()
