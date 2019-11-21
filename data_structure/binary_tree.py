#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from data_structure.node import BinaryTreeNode as Node


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def build(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            cur = self.root
            while True:
                if val < cur.value:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(val)
                        return True
                elif val > cur.value:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(val)
                        return True
                else:
                    return False
        return True

    def traverse_mid(self):
        return self._traverse_mid(self.root)

    def traverse_pre(self):
        return self._traverse_pre(self.root)

    def traverse_after(self):
        return self._traverse_after(self.root)

    @classmethod
    def _traverse_mid(cls, root):
        result = []
        if root:
            result += cls._traverse_mid(root.left)
            result += [root.value]
            result += cls._traverse_mid(root.right)
        return result

    @classmethod
    def _traverse_pre(cls, root):
        result = []
        if root:
            result += [root.value]
            result += cls._traverse_pre(root.left)
            result += cls._traverse_pre(root.right)
        return result

    @classmethod
    def _traverse_after(cls, root):
        result = []
        if root:
            result += cls._traverse_after(root.left)
            result += cls._traverse_after(root.right)
            result += [root.value]
        return result

    def in_order(self):
        result = []
        if self.root:
            cur, tra_tack = self.root, []
            while cur or tra_tack:
                while cur:
                    tra_tack.append(cur)
                    cur = cur.left
                cur = tra_tack.pop()
                result.append(cur.value)
                cur = cur.right
        return result

    def pre_order_base(self):
        result = []
        if self.root:
            later_stack = [self.root]
            while later_stack:
                cur = later_stack.pop()
                result.append(cur.value)
                if cur.right:
                    later_stack.append(cur.right)
                if cur.left:
                    later_stack.append(cur.left)
        return result

    def pre_order(self):
        result = []
        if self.root:
            cur, tra_tack = self.root, []
            while cur or tra_tack:
                while cur:
                    result.append(cur.value)
                    tra_tack.append(cur)
                    cur = cur.left
                cur = tra_tack.pop().right
        return result

    def post_order(self):
        result = []
        if self.root:
            cur, tra_tack = self.root, []
            while cur or tra_tack:
                while cur:
                    result.append(cur.value)
                    tra_tack.append(cur)
                    cur = cur.right
                cur = tra_tack.pop().left
        return result[::-1]

    def post_order_base(self):
        result = []
        if self.root:
            later_stack = [self.root]
            while later_stack:
                cur = later_stack.pop()
                result.append(cur.value)
                if cur.left:
                    later_stack.append(cur.left)
                if cur.right:
                    later_stack.append(cur.right)
        return result[::-1]

    def post_order_origin(self):
        result = []
        if self.root:
            visit, cur, tra_tack = None, self.root, []
            while cur or tra_tack:
                while cur:
                    tra_tack.append(cur)
                    cur = cur.left
                cur = tra_tack[-1]
                if cur.right is None or cur.right == visit:
                    result.append(cur.value)
                    tra_tack.pop()
                    visit = cur
                    cur = None
                else:
                    cur = cur.right
        return result

    @classmethod
    def get_after_traversed(cls, pre, mid):
        if len(pre) == 0:
            return []
        elif len(pre) == 1:
            return [pre[0]]
        root = pre[0]
        p = mid.index(root)
        result = cls.get_after_traversed(pre[1: p + 1], mid[:p])
        result += cls.get_after_traversed(pre[p + 1:], mid[p + 1:])
        result += root
        return result

    def get_depth(self):
        return self._get_depth(self.root)

    @classmethod
    def _get_depth(cls, root):
        if root is None:
            return 0
        return 1 + max(cls._get_depth(root.left), cls._get_depth(root.right))

    def get_node_num(self):
        return self._get_node_num(self.root)

    @classmethod
    def _get_node_num(cls, root):
        if root is None:
            return 0
        return 1 + cls._get_node_num(root.left) + cls._get_node_num(root.right)

    def traverse_level(self):
        result = []
        if self.root:
            cur = [self.root]
            while cur:
                p = cur.pop(0)
                result.append(p.value)
                if p.left:
                    cur.append(p.left)
                if p.right:
                    cur.append(p.right)
        return result


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
        cur, tra_tack = root, []
        while cur or tra_tack:
            while cur:
                result.append(cur.value)
                tra_tack.append(cur)
                cur = cur.left
            cur = tra_tack.pop().right
    return result


def tra_no_recursive_pre2(root):
    result = []
    if root:
        later_stack = [root]
        while later_stack:
            temp = later_stack.pop()
            result.append(temp.value)
            if temp.right:
                later_stack.append(temp.right)
            if temp.left:
                later_stack.append(temp.left)
    return result


def tra_no_recursive_mid(root):
    result = []
    if root:
        cur, tra_tack = root, []
        while cur or tra_tack:
            while cur:
                tra_tack.append(cur)
                cur = cur.left
            cur = tra_tack.pop()
            result.append(cur.value)
            cur = cur.right
    return result


def tra_no_recursive_mid2(root):
    result = []
    if root:
        cur, tra_tack = root, []
        while cur or tra_tack:
            while cur:
                tra_tack.append(cur)
                cur = cur.left
            cur = tra_tack.pop()
            result.append(cur.value)
            cur = cur.right
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
        cur = [root]
        while cur:
            p = cur.pop(0)
            result.append(p.value)
            if p.left:
                cur.append(p.left)
            if p.right:
                cur.append(p.right)
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


class TestBinaryTreeClass(unittest.TestCase):
    def setUp(self):
        tree = BinarySearchTree()
        for i in 'DBACEGF':
            tree.build(i)
        self.tree = tree
        self.resultPre = list("DBACEGF")
        self.resultMid = list("ABCDEFG")
        self.resultAft = list("ACBFGED")
        self.resultLev = list("DBEACGF")

    def test_order(self):
        self.assertEqual(self.tree.traverse_pre(), self.resultPre)
        self.assertEqual(self.tree.pre_order(), self.resultPre)
        self.assertEqual(self.tree.pre_order_base(), self.resultPre)

        self.assertEqual(self.tree.traverse_mid(), self.resultMid)
        self.assertEqual(self.tree.in_order(), self.resultMid)

        self.assertEqual(self.tree.traverse_after(), self.resultAft)
        self.assertEqual(self.tree.post_order(), self.resultAft)
        self.assertEqual(self.tree.post_order_base(), self.resultAft)
        self.assertEqual(self.tree.post_order_origin(), self.resultAft)

    def test_tree(self):
        self.assertEqual(self.tree.get_after_traversed(self.resultPre, self.resultMid), self.resultAft)
        self.assertEqual(self.tree.traverse_level(), self.resultLev)
        self.assertEqual(self.tree.get_depth(), 4)
        self.assertEqual(self.tree.get_node_num(), 7)


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
