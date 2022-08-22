#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   hash_table.py
#@Time    :   2022/06/23 08:23:41
#@Author  :   Theo Yu


# 哈希表是一个通过哈希函数来计算数据存储位置的数据结构，通常支持如下操作:
# insert(key,value): 插入键值对(key, value)
# get(key): 如果存在键为key的键值对则返回其value, 否则返回空值
# delete(key): 删除键为key的键值对

# 直接寻址表
# 当关键字的全域U比较小时，直接寻址是一种简单而有效的方法
# 直接寻址技术特点
# 当域U很大时，需要消耗大量内存，很不实际
# 如果域U很大而实际出现的key很少，则大量空间被浪费
# 无法处理关键字不是数字的情况

# 哈希
# 直接寻址表: key为k的元素放到k位置上
# 改进直接寻址表: 哈希(hashing)
# 构建大小为m的寻址表T
# key为k的元素放到h(k)位置上
# h(k)是一个函数，其将域U映射到表T[0,1,...,m-1]

# 哈希表
# 哈希表(Hash Table, 又称为散列表), 是一种线性表的存储结构。哈希表由一个直接寻址表和一个哈希函数组成。
# 哈希函数h(k)将元素关键字k作为自变量, 返回元素的存储下标
# 例子: 假设有一个长度为7的哈希表, 哈希函数h(k)=k%7。元素集合{14, 22, 3, 5}的存储方式

# 哈希冲突 
# 由于哈希表的大小是有限的, 而要存储的值的总数量是无限的, 因此对于任何哈希函数, 都会出现
# 两个不同元素映射到同一个位置上的情况，这种情况叫做哈希冲突。
# 例子: h(k)=k%7, h(0)=h(7)=h(14)=...

# 解决哈希冲突——开放寻址法
# 开放寻址法：如果哈希函数返回的位置已经有值, 则可以向后探查新的位置来存储这个值
# 线性探查: 如果位置i被占用, 则探查i+1, i+2,...
# 二次探查: 如果位置i被占用, 则探查i+1^2, i-1^2, i+2^2, i-2^2,...
# 二度哈希: 有n个哈希函数, 当使用第1个哈希函数h1发生冲突时, 则尝试使用h2, h3,...

# 解决哈希冲突——拉链法
# 拉链法: 哈希表每个位置都连接一个链表, 当冲突发生时, 冲突的元素将被加到该位置链表的最后。

# 常见的哈希函数
# 除法哈希法：
# h(k)= k % m
# 乘法哈希法:
# h(k)= floor(m*(A*key%1))
# 全域哈希法
# h_(a,b)(k)= ((a*key+b) mod p) mod m  a,b= 1,2,...,p-1

# 哈希的应用
# python的字典与集合都是通过哈希表来实现的。
# a = {'name':'Alex', 'age':18, 'gender':'Man'}
# 使用哈希表存储字典，通过哈希函数将字典的键映射为下标。

# 中文怎么映射成数字？
# 中文实质就是二进制字符串，当然可以转化十进制的
# 假设h('name')=3, h('age')=1, h('gender')=4, 
# 则哈希表存储为[None,18,None,'Alex','Man']

# 如果发生哈希冲突，则通过拉链法或开发寻址发解决

# RSA加密算法是一种非对称加密算法（可以加密，也可以解密）
# RSA是由罗纳德·李维斯特（Ron Rivest）、阿迪·萨莫尔（Adi Shamir）和伦纳德·阿德曼（Leonard Adleman）
# 在1977年一起提出的。当时他们三人都在麻省理工学院工作。
# RSA 就是他们三人姓氏开头字母拼在一起组成的。
# 对极大整数做因数分解的难度决定了 RSA 算法的可靠性。
# 换言之，对一极大整数做因数分解愈困难，RSA 算法愈可靠。
# 假如有人找到一种快速因数分解的算法的话，那么用 RSA 加密的信息的可靠性就会极度下降。
# 但找到这样的算法的可能性是非常小的。
# 今天只有短的 RSA 钥匙才可能被强力方式破解。
# 到2020年为止，世界上还没有任何可靠的攻击RSA算法的方式。
# 只要其钥匙的长度足够长，用RSA加密的信息实际上是不能被破解的

# MD5(Message-Digest Algorithm 5)曾经是密码学中常用的哈希函数（只有加密，没有解密）
# 可以把任意长度的数据映射为128位的哈希值，其曾经包含如下特征:
# 1. 同样的消息，其MD5值必定相同
# 2. 可以快速计算出任意给定消息的MD5值
# 3. 除非暴力的枚举所有可能的消息，否则不可能从哈希值反推出消息本身
# 4. 两条消息之间即使只有微小的差别，其对应的MD5值也应该是完全不同、完全不相关的
# 5. 不能在有意义的时间内人工的构造两个不同的消息，使其具有相同的MD5值
# （MD5本身也是一种哈希，只要有哈希，就一定存在哈希冲突，哪怕128位的数据已经很大了）

# MD5应用举例：文件的哈希值
# 算出文件的哈希值，若有两个文件的哈希值相同，则认为这两个文件是相同的，因此：
# 1. 用户可以利用它来验证下载的文件是否完整
# 2. 云存储服务商可以利用它来判断用户要上传的文件，是否已经存在与服务器上，从而实现秒传的功能
# 同时避免存储过多相同的文件副本
# 目前，MD5已经被破解了

# SHA2算法
# 历史上MD5和SHA-1曾经是使用最广泛的cryptographic hash function，但是随着密码学的发展
# 这两个哈希函数的安全性相继受到了各种挑战。
# 因此现在安全性较重要的场合推荐使用SHA-2等新的更安全的哈希函数
# SHA-2包含了一系列的哈希函数：SHA-224，SHA-256，SHA-384，SHA-512,SHA-512/224, SHA-512/256
# 其对应的哈希值长度分别为224，256，384，or 512位
# SHA-2具有和MD5类似的性质

# SHA2应用举例：
# 例如，在比特币系统中，所有参与者需要共同解决如下问题：
# 对于一个给定的字符串U，给定的目标哈希值H，需要计算一个字符串V，
# 使得U+V的哈希值与H的差小于一个给定值D
# 此时，只能通过暴力枚举V来进行猜测（因为哈希值是不能反解的），首先计算出结果的人可以获得一定奖金。
# 而某人首先计算成功的概率与其拥有的计算量成正比，
# 所以其获得的奖金的期望值与其拥有的计算量成正比


class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self
    
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)
        
    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<"+", ".join(map(str, self))+">>"


class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]

    def h(self, k):
        return k % self.size
    
    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert.")
        else:
            self.T[i].append(k)
    
    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)


if __name__=="__main__":
    # 测试链表
    lk = LinkList([1,2,3,4,5])
    for element in lk:
        print(element)
    print(lk)

    # 测试哈希表
    ht = HashTable()
    ht.insert(0)
    ht.insert(1)
    ht.insert(3)
    ht.insert(102)
    ht.insert(508)

    print(",".join(map(str, ht.T)))            