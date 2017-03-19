#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/3/19


class Stack:
    """
    Stack ADT, using python list
    is_empty()
    length()
    pop(): assert not empty
    peek(): assert not empty, return top of non-empty stack without removing it
    push(item)
    clear()
    """

    def __init__(self):
        self._items = list()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)

    def pop(self):
        assert not self.is_empty()
        return self._items.pop()

    def peek(self):
        assert not self.is_empty()
        return self._items[-1]

    def push(self, item):
        self._items.append(item)

    def clear(self):
        del self._items[:]

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            return self._items.pop()


class StackLinked:
    """
    Stack ADT, use linked list
    """
    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        return self._top is None

    def __len__(self):
        return self._size

    def pop(self):
        assert not self.is_empty()
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item

    def peek(self):
        assert not self.is_empty()
        return self._top.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1

    def clear(self):
        self._top = None
        self._size = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            return self.pop()


class _StackNode:
    def __init__(self, item, origin):
        self.item = item
        self.next = origin


if __name__ == '__main__':
    def divide_by_2(num):
        # digitals = Stack()
        digitals = StackLinked()
        while num > 0:
            digitals.push(num & 1)
            num >>= 1
        return "".join([str(num) for num in digitals])


    assert int(divide_by_2(233), 2) == 233
