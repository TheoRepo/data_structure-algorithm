import random
import copy

# 冒泡排序
# 算法复杂度O(n^2)
def bubble_sort(li):
    for i in range(len(li)-1): # 第i趟
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j] , li[j+1] = li[j+1], li[j]


def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


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
        # print(li,'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left] # 把左边的值写道右边空位上
        # print(li,'left')
    li[left] = tmp # 把tmp归位
    return left

def quick_sort(li,left, right):
    if left < right: # 至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li,mid+1, right)


if __name__ == "__main__":
    # li = [random.randint(0, 10000) for i in range(1000)]
    # li_copy = copy.deepcopy(li)
    # bubble_sort(li)
    # select_sort(li_copy)
    # print(li)
    # print(li_copy)
    # assert li == li_copy
    li = [5,7,4,6,3,1,2,9,8]
    quick_sort(li,0,len(li)-1)
    print(li)