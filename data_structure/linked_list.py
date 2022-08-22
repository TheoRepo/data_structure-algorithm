#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   linked_list.py
#@Time    :   2022/06/22 07:38:40
#@Author  :   Theo Yu

# 链表是由一系列节点组成的元素集合。每个节点包含两部分，数据域item和指向下一个节点的指针next。
# 通过节点之间的相互连接，最终串联成一个链表。
# 创建链表的方法：头插法，尾插法
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
    
def create_linklist(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def print_linklist(lk):
    while lk:
        print(lk.item, end= ',')
        lk = lk.next

# 双链表
# 双链表的每个节点有两个指针: 一个指向后一个节点, 另一个指向前一个节点。
# 双链表的基本操作: 双链表的建立, 双链表节点的插入, 双链表节点的删除

# 链表复杂度分析
# 顺序表(列表/数组)与链表
# 按元素值查找  顺序表:O(n)  链表:O(n)
# 按下标查找  顺序表:O(1)  链表:O(n)
# 在某个元素后插入  顺序表:O(n)  链表:O(1)
# 删除某个元素  顺序表:O(n)  链表:O(1)
# 链表在插入和删除的操作上明显快于顺序表
# 链表的内存可以更灵活的分配
# 链表这种链式存储的数据结构对树和图的结构有很大的启发性
 
if __name__ == "__main__":
    print("测试一: 头插法")
    lk1 = create_linklist([1,2,3])
    print_linklist(lk1)
    print("测试二: 尾插法")
    lk2 = create_linklist_tail([4,5,6])
    print_linklist(lk2)
