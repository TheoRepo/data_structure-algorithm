#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   maze_stack.py
#@Time    :   2022/06/21 08:34:50
#@Author  :   Theo Yu

# 栈和队列的应用：迷宫问题
# 给一个二维列表，表示迷宫(0表示通道，1表示围墙)。给出算法，求一条走出迷宫的路径
# 回溯法(深度优先搜索)
# 思路：从一个节点开始，任意找下一个能走的点，当找不到能走的点时，退回上一个点寻找是否有其他方向的点。
# 使用栈存储当前路径


dirs = [
    lambda x,y: (x+1,y),
    lambda x,y: (x-1,y),
    lambda x,y: (x,y-1),
    lambda x,y: (x,y+1)
]


def maze_path(x1,y1,x2,y2,maze):
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
    print("测试: 用栈解决迷宫问题")
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
    maze_path(1,1,8,8,maze)