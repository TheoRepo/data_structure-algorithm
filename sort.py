import random
import copy

# 冒泡排序
# 算法复杂度O(n^2)
def bubble_sort(li):
    for i in range(len(li)-1): # 第i趟
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j] , li[j+1] = li[j+1], li[j]


# 选择排序
# 算法复杂度O(n^2)
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
def insert_sort(li):
    for i in range(1, len(li)):# i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1 #j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:# 手里的牌的顺序是从右往左，从大到小递减
            li[j+1] =  li[j] # 手里的牌往右挪个位置
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
        print(li,'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left] # 把左边的值写道右边空位上
        print(li,'left')
    li[left] = tmp # 把tmp归位
    return left

def quick_sort(li,left, right):
    if left < right: # 至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li,mid+1, right)


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
def sift(heap, low ,high):
    # hight是堆的最后一个元素的下标，low是第一个元素
    i = low # i开始时父亲节点
    j = 2*i + 1 # j开始是左孩子
    tmp = li[low] # 把堆顶存起来
    while j <= high: # 只要j位置有节点
        if j + 1 <= high and li[j + 1] > li[j]: # 如果右孩子有，并且比较大
            j = j + 1 # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j # 往下看一层
            j = 2 * i + 1
        else: # tmp更大，把tmp放到i的位置上
            # li[i] = tmp # 把tmp放到某一级领导的位置 # 重复代码，注释掉
            break
    else: # j位置没有节点，跳出循环
        li[i] = tmp


# 堆排序的实现
def heap_sort(li):
    # 构造堆
    n = len(li)
    for i in range((n-2)//2, -1 , -1): # -1表示倒叙，步长是-1
        # i表示建堆的时候调整的部分的根的下标
        sift(li, i, n-1)
    # 建堆完成了（农村包围城市）
    for i in range(n-1, -1, -1): 
        # i指向当前堆的最后一个元素
        li[0], li[i] = li[i],li[0]
        sift(li, 0, i-1) # i-1是新的high

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
def sift(li, low, high): # 建立小根堆的sift函数
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
        sift(heap, i, k-1)
    # 1.取列表的前k个元素建堆
    for i in range(k, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    # 2.遍历列表的后k+1个元素，如果比堆顶大，就和堆顶元素替换
    for i in range(k-1, -1 ,-1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
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
def merge_sort(li, low, high):
    if low < high: # 至少有两个元素，递归
        mid = (low + high) // 2
        merge_sort(li, low ,mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid ,high)

if __name__ == "__main__":
    li = list(range(1000))
    random.shuffle(li)
    # li = [5,7,4,6,3,1,2,9,8]
    # li = [random.randint(0,1000) for i in range(1000)]
    # print(li)
    # li_copy = copy.deepcopy(li)
    # print(li_copy)
    # 冒泡排序
    # bubble_sort(li)
    # 选择排序
    # select_sort(li_copy)
    # 快速排序
    # quick_sort(li,0,len(li)-1)
    # 堆排序例子
    # heap_sort(li)
    # print(li)
    # python内置的堆排列
    # heapq_example()
    # topk问题
    # print(topk(li,10))
    merge_sort(li, 0, len(li)-1)
    print(li)
