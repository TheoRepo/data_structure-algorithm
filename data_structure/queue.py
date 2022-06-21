#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   queue.py
#@Time    :   2022/06/21 08:31:25
#@Author  :   Theo Yu

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

if __name__ == "__main__":
    print("测试一: 队列")
    q = Queue(5)
    for i in range(4):
        q.push(i)
    print(q.pop())
    q.push(4)

    print("测试二: python队列内置模块")
    from collections import deque
    q = deque([1,2,3,4,5],5)
    q.append(6) # 队尾进队
    print(q.popleft()) # 队首出队
    # 用于双向队列
    q.appendleft(1) # 队首进队
    print(q.pop()) # 队尾出队

    print("测试三: 使用python队列读取文件末尾n行的内容")
    for line in tail(5):
        print(line, end='')