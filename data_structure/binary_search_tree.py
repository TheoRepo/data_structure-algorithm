#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   binary_tree_operation.py
#@Time    :   2022/08/22 10:20:20
#@Author  :   Theo Yu


# 二叉树的常规操作
from dataclasses import dataclass


class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None # 左孩子
        self.rchild = None # 右孩子
        self.parent = None

class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    # 递归（慢）
    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    # 非递归
    def insert_no_rec(self, val):
        p = self.root
        if not p:   # 空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
            else:
                return

    def pre_order(self, root):
        if root:
        # 如果是空，递归终止
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序遍历（根节点在中间）
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    # 后序遍历
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')
        
tree = BST([4,6,7,9,2,1,3,5,8])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
print("")
tree.post_order(tree.root)