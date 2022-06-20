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


# 队列
# 队列(Queue)是一个数据集合，仅允许在列表的一端进行插入，另一端进行删除。
# 进行插入的一端称为队尾(rear),插入动作称为进队或入队
# 进行删除的一端称为队头(front),删除动作称为出队
# 队列的性质：先进先出(First-in, First-out)
# 队列有如下几个操作：
# push(x) : 将 x 压入队尾 
# pop() : 删除并返回队首元素

# 队列的实现方式
# 环形队列：当队尾指针front == Maxsize -1 时，再前进一个位置就自动到0
# 队首指针前进：front = (front + 1) % MaxSize
# 队尾指针前进：rear = (rear + 1) % MaxSize
# 队空条件：rear == front
# 队满条件：(rear + 1) % MaxSize == front
class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0 # 队尾指针
        self.front = 0 # 队首指针

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")

    # 判断队空
    def is_empty(self):
        return self.rear == self.front

    # 判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


# 双向队列
# 双向队列的两端都支持进队和出队操作
# 双向队列的基本操作
# 队首进队
# 队首出队
# 队尾进队
# 队尾出队

# python队列内置模块
# 使用方法 from collections import deque
# 创建队列 queue = deque()
# 进队 append()
# 出队 popleft()
# 双向队列队首进队 appendleft()
# 双向队列队尾出队 pop()

# 读取文件末尾n行的内容
# 使用python队列内置模块实现
def tail(n):
    with open('test.txt', 'r') as f:
        a= deque(f, n)
        return a

# 栈和队列的应用：迷宫问题
# 给一个二维列表，表示迷宫(0表示通道，1表示围墙)。给出算法，求一条走出迷宫的路径
# 回溯法
# 思路：从一个节点开始，任意找下一个能走的点，当找不到能走的点时，退回上一个点寻找是否有其他方向的点。
# 使用栈存储当前路径
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]
dirs = [
    lambda x,y: (x+1,y),
    lambda x,y: (x-1,y),
    lambda x,y: (x,y-1),
    lambda x,y: (x,y+1)
]

def maze_path(x1,y1,x2,y2):
    stack = []
    stack.append((x1, y1))
    while(len(stack)>0):
        curNode = stack[-1] # 当前的节点
        if curNode[0] == x2 and curNode[1] == y2:
            # 走到重点了
            for p in stack:
                print(p)
            return True
        
        # x,y四个方向，x-1,y; x+1,y ;x,y-1; x,y+1
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2 # 表示为已经走过
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print("没有路")
        return False


if __name__ == "__main__":

    print("测试: 栈")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())

    print("测试: 括号匹配功能")
    print(brace_match('[{()}(){()}[]({}){}]'))
    print(brace_match('[{]'))

    print("测试: 队列")
    q = Queue(5)
    for i in range(4):
        q.push(i)
    print(q.pop())
    q.push(4)

    print("测试: python队列内置模块")
    from collections import deque
    q = deque([1,2,3,4,5],5)
    q.append(6) # 队尾进队
    print(q.popleft()) # 队首出队
    # 用于双向队列
    q.appendleft(1) # 队首进队
    print(q.pop()) # 队尾出队

    print("测试: 使用python队列读取文件末尾n行的内容")
    for line in tail(5):
        print(line, end='')
        
    print("测试: 迷宫问题")
    maze_path(1,1,8,8)