import random
import copy

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


if __name__ == "__main__":
    li = [random.randint(0, 10000) for i in range(1000)]
    li_copy = copy.deepcopy(li)
    bubble_sort(li)
    select_sort(li_copy)
    # print(li)
    # print(li_copy)
    assert li == li_copy