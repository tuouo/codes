#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def traverse_pre(root):
    result = []
    if root:
        result += [root.value]
        result += traverse_pre(root.left)
        result += traverse_pre(root.right)
    return result


def traverse_mid(root):
    result = []
    if root:
        result += traverse_mid(root.left)
        result += [root.value]
        result += traverse_mid(root.right)
    return result


def traverse_after(root):
    result = []
    if root:
        result += traverse_after(root.left)
        result += traverse_after(root.right)
        result += [root.value]
    return result


def get_after_traversed(pre, mid):
    if len(pre) == 0:
        return []
    elif len(pre) == 1:
        return [pre[0]]
    root = pre[0]
    p = mid.index(root)
    result = get_after_traversed(pre[1: p + 1], mid[:p])
    result += get_after_traversed(pre[p + 1:], mid[p + 1:])
    result += root
    return result


def tra_no_recursive_pre(root):
    result = []
    if root:
        cur = root
        tra_tack = []
        while cur or tra_tack:
            while cur:
                result.append(cur.value)
                tra_tack.append(cur)
                cur = cur.left
            cur = tra_tack[-1].right
            tra_tack.pop()
    return result


def tra_no_recursive_pre2(root):
    result = []
    if root:
        later_stack = [root]
        while later_stack:
            temp = later_stack[-1]
            result.append(temp.value)
            later_stack.pop()
            if temp.right:
                later_stack.append(temp.right)
            if temp.left:
                later_stack.append(temp.left)
    return result


def tra_no_recursive_mid(root):
    result = []
    if root:
        cur = root
        tra_tack = []
        while cur or tra_tack:
            while cur:
                tra_tack.append(cur)
                cur = cur.left
            cur = tra_tack[-1]
            result.append(cur.value)
            cur = cur.right
            tra_tack.pop()
    return result


def tra_no_recursive_mid2(root):
    result = []
    if root:
        cur = root.left
        tra_tack = [root]
        while cur or tra_tack:
            while cur:
                tra_tack.append(cur)
                cur = cur.left
            cur = tra_tack[-1]
            result.append(cur.value)
            cur = cur.right
            tra_tack.pop()
    return result


def tra_no_recursive_aft(root):
    result = []
    if root:
        visit = None
        cur = root.left
        later_stack = [root]
        while cur or later_stack:
            while cur:
                later_stack.append(cur)
                cur = cur.left
            cur = later_stack[-1]
            if cur.right is None or cur.right == visit:
                result.append(cur.value)
                later_stack.pop()
                visit = cur
                cur = None
            else:
                cur = cur.right
    return result


def traverse_level(root):
    result = []
    if root:
        result = [root.value]
        cur = [root]
        while cur:
            p = cur[0]
            cur.pop(0)
            if p.left:
                cur.append(p.left)
                result.append(p.left.value)
            if p.right:
                cur.append(p.right)
                result.append(p.right.value)
    return result


def get_depth(root):
    if root is None:
        return 0
    dl = get_depth(root.left)
    dr = get_depth(root.right)
    return 1 + max(dl, dr)


def get_node_num(root):
    if root is None:
        return 0
    return 1 + get_node_num(root.left) + get_node_num(root.right)


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
        self.resultPre = list("DBACEGF")
        self.resultMid = list("ABCDEFG")
        self.resultAft = list("ACBFGED")
        self.resultLev = list("DBEACGF")

    def test_pre(self):
        self.assertEqual(traverse_pre(self.tree), self.resultPre)

    def test_mid(self):
        self.assertEqual(traverse_mid(self.tree), self.resultMid)

    def test_after(self):
        self.assertEqual(traverse_after(self.tree), self.resultAft)

    def test_getAfter(self):
        self.assertEqual(get_after_traversed(self.resultPre, self.resultMid), self.resultAft)

    def test_preNoRe(self):
        self.assertEqual(tra_no_recursive_pre(self.tree), self.resultPre)

    def test_preNoRe2(self):
        self.assertEqual(tra_no_recursive_pre2(self.tree), self.resultPre)

    def test_midNoRe(self):
        self.assertEqual(tra_no_recursive_mid(self.tree), self.resultMid)

    def test_midNoRe2(self):
        self.assertEqual(tra_no_recursive_mid2(self.tree), self.resultMid)

    def test_aftNoRe(self):
        self.assertEqual(tra_no_recursive_aft(self.tree), self.resultAft)

    def test_level(self):
        self.assertEqual(traverse_level(self.tree), self.resultLev)

    def test_dept(self):
        self.assertEqual(get_depth(self.tree), 4)

    def test_num(self):
        self.assertEqual(get_node_num(self.tree), 7)


if __name__ == '__main__':
    unittest.main()
