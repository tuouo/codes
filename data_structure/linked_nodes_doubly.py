#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: young
# date: 2019/11/21
from collections.abc import Iterable
from data_structure.node import NodeDoubly


class NodesDoubly(NodeDoubly):
    @staticmethod
    def create_nodes(values):
        if isinstance(values, Iterable):
            head = pre = None
            for value in values:
                cur = NodeDoubly(value)
                if not head:
                    head = cur
                if pre:
                    pre.next, cur.pre = cur, pre
                pre = cur
            return head
        else:
            return NodeDoubly(values)

    @staticmethod
    def print_nodes(head):
        values, cur = [], head
        while cur:
            values.append(cur.data)
            cur = cur.next
        return ' <-> '.join(map(str, values))

    @staticmethod
    def sorted_insert(head, data):
        added = NodeDoubly(data)
        if not head:
            return added
        if head.data > data:
            added.next, head.pre = head, added
            return added
        cur = head
        while cur:
            if cur.data > data:
                added.next, added.pre = cur, cur.pre
                cur.pre, added.pre.next = added, added
                break
            else:
                if cur.next:
                    cur = cur.next
                else:
                    cur.next, added.pre = added, cur
                    break
        return head

    @staticmethod
    def reverse(head):
        if not head:
            return
        left = right = head
        while right.next:
            right = right.next
        while left != right:
            left.data, right.data = right.data, left.data
            if left.next == right:
                break
            left, right = left.next, right.pre
        return head


if __name__ == '__main__':
    nodes = NodesDoubly.create_nodes(range(5))
    nodes = NodesDoubly.sorted_insert(nodes, 2.5)
    assert NodesDoubly.print_nodes(nodes) == '0 <-> 1 <-> 2 <-> 2.5 <-> 3 <-> 4'
    nodes = NodesDoubly.reverse(nodes)
    assert NodesDoubly.print_nodes(nodes) == '4 <-> 3 <-> 2.5 <-> 2 <-> 1 <-> 0'
