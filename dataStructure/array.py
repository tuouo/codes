#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/3/19
import ctypes


class Array:
    def __init__(self, size):
        assert size > 0, "array size must be >0"
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

    def clear(self, value):
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


class Array2D:
    """
    Two-Demensional Arrays
    Array2D(num_row, num_col):  constructor
    num_row()
    num_col()
    clear()
    getitem(r, c)
    setitem(r, c, value)
    """
    def __init__(self, num_row, num_col):
        self._rows = Array(num_row)
        for _ in range(num_row):
            self._rows = Array(num_col)

    @property
    def num_row(self):
        return len(self._rows)

    @property
    def num_col(self):
        return len(self._rows[0])

    def clear(self, value):
        for row in self._rows:
            row.clear(value)

    def __getitem__(self, pos_tuple):
        assert len(pos_tuple) == 2
        row, col = pos_tuple
        assert 0 <= row < self.num_row and 0 <= row < self.num_col
        return self._rows[row][col]

    def __setitem__(self, pos_tuple, value):
        assert len(pos_tuple) == 2
        row, col = pos_tuple
        assert 0 <= row < self.num_row and 0 <= row < self.num_col
        self._rows[row][col] = value


if __name__ == '__main__':
    pass
