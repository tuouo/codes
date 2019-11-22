#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: young
# date: 2019/11/22
import unittest
from data_structure.node import BinaryBalancingTreeNode as Node
from data_structure.tree_binary import BinarySearchTree


class BinaryBalancingSearchTree(BinarySearchTree):
    def __init__(self, root=None):
        super().__init__(root)

    @classmethod
    def insert(cls, root, val):
        if root is None:
            root = Node(val)
            root.height = cls.find_height(root)
            return root
        if val < root.value:
            root.left = cls.insert(root.left, val)
        elif val > root.value:
            root.right = cls.insert(root.right, val)
        else:
            raise ValueError('value has already in tree')

        balance = cls.height(root.left) - cls.height(root.right)
        if balance > 1:
            if cls.height(root.left.left) < cls.height(root.left.right):
                root.left = cls.left_rotate(root.left)
            root = cls.right_rotate(root)
        elif balance < -1:
            if cls.height(root.right.left) > cls.height(root.right.right):
                root.right = cls.right_rotate(root.right)
            root = cls.left_rotate(root)
        else:
            root.height = cls.find_height(root)
        return root

    @classmethod
    def find_height(cls, root):
        if root is None:
            return -1
        else:
            return 1 + max(cls.find_height(root.left), cls.find_height(root.right))

    @classmethod
    def height(cls, root):
        return -1 if root is None else root.height

    @classmethod
    def left_rotate(cls, root):
        item = root.right
        root.right = item.left
        item.left = root
        root.height = cls.find_height(root)
        item.height = cls.find_height(item)
        return item

    @classmethod
    def right_rotate(cls, root):
        item = root.left
        root.left = item.right
        item.right = root
        root.height = cls.find_height(root)
        item.height = cls.find_height(item)
        return item


class TestBinaryBalancingTree(unittest.TestCase):
    def setUp(self):
        tree = BinaryBalancingSearchTree()
        for i in 'DBACEGF':
            tree.root = tree.insert(tree.root, i)

        self.tree = tree
        self.resultPre = list("DBACFEG")
        self.resultMid = list("ABCDEFG")

    def test_balancing(self):
        self.assertEqual(self.tree.pre_order(), self.resultPre)
        self.assertEqual(self.tree.in_order(), self.resultMid)


if __name__ == '__main__':
    unittest.main()
