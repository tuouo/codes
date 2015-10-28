#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def traversePre(root):
    result = []
    if root:
        result += [root.value]
        result += traversePre(root.left)
        result += traversePre(root.right)
    return result

def traverseMid(root):
    result = []
    if root:
        result += traverseMid(root.left)
        result += [root.value]
        result += traverseMid(root.right)
    return result

def traverseAfter(root):
    result = []
    if root:
        result += traverseAfter(root.left)
        result += traverseAfter(root.right)
        result += [root.value]
    return result

def getAfter(pre, mid):
    treeLen = len(pre)
    if treeLen == 0:
        return []
    if treeLen == 1:
        return [pre[0]]
    root = pre[0]
    p = mid.index(root)
    result = getAfter(pre[1: p + 1], mid[:p])
    result += getAfter(pre[p + 1:], mid[p + 1:])
    result += root
    return result

def traNoRecursivePre(root):
    result = []
    if root:
        cur = root
        treeStack = []
        while cur or treeStack:
            while cur:
                result.append(cur.value)
                treeStack.append(cur)
                cur = cur.left
            #if treeStack:
                #cur = treeStack[-1].right
                #treeStack.pop()
            cur = treeStack[-1].right
            treeStack.pop()
    return result

def traNoRecursivePre2(root):
    result = []
    if root:
        treeStack = [root]
        while treeStack:
            temp = treeStack[-1]
            result.append(temp.value)
            treeStack.pop()
            if temp.right:
                treeStack.append(temp.right)
            if temp.left:
                treeStack.append(temp.left)                
    return result

def traNoRecursiveMid(root):
    result = []
    if root:
        cur = root
        treeStack = []
        while cur or treeStack:
            while cur:
                treeStack.append(cur)
                cur = cur.left
            #if treeStack:
                #cur = treeStack[-1]                
                #result.append(cur.value)
                #cur = cur.right
                #treeStack.pop()
            cur = treeStack[-1]                
            result.append(cur.value)
            cur = cur.right
            treeStack.pop()
    return result

def traNoRecursiveMid2(root):
    result = []
    if root:
        cur = root.left
        treeStack = [root]
        while cur or treeStack:
            while cur:
                treeStack.append(cur)
                cur = cur.left
            cur = treeStack[-1]                
            result.append(cur.value)
            cur = cur.right
            treeStack.pop()
    return result

def traNoRecursiveAft(root):
    result = []
    if root:
        visit = None
        cur = root.left
        treeStack = [root]
        while cur or treeStack:
            while cur:
                treeStack.append(cur)
                cur = cur.left
            cur = treeStack[-1]
            if cur.right == None or cur.right == visit:
                result.append(cur.value)
                treeStack.pop()
                visit = cur
                cur = None
            else:
                cur = cur.right
    return result

def traverseLevel(root):
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

def getDepth(root):
    if root == None:
        return 0
    dl = getDepth(root.left)
    dr = getDepth(root.right)
    return 1 + max(dl, dr)

def getNodeNum(root):
    if root == None:
        return 0
    return 1 + getNodeNum(root.left) + getNodeNum(root.right)

import unittest
class tBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
        self.resultPre = list("DBACEGF")
        self.resultMid = list("ABCDEFG")
        self.resultAft = list("ACBFGED")
        self.resultLev = list("DBEACGF")

    def test_pre(self):
        self.assertEqual(traversePre(self.tree), self.resultPre)
    def test_mid(self):
        self.assertEqual(traverseMid(self.tree), self.resultMid)
    def test_after(self):
        self.assertEqual(traverseAfter(self.tree), self.resultAft)
    def test_getAfter(self):
        self.assertEqual(getAfter(self.resultPre, self.resultMid), self.resultAft)

    def test_preNoRe(self):
        self.assertEqual(traNoRecursivePre(self.tree), self.resultPre)
    def test_preNoRe2(self):
        self.assertEqual(traNoRecursivePre2(self.tree), self.resultPre)
    def test_midNoRe(self):
        self.assertEqual(traNoRecursiveMid(self.tree), self.resultMid)
    def test_midNoRe2(self):
        self.assertEqual(traNoRecursiveMid2(self.tree), self.resultMid)
    def test_aftNoRe(self):
        self.assertEqual(traNoRecursiveAft(self.tree), self.resultAft)

    def test_level(self):
        self.assertEqual(traverseLevel(self.tree), self.resultLev)
    def test_dept(self):
        self.assertEqual(getDepth(self.tree), 4)
    def test_num(self):
        self.assertEqual(getNodeNum(self.tree), 7)

if __name__ == '__main__':
    unittest.main()