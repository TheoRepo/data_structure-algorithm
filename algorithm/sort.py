#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   sort.py
#@Time    :   2022/06/17 08:16:29
#@Author  :   Theo Yu


import random
import copy
import sys 
sys.path.append("..") 
from utils.cal_time import cal_time

# 冒泡排序
# 算法复杂度O(n^2)
@cal_time
def bubble_sort(li):
    for i in range(len(li)-1): # 第i趟
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j] , li[j+1] = li[j+1], li[j]


# 选择排序
# 算法复杂度O(n^2)
@cal_time
def select_sort(li):
    for i in range(len(li)-1): # i是第几趟
        # 选出无序区的最小值
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        # 找到最小值后，和无序区的第一个值做交换
        li[i], li[min_loc] = li[min_loc], li[i]


# 插入排序
# 算法复杂度: O(n^2)
# 思想：扑克牌洗牌
# 初始时手里（有序区）只有一张牌
# 每次（从无序区）摸一张牌，插入到手里已有牌的正确位置

# 关键问题：1.摸什么牌 2.插在什么位置
@cal_time
def insert_sort(li):
    for i in range(1, len(li)):# i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1 #j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:# 手里的牌的顺序是从右往左，从大到小递减
            li[j+1] = li[j] # 手里的牌往右挪个位置
            j -=1
        li[j+1] = tmp # 向空位插入


# 快速排序
# 快排的时间复杂度O()
# 快排的思路
# 取一个元素p(第一个元素)，使元素p归位
# 列表被p分成两部分，左边都比p小，右边都比p大
# 递归完成排序
def partition(li, left, right):
    # 把第一个元素存起来
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp: # 从右边找比tmp小的数
            right -= 1 # 往左边走一步
        li[left] = li[right] # 把右边的值写到左边空位上
        # print(li,'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left] # 把左边的值写道右边空位上
        # print(li,'left')
    li[left] = tmp # 把tmp归位
    return left

@cal_time
def quick_sort(li, left, right):
    def _quick_sort(li, left, right):
        if left < right: # 至少两个元素
            mid = partition(li, left, right)
            _quick_sort(li, left, mid-1)
            _quick_sort(li,mid+1, right)
    return _quick_sort(li, left, right)

# 堆排序
# 堆排序过程
# 1.建立堆。
# 2.得到堆顶元素，为最大元素。
# 3.去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序。
# 4.堆顶元素为第二大元素。
# 5.重复步骤3，直到堆变空。

# 为了节省存储空间
# 拿下来的最大元素，放在列表的尾端
# 时间复杂度O(nlog(n))

# 堆的向下调整过程sift
# 当根节点的左右子树都是堆时，可以通过一次向下的调整来将其变换成一个堆

# 建立大根堆
def sift_big_draft(li, low ,high):
    """
    :param li:列表
    :param low:堆的根节点位置
    :param high:堆的最后一个元素的位置
    :return:
    """
    # high是堆的最后一个元素的下标，low是第一个元素
    i = low # i开始时父亲节点
    j = 2 * i + 1 # j开始是左孩子
    tmp = li[low] # 把堆顶存起来
    # 谁放在堆顶？
    while j <= high: # 只要j位置有节点
        # j指向两个孩子节点中较大的那个节点
        if j + 1 <= high and li[j + 1] > li[j]: # 如果右孩子有，并且比较大
            j = j + 1 # j指向右孩子
        # 更大的孩子和tmp比较，谁更大，谁放到堆顶
        if li[j] > tmp:
            li[i] = li[j]
            i = j # 往下看一层
            j = 2 * i + 1
        else: # tmp更大，把tmp放到i的位置上
            li[i] = tmp # 把tmp放到某一级领导的位置 # 重复代码，注释掉
            break
    else:
        li[i] = tmp # 把tmp放到叶子节点上


def sift_big(li, low ,high):
    """
    :param li:列表
    :param low:堆的根节点位置
    :param high:堆的最后一个元素的位置
    :return:
    """
    i = low 
    j = 2 * i + 1
    tmp = li[low] 
    while j <= high: 
        if j + 1 <= high and li[j + 1] > li[j]: 
            j = j + 1 
        if li[j] > tmp:
            li[i] = li[j]
            i = j 
            j = 2 * i + 1
        else: 
            # li[i] = tmp  # 重复代码，注释掉
            break
        li[i] = tmp 


# 堆排序的实现
@cal_time
def heap_sort(li):
    # 构造堆
    n = len(li)
    for i in range((n-2)//2, -1 , -1): # -1表示倒叙，步长是-1
        # i表示建堆的时候调整的部分的根的下标
        sift_big(li, i, n-1)
    # 建堆完成了（农村包围城市）
    for i in range(n-1, -1, -1): 
        # i指向当前堆的最后一个元素
        li[0], li[i] = li[i],li[0]
        sift_big(li, 0, i-1) # i-1是新的high


# 堆排序在python有内置的模块
# heapq
# heapify(x)
# heappush(heap,item)
# heappop(heap)
import heapq #q-> queue 优先队列
import random

def heapq_example():
    li = list(range(100))
    random.shuffle(li)
    heapq.heapify(li) # 建堆
    n = len(li)
    for i in range(n):
        print(heapq.heappop(li), end = ',')


# 堆排序——topk问题
# 现在有n个数，设计算法得到前k大的数 （k<n）
# 解决思路
# 1.排序后切片 O(nlog(n)) 方法瓶颈：上亿的数据量支取10个数
# 2.冒泡排序：k趟 O(nk)
# 3.插入排序：维护一个长度为k的列表 O(nk)
# 4.简单排序：选择最大的数据和无序区的第一个数交换 O(nk)
# 5.堆排序：O(nlog(k))
# 取列表前k个元素建立一个小根堆。堆顶就是目前第k大的数
# 依次向后遍历原列表，对于列表中的元素，如果小于堆顶，则忽略该元素；
# 如果大于堆顶，则将堆顶更换为该元素，并且对堆顶进行一次调整；
# 遍历列表所有元素后，倒序弹出堆顶
def sift_small(li, low, high): # 建立小根堆的sift函数
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]: # 两个孩子节点取比较小的那个数
            j = j + 1
        if li[j] < tmp: # 孩子大，就和父亲节点交换，满足父亲比孩子小
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
        li[i] = tmp


def topk(li, k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift_small(heap, i, k-1)
    # 1.取列表的前k个元素建堆
    for i in range(k, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift_small(heap, 0, k-1)
    # 2.遍历列表的后k+1个元素，如果比堆顶大，就和堆顶元素替换
    for i in range(k-1, -1 ,-1):
        heap[0], heap[i] = heap[i], heap[0]
        sift_small(heap, 0, i - 1)
    # 3.挨个输出：堆顶元素输出，堆最后一个元素放到堆顶，sift
    return heap


# 归并算法
# 什么是归并？
# 列表分两段有序，如何将其合并成为一个有序列表，这种操作称为一次归并
# 分解：将列表越分越小，直至分成一个元素
# 终止条件：一个元素是有序的
# 合并：将两个有序列表归并，列表越来越大
# 写算法，其实就是演绎法，
# 找一个具有代表性的例子，想清楚这个例子执行过程的各个细节（看动画）
# 考虑除了这个例子之外的，其他的典型例子。
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high: # 只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i]) 
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行完，一定是一部分没数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp # 前包括后不包
# li = [2,4,5,7,1,3,6,8]
# merge(li, 0, 3, 7)
# print(li)

# 算法复杂度
# 看图
# 每层是n，log(n)层，所以时间复杂度是O(nlog(n))
# 空间复杂度, O(n)
@cal_time
def merge_sort(li, low, high):
    def _merge_sort(li, low, high):
        if low < high: # 至少有两个元素，递归
            mid = (low + high) // 2
            _merge_sort(li, low ,mid)
            _merge_sort(li, mid+1, high)
            merge(li, low, mid ,high)
    return _merge_sort(li, low, high)


# 希尔排序
# 希尔排序（shell sort）是一种分组插入排序算法
# 首先取一个整数d1=n/2,将元素分为d1个组，每组相邻量元素之间距离为d1,在各组内进行直接插入排序；
# 取第二个整数d2=d1/2,重复上述分组排序过程，直到di=1，即将所有元素在同一个组内进行直接插入排序。
# 希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序；最后一趟排序使得所有数据有序。
# 希尔排序的时间复杂度比较复杂，可以在维基百科上查询，主要和gap的取值有关
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)): #i 表示摸到的牌的下标
        tmp = li[i]
        j = i - gap # 指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j+gap] = tmp


@cal_time
def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //=2


# 计数排序
# 对列表进行排序，已知列表中的数范围都在0到100之间，设计时间复杂度为O(n)的算法
# 比较排序的时间复杂度，最快是O(nlogn)
# 实现方法是一种比较取巧的办法，就是数每个数字出现的个数
def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


# 在计算排序中，如果元素的范围比较大(比如在1到1亿之间)，如何改造算法？
# 桶排序（Bucket Sort）,首先将元素分在不同的桶中，在对每个桶中的元素排序
# 桶排序的表现取决于数据的分布。也就是需要对不同数据排序时采取不同的分桶策略
# 平均情况时间复杂度: O(n + k)
# 最坏情况时间复杂度：O(n^2k)
# 空间复杂度: O(nk)
# 直观理解, k表示一个桶平均能有多少个数
def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)] # 创建桶
    for var in li:
        i = min(var // (max_num // n), n-1) # i 表示var放到几号桶里
        buckets[i].append(var) # 把var加到桶里边
        # 保持桶内的顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    li.clear()
    for buc in buckets:
        li.extend(buc)
    return li


# 基数排序
# 对关键字排序：假如现在有一个员工表，要求按照薪资排序，年龄相同的员工按照年龄排序
# 先按照年龄进行排序，再按照薪资进行稳定的排序
# 对32,13,94,52,17,54,93排序，可以看做多关键字排序
# 先按照个位数排序，再按照十位数分桶，最后挨个输出
# 时间复杂度：O(kn)
# 空间复杂度：O(k+n)
# k表示数字位数
# 快排的时间复杂度是O(nlogn),所以基数排序比快速排序快
# 从数学也好理解, 快速排序：logn是以2为底的对数，基数排序：log10以10为底数
# 但是也有反例：[random.randint(0,10000000000) for _ in range(1000)]
# 基数排序的效率，和数字的个数有关
def radix_sort(li):
    max_num = max(li) # 最大值 9->1, 99->2, 888->3, 10000->5
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            # 987 
            # it=1 987//10 -> 98  98%10->8
            # it=2 987//100 -> 9 9%10 -> 9
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 把数重新写回li
        it += 1


if __name__ == "__main__":
    # li = [5,7,4,6,3,1,2,9,8]
    # li = [random.randint(0,1000) for i in range(1000)]

    li = list(range(100))
    random.shuffle(li)

    li1 = copy.deepcopy(li)
    li2 = copy.deepcopy(li)
    li3 = copy.deepcopy(li)
    li4 = copy.deepcopy(li)
    li5 = copy.deepcopy(li)
    li6 = copy.deepcopy(li)
    li7 = copy.deepcopy(li)
    li8 = copy.deepcopy(li)

    li_limit1 = [random.randint(0,10) for _ in range(100)]
    li_limit2 = [random.randint(0,10) for _ in range(100)]

    # 冒泡排序
    print("冒泡排序")
    bubble_sort(li1)
    print(li1)

    # 选择排序
    print("选择排序")
    select_sort(li2)
    print(li2)

    # 插入排序
    print("插入排序")
    insert_sort(li3)
    print(li3)

    # 快速排序
    print("快速排序")
    quick_sort(li4,0,len(li4)-1)
    print(li4)

    # 堆排序
    print("堆排序")
    heap_sort(li5)
    print(li5)

    # 归并排序
    print("归并排序")
    merge_sort(li6, 0, len(li6)-1)
    print(li6)

    # 希尔排序
    print("希尔排序")
    shell_sort(li7)
    print(li7)

    # 计数排序
    print("计数排序")
    count_sort(li_limit1)
    print(li_limit1)

    # 桶排序
    print("桶排序")
    bucket_sort(li_limit2, n=2, max_num=10)
    print(li_limit2)

    # 基数排序
    print("基数排序")
    radix_sort(li8)
    print(li8)