#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   maze_queue.py
#@Time    :   2022/06/21 08:36:00
#@Author  :   Theo Yu


from collections import deque
# 广度优先搜索
# 思路：从一个节点开始，寻找所有接下来能继续走的点，继续不断寻找，直到找到出口。
# 使用队列存储当前正在考虑的节点

dirs = [
    lambda x,y: (x+1,y),
    lambda x,y: (x-1,y),
    lambda x,y: (x,y-1),
    lambda x,y: (x,y+1)
]


def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2]) # 起点
    realpath.reverse()
    for node in realpath:
        print(node)


def maze_path_queue(x1, y1, x2, y2, maze):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:
        curNode = queue.pop()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 终点
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1)) # 后续节点进队，记录哪个节点带他来的
                maze[nextNode[0]][nextNode[1]] = 2 # 标记为已经走过
    else:
        print("没有路")
        return False

if __name__ == "__main__":
    print("测试: 用队列解决迷宫问题")
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
    maze_path_queue(1,1,8,8,maze)