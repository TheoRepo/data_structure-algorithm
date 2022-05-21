# _*_coding:utf-8_*_
# created by Theo Yu on 5/16/22

# 汉诺塔问题
# 解题思路：
# n个盘子时（最小重复迭代单元）

# 把n-1个圆盘从A经过C移动到B
# 把第n个圆盘从A移动到C
# 把n-1个小圆盘从B经过A移动到C
def hanoi(n,a,b,c):
	if n>0:
		hanoi(n-1,a,c,b)
		print("moving from %s to %s" % (a,c))
		hanoi(n-1,b,a,c)
hanoi(3, 'A','B','C')

# 汉诺塔移动次数的递推公式：h(x)= 2h(x-1)+1
# h(64)=18446744073709551615
# 假设每秒钟搬一个盘子，则总共需要5800亿年