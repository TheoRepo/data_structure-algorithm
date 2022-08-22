#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   binary_tree.py
#@Time    :   2022/08/08 09:01:48
#@Author  :   Theo Yu


# 二叉树就是度不超过2的树
class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None # 左孩子
        self.rchild = None # 右孩子

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f 

root = e

print(root.lchild.rchild.data)

# 二叉树怎么遍历
# 前序遍历

# 仅仅知道前序遍历的序列，是无法确定这颗树的
# 但是如果知道两种遍历序列，这棵树就是可以确定的
# 例子：前序序列+中序序列
# 前序序列：第一个是根
# 中序序列：根的左边是左子树，右边是右子树
from collections import deque

def pre_order(root):
    if root:
    # 如果是空，递归终止
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

# 中序遍历（根节点在中间）
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)

# 后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')

# 层次遍历
# 逐层输出
# 运用队列去实现
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0: # 只要队不空
        node = queue.popleft()
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


# pre_order(root)
# in_order(root)
# post_order(root)
level_order(root)

# 二叉搜索树
# 二叉搜索树是一个颗二叉树且满足性质：
# 设x是二叉树的一个节点。如果y是x左子树的一个节点，那么y.key <= x.key；
# 如果y是x右子树的一个节点,那么y.key >= x.key

# 二叉搜索树的操作：查询、插入、删除
# 查询：和树的深度有关
# O(log(n))
# 插入：向叶子节点插入，向深度走
# 
# 删除：




