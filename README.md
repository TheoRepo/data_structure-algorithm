# 数据结构和算法学习笔记
[课程链接](https://www.bilibili.com/video/BV1uA411N7c5?p=1)

# 目录
+ 算法
    + 汉诺塔问题
    + 搜索
        + 线性查找
        + 二分法查找
        + 
    + 排序算法
        + 冒泡排序
        + 选择排序
        + 插入排序
        + 快速排序
        + 堆排序
        + 归并排序
        + 希尔排序
        + 计数排序
        + 桶排序
        + 基数排序
+ 数据结构
    + 列表
    + 栈
    + 队列
    + 链表
    + 哈希表
    + 树

# 学习心得
1. 把算法拆解成几个部分，每个部分通过动画辅助理解，是比较直观的
比如：归并算法的时间复杂度是多少？
![](/pic/merge_sort.png)
比如：队列是如何实现的？
![](/pic/queue_realization.png)
栈和队列的应用：迷宫问题
![](/pic/迷宫问题_栈.png)
![](/pic/迷宫问题_队列.png)
链表的操作
![](/pic/链表的插入.png)
![](/pic/链表的删除.png)
双链表的操作
![](/pic/双链表的插入.png)
![](/pic/双链表的删除.png)


2. 想不清楚了就写例子
建议：代码的逻辑想不清楚的时候，就要结合具体的例子，看动画。比如希尔排序用到了插入排序，但是插入排序想不明白了，就应该回去看动画。

# 课程随笔
NB三人组小结
三种算法的时间复杂度都是O(nlog(n))
一般情况下，就运行时间而言：
快速排序 < 归并排序 < 堆排序
三种排序算法的缺点：
快速排序：极端情况下排序效率低
归并排序：需要额外的内存开销
堆排序：在快的排序算法种相对较慢

希尔排序
希尔排序（shell sort）是一种分组插入排序算法
首先取一个整数d1=n/2,将元素分为d1个组，每组相邻量元素之间距离为d1,在各组内进行直接插入排序；
取第二个整数d2=d1/2,重复上述分组排序过程，直到di=1，即将所有元素在同一个组内进行直接插入排序。
希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序；最后一趟排序使得所有数据有序。


