#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   data_structure.py
#@Time    :   2022/06/17 08:06:26
#@Author  :   Theo Yu


# 数据结构是指相互之间存在着一种或多种关系的数据元素的集合和该集合中数据元素之间的关系组成
# 简单来说，数据结构就是设计数据以何种方式组织并存储在计算机中
# 比如：列表、集合于字典都是一种数据结构
# N.Wirth: "程序=数据结构+算法"

# 数据结构按照逻辑结构可分为线性结构、树结构、图结构
# 线性结构：数据结构中的元素存在一对一的相互关系: 列表
# 树结构：数据结构中的元素存在一对多的相互关系
# 图结构：数据结构中的元素存在多对多的相互关系

# 数组和列表有两点不同
# 1.数组元素类型要相同
# 2.数组长度固定
# 32位机器上，一个整数占4个字节，一个地址占4个字节，
# 数组直接存储整数，列表则存储指向数据的地址
# 1.列表的元素类型可以不同（python的解决办法就是，存储指向元素的地址）
# 2.列表的长度不固定(python的解决办法是，append元素，发现原来的列表长度不够了，就开一个新的列表，拷贝旧元素)
# 列表的基本操作
# 按下标查找 O(1)
# append O(1)
# 插入元素 O(n)
# 删除元素 O(n)

# 栈，直观的理解，就是一堆书
# 栈(stack),是一个数据集合，可以理解为只能在一端进行插入或删除操作的列表
# 栈的特点：后进先出 LIFO (last-in, first-out)
# 栈的概念：栈顶、栈底
# 栈的基本操作：
# 进栈（压栈）：push
# 出栈：pop
# 取栈顶：gettop
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


# 栈的应用-括号匹配问题
# 括号匹配问题：给一个字符串，其中包好小括号、中括号、大括号，求改字符串中的括号是否匹配
# 例如
# ()()[]{}  匹配
# ([{()}])  匹配
# [](       不匹配
# [(])      不匹配
def brace_match(s):
    match = {'}':'{', ']':'[', ')':'('}
    stack = Stack()
    for ch in s:
        if ch in {'(','[','{'}:
            stack.push(ch)
        else: # ch in  {')',']','}'}
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else: # stack.get_top() != match[ch]
                return False
    if stack.is_empty():
        return True
    else:
        return False
        

if __name__ == "__main__":

    print("测试一: 栈")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())

    print("测试二: 括号匹配功能")
    print(brace_match('[{()}(){()}[]({}){}]'))
    print(brace_match('[{]'))


        
