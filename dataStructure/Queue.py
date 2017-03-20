#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/3/19


class Queue:
    """
    Queue ADT, use list.
    Queue()
    is_empty()
    length()
    enqueue(item)
    dequeue()
    """
    def __init__(self):
        self._queue = list()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._queue)

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        assert not self.is_empty()
        return self._queue.pop(0)


class QueueCircular:
    """
    circular Array. length limited, append, po O(1)
    """
    def __init__(self, size):
        self._start = 0
        self._end = 0
        self._array = _Array(size)

    def is_empty(self):
        return self._start == self._end

    def is_full(self):
        return (self._end + 1) % len(self._array) == self._start

    def __len__(self):
        return (self._end + len(self._array) - self._start) % len(self._array)

    def enqueue(self, item):
        assert not self.is_full()
        self._end = (self._end + 1) % len(self._array)
        self._array[self._end] = item

    def dequeue(self):
        assert not self.is_full()
        item = self._array[self._start]
        self._start = (self._start + 1) % len(self._array)
        return item


class _Array:
    def __init__(self, size):
        assert size > 0, "array size must be >0"
        import ctypes
        self._size = size
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        self.clear()

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert 0 <= index < len(self), "out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert 0 <= index < len(self), "out of range"
        self._elements[index] = value

    def clear(self, value=None):
        """ reset each to value """
        for _ in range(len(self)):
            self._elements[_] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self, items):
        self._items = items
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self._items):
            val = self._items[self._idx]
            self._idx += 1
            return val
        else:
            raise StopIteration


class QueueLinked:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._head is None

    def __len__(self):
        return self._size

    def enqueue(self, item):
        node = _QueueNode(item)
        if self.is_empty():
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        assert not self.is_empty(), "queue is empty"
        node = self._head
        if self._head is self._tail:
            self._tail = None
        self._head = self._head.next
        return node.item


class _QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None


class PriorityQueueUnbounded:
    from collections import namedtuple
    _PriorityEntry = namedtuple('_PriorityEntry', 'item priority')

    def __init__(self):
        self._queue = list()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._queue)

    def enqueue(self, item, priority):
        entry = PriorityQueueUnbounded._PriorityEntry(item, priority)
        self._queue.append(entry)

    def dequeue(self):
        assert not self.is_empty(), "queue is empty"
        highest = 0
        for i in range(len(self)):
            if self._queue[i].priority < self._queue[highest].priority:
                highest = i
        entry = self._queue.pop(highest)
        return entry.item


class PriorityQueueBounded:
    """
    BoundedPriorityQueue ADT, use linked list
    priority in [0, max_priority - 1]
    _queue
    [0] -> ["apple"]
    [1]
    [2] -> ["banana", "peach"]
    [3] -> ["melon"]
    """
    def __init__(self, max_priority):
        self._size = 0
        self._levels = _Array(max_priority)
        for i in range(max_priority):
            self._levels[i] = QueueLinked()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def enqueue(self, item, priority):
        assert 0 <= priority < len(self._levels), "invalid priority"
        self._levels[priority].enqueue(item)
        self._size += 1

    def dequeue(self):
        assert not self.is_empty(), "queue is empty"
        self._size -= 1
        for item in self._levels:
            if not item.is_empty():
                return item.dequeue()


if __name__ == '__main__':
    q = PriorityQueueBounded(10)
    q.enqueue("s", 4)
    q.enqueue("g", 3)
    q.enqueue("v", 9)
    q.enqueue("r", 4)
    q.enqueue("a", 1)
    q.enqueue("o", 4)
    assert q.dequeue() == "a"
    assert q.dequeue() == "g"
    assert q.dequeue() == "s"
    assert q.dequeue() == "r"
    assert q.dequeue() == "o"
    assert q.dequeue() == "v"
