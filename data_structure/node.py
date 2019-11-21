#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: young
# date: 2019/11/19


class Node:
    def __init__(self, node_data, next_node=None):
        self.data = node_data
        self.next = next_node

    def __str__(self):
        return str(self.data) if self.data is not None else 'None'

    def __eq__(self, other):
        return self.data == other.data

    def real_equal(self, other):
        return id(self) == id(other)


class NodeDoubly(Node):
    def __init__(self, node_data, next_node=None, pre_node=None):
        self.data = node_data
        self.pre = pre_node
        self.next = next_node


class BinaryTreeNode(Node):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return id(self) == id(other)


if __name__ == '__main__':
    pass
