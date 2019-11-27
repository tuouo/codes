#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: young
# date: 2019/11/22
import unittest


class UnionFindList:
    def __init__(self, n):
        # if not 1--n, may use dict
        self.group = [i for i in range(n+1)]
        self.size = [1] * (n+1)
        self.count = n  # ignore 0

    def find(self, cur):
        t = cur
        while t != self.group[t]:
            t = self.group[t]
        while cur != self.group[cur]:
            p = self.group[cur]
            self.group[cur] = t
            cur = p
        return t

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        t_a, t_b = self.find(a), self.find(b)
        if t_a == t_b:
            return t_a
        if self.size[a] < self.size[b]:
            self.group[t_a] = t_b
            self.size[t_b] += self.size[t_a]
            self.size[t_a] = 0
            self.count -= 1
            return t_b
        else:
            self.group[t_b] = t_a
            self.size[t_a] += self.size[t_b]
            self.size[t_b] = 0
            self.count -= 1
            return t_a

    def count(self):
        return self.count


class UnionFindDict:
    def __init__(self):
        self.group = {}
        self.size = {}
        self.count = 0

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

    def find(self, a):
        if a not in self.group:
            self.group[a], self.size[a] = a, 1
            self.count += 1
            return a
        t = a
        while t != self.group[t]:
            t = self.group[t]
        while a != self.group[a]:
            near = self.group[a]
            self.group[a] = near
            a = near
        return t

    def union(self, a, b):
        A, B = self.find(a), self.find(b)
        if A == B:
            return A
        if self.size[A] >= self.size[B]:
            self.group[B] = A
            self.size[A] += self.size[B]
            del self.size[B]
            self.count -= 1
            return A
        else:
            self.group[A] = B
            self.size[B] += self.size[A]
            del self.size[A]
            self.count -= 1
            return B


class TestDisjointSet(unittest.TestCase):
    def setUp(self):
        edges = ((1, 6), (2, 7), (3, 8), (4, 9), (2, 6))
        graph = UnionFindList(10)
        for a, b in edges:
            graph.union(a, b)
        self.graph = graph

    def test_union(self):
        self.assertEqual(self.graph.size, [1, 0, 4, 2, 2, 1, 0, 0, 0, 0, 1])
        self.assertEqual(self.graph.count, 5)


if __name__ == '__main__':
    unittest.main()
