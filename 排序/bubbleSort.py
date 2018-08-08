import numpy as np
def bubbleSort(seq):
    "冒泡排序"
    n = len(seq)
    print("待排序列表")
    print(seq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]

    print("冒泡排序后列表")
    print(seq)
    return seq

a = np.random.randint(10, size = 10)
b = bubbleSort(a)
