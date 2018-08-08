import numpy as np
import math

def heapInsert(list, index):
    #index位置上的数是新加的,
    # 0~index - 1上已经是大根堆了，该函数实现0~index上重整为大根堆
    "向上寻找位置"
    while list[index] > list[int((index - 1) / 2)]:
        list[index], list[int((index - 1) / 2)] = list[int((index - 1) / 2)], list[index]
        index = int((index - 1) / 2)

def heapify(list, index, size):
    "list[index]上的数变小了，向下调整"
    l = index * 2 + 1
    #判断是否有左儿子
    while l < size:
        #判断是否存在右儿子，如果不存在，最大为左儿子
        r = l + 1
        if r >= size:
            large = l
        else:
            if list[l] >= list[r]:
                large = l
            else:
                large = r

        if list[index] >= list[large]:
            break
        list[index], list[large] = list[large], list[index]
        index = large
        l = index * 2 + 1

def quickHeapify(list):
    "用O（n）的时间复杂度将数组变为一个大根堆"
    size = len(list)
    k = int(math.log(size, 2))
    index = 2 ** k - 2
    for i in range(0, index + 1):
        heapify(list, index - i, size)

def heapSort(list):
    "堆排序"
    #首先将列表变成一个大根堆
    print("待排序列表:", list)
    n = len(list)
    quickHeapify(list)
    print("大根堆列表:", list)

    for i in range(0, n - 1):
        list[0], list[n - 1 - i], = list[n - 1 - i], list[0]
        heapify(list, 0, n - 1 - i)##
    print("排序后列表:", list)
    return list
aa = [4, 1, 3, 2, 5]
a = np.random.randint(100, size = 10)
heapSort(a)





