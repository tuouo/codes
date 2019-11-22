#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: young
# date: 2019/11/22
import unittest
from data_structure.node import TrieNode as Node


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node.starts += 1
            node = node.children[c]
        else:
            node.count += 1

    def search(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c, None)
            if node is None:
                return False
        else:
            return node.count > 0

    def starts_with_num(self, prefix):
        node = self.root
        for c in prefix:
            node = node.children.get(c, None)
            if node is None:
                return 0
        else:
            return node.starts + node.count


class TestDisjointSet(unittest.TestCase):
    def setUp(self):
        trie = Trie()
        for word in ('good', 'goodness'):
            trie.insert(word)
        self.trie = trie

    def test_union(self):
        self.assertEqual(self.trie.starts_with_num('go'), 2)
        self.assertEqual(self.trie.starts_with_num('good'), 2)
        self.assertTrue(self.trie.search('good'))
        self.assertFalse(self.trie.search('go'))


if __name__ == '__main__':
    unittest.main()
