#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: young
# date: 2019/11/20
from collections.abc import Iterable
from data_structure.node import Node


class Nodes(Node):
    @staticmethod
    def create_nodes(values):
        if isinstance(values, Iterable):
            head = pre = None
            for value in values:
                cur = Node(value)
                if not head:
                    head = cur
                if pre:
                    pre.next = cur
                pre = cur
            return head
        else:
            return Node(values)

    @staticmethod
    def print_nodes(head):
        values, cur = [], head
        while cur:
            values.append(cur.data)
            cur = cur.next
        return ' -> '.join(map(str, values))

    @staticmethod
    def is_equal(one, other):
        cur, compare = one, other
        while cur and compare:
            if cur.data != compare.data:
                return False
            cur, compare = cur.next, compare.next
        if cur or compare:
            return False
        return True

    @staticmethod
    def values_to_end(head):
        values, cur = [], head
        while cur:
            values.append(cur.data)
            cur = cur.next
        return values

    @staticmethod
    def get_tail(head):
        tail = head
        while tail.next:
            tail = tail.next
        return tail

    @staticmethod
    def insert(head, node_data):
        node = Node(node_data)
        if not head:
            return node
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = node
        return head

    @staticmethod
    def insert_head(head, node_data):
        return Node(node_data, head)

    @staticmethod
    def insert_items(head, nodes_data):
        if not head:
            head = pre = None
            for value in nodes_data:
                cur = Node(value)
                if not head:
                    head = cur
                if pre:
                    pre.next = cur
                pre = cur
            return head
        else:
            tail = head
            while tail.next:
                tail = tail.next
            for value in nodes_data:
                tail.next = Node(value)
                tail = tail.next
            return head

    @staticmethod
    def insert_at_position(head, node_data, pos):
        assert pos >= 0, 'position need >= 0'
        if not head:
            return Node(node_data)

        num, cur = 0, head
        while num != pos and cur.next:
            num += 1
            cur = cur.next
        if cur.next is None and (num + 1) == pos:
            cur.next = Node(node_data)
        else:
            new = Node(cur.data, cur.next)
            cur.next, cur.data = new, node_data
        return head

    @staticmethod
    def append_nodes(one, other):
        if not one:
            return other
        else:
            tail = one
            while tail.next:
                tail = tail.next
            tail.next = other
            return one

    @staticmethod
    def delete(head, pos=None):
        assert head, 'list not has item'
        if pos is None:
            pre, behind = head, head.next
            if behind is None:
                return None
            while behind.next:
                pre, behind = behind, behind.next
            pre.next = None
            return head
        elif pos == 0:
            return head.next
        else:
            cur, num = head, 1
            while pos > num:
                if not cur.next:
                    return head
                cur = cur.next
                num += 1
            if cur.next:
                cur.next = cur.next.next
            return head

    @staticmethod
    def reverse(head):
        tmp, new = head, None
        while head:
            head, tmp.next = head.next, new
            tmp, new = head, tmp
        return new

    @staticmethod
    def sort(head):
        if head is None:
            return None
        values, cur = [], head
        while cur:
            values.append(cur.data)
            cur = cur.next
        cur = head
        for value in sorted(values):
            cur.data = value
            cur = cur.next
        return head

    @staticmethod
    def merge_sorted(one, other_list):
        if not other_list:
            return one
        sentry = cur = Node(0)
        first, second = one, other_list
        while first and second:
            if second.data > first.data:
                cur.next, cur, first = first, first, first.next
            else:
                cur.next, cur, second = second, second, second.next
        cur.next = first if first else second
        return sentry.next

    @staticmethod
    def delete_sorted_duplicate(head):
        if head is None:
            return None
        pre, behind = head, head.next
        while behind:
            if pre.data == behind.data:
                behind = pre.next = behind.next
            else:
                pre, behind = behind, behind.next
        return head

    @staticmethod
    def has_cycle(head):
        fast = slow = head
        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
            if fast.real_equal(slow):
                return True
        else:
            return False

    @staticmethod
    def merge_point(one, other_list):
        length1 = length2 = 0
        move = one
        while move:
            move = move.next
            length1 += 1
        move = other_list
        while move:
            move = move.next
            length2 += 1
        move1, move2 = one, other_list
        if length1 > length2:
            while length2 != length1:
                move1 = move1.next
                length1 -= 1
        else:
            while length2 != length1:
                move2 = move2.next
                length2 -= 1
        while move1.data != move2.data:
            move1, move2 = move1.next, move2.next
        return move1.data


if __name__ == '__main__':
    nodes = Nodes.create_nodes(0)
    assert Nodes.print_nodes(nodes) == '0'
    nodes = Nodes.insert_items(nodes, range(1, 3))
    assert Nodes.print_nodes(nodes) == '0 -> 1 -> 2'
    compare = Nodes.create_nodes(range(3))
    assert Nodes.is_equal(nodes, compare)
    assert Nodes.values_to_end(nodes) == list(range(3))

    nodes = Nodes.insert(nodes, 4)
    nodes = Nodes.insert_head(nodes, -1)
    assert Nodes.print_nodes(nodes) == '-1 -> 0 -> 1 -> 2 -> 4'
    compare = Nodes.insert_head(None, -1)
    compare = Nodes.insert_at_position(compare, 4, pos=1)
    compare = Nodes.insert_at_position(compare, 2, pos=1)
    compare = Nodes.insert_at_position(compare, 1, pos=1)
    compare = Nodes.insert_at_position(compare, 0, pos=1)
    assert Nodes.is_equal(nodes, compare)

    compare = Nodes.delete(compare, 2)
    compare = Nodes.delete(compare)
    compare = Nodes.delete(compare, 0)
    compare = Nodes.reverse(compare)
    assert Nodes.print_nodes(compare) == '2 -> 0'
    nodes = Nodes.append_nodes(nodes, compare)
    nodes = Nodes.sort(nodes)
    assert Nodes.print_nodes(nodes) == '-1 -> 0 -> 0 -> 1 -> 2 -> 2 -> 4'
    nodes = Nodes.delete_sorted_duplicate(nodes)
    assert Nodes.print_nodes(nodes) == '-1 -> 0 -> 1 -> 2 -> 4'

    nodes = Nodes.merge_sorted(nodes, Nodes.create_nodes(range(2)))
    assert Nodes.print_nodes(nodes) == '-1 -> 0 -> 0 -> 1 -> 1 -> 2 -> 4'
    assert Nodes.has_cycle(nodes) is False
    nodes_tail = Nodes.get_tail(nodes)
    nodes_tail.next = nodes.next
    assert Nodes.has_cycle(nodes) is True
    nodes_tail.next = nodes.next.next
    assert Nodes.has_cycle(nodes) is True

    compare = Nodes.create_nodes(range(3, 6))
    compare_tail = Nodes.get_tail(compare)
    compare_tail.next = nodes_tail.next
    nodes_tail.next = None
    assert Nodes.merge_point(nodes, compare) == 0
    compare_tail.next = compare_tail.next.next
    assert Nodes.merge_point(nodes, compare) == 1
