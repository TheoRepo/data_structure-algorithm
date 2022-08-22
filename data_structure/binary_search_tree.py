#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   binary_tree_operation.py
#@Time    :   2022/08/22 10:20:20
#@Author  :   Theo Yu


# 二叉树的常规操作
import random

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
    # 递归
    def query(self,node, val):
        if not node:
            return None
        if node.data < val:
            # 向右边找
            return self.query(node.rchild, val)
        elif node.data > val:
            # 向左边找
            return self.query(node.lchild, val)
        else:
            return node

    # 非递归
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def __remove_node_1(self, node):
        # 情况1：node是叶子节点
        if not node.parent:
            self.node = None
        # 把它和它父亲脱离关系
        if node == node.parent.lchild: # node是它父亲的左孩子
            self.parent.lchild = None
        else: # node是它父亲的右孩子
            node.parent.rchild = None
            
    def __remove_node_21(self, node):
        # 情况2：node只有一个左孩子
        if not node.parent: # 根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild: # node是它父亲的左孩子
            node.parent.lchild = node.lchild 
            node.lchild.parent = node.parent
        else: # node是它父亲的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况2.2：只有一个右孩子
        if not node.parent: # 根节点
            self.root = node.rchild
        elif node == node.parent.lchild: # node是它父亲的左孩子   
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else: # node是它父亲的右孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent    

    def delete(self, val):
        if self.root: # 不是空树
            # 先找到节点
            node = self.query_no_rec(val)
            if not node: # 不存在
                return False 
            # 第一种情况：node是叶子节点
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            # 第二种情况：只有一个左孩子
            elif not node.rchild: # 只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild: # 只有一个右孩子
                self.__remove_node_22(node)
            # 第三种情况：有两个孩子
            else:
                #先找右子树最小的节点
                min_node= node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_node
                # 因为前一步通过递归找左孩子，所以不存在左孩子，那就只剩下两种情况，有一个右孩子，叶子节点
                if min_node.rchild:
                    self.__remove_node_22(min_node) 
                else: 
                    self.__remove_node_1(min_node)


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


# 插入功能测试   
tree = BST([4,6,7,9,2,1,3,5,8])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root) # 中序排列输出的是有序数列
print("")
tree.post_order(tree.root)

# 查询功能测试
li = list(range(0,500,2))
random.shuffle(li)
print("")
tree = BST(li)
print(tree.query_no_rec(4).data)

# 删除功能测试
tree = BST([1,4,2,5,3,8,6,9,7])
tree.in_order(tree.root)
print("")
tree.delete(4)
tree.delete(1)
tree.in_order(tree.root)