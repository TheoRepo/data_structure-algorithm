#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   tree.py
#@Time    :   2022/08/04 13:53:49
#@Author  :   Theo Yu

# 树是一种数据结构 比如:目录结构
# 树是一种可以递归定义的数据结构

# 树是由n个节点组成的集合
# 如果n=0, 那这是一颗空树
# 如果n>0, 那存在1个节点作为树的根节点，其他节点可以分为m个集合，每个集合本身又是一棵树

# 一些概念：根节点、叶子节点、树的深度（高度）、树的度、孩子节点/父节点，子树

class Node:
    # 树--链式存储
    def __init__(self, name, type= 'dir'):
        self.name = name
        self.type = type #"dir" or "file"
        self.children = []
        self.parent = None
        # to do
        # 实现文件：文件不能append
       
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        # name 以/结尾
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        # to do
        # 支持绝对路径的思路：按照/ split,判断第一个未知是否位空，为空就是绝对路径
        # 绝对路径从root开始走
        if name[-1] != "/":
            name += "/"
        if name == "../":
            self.now = self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError("invalid dir")


if __name__=="__main__":
    # tree = FileSystemTree()
    # tree.mkdir("var/")
    # print(tree.root.children)


    tree = FileSystemTree()
    tree.mkdir("var/")
    tree.mkdir("bin/")
    tree.mkdir("usr/")

    tree.cd("bin/")
    tree.mkdir("python/")

    tree.cd("../")
    
    print(tree.ls())

