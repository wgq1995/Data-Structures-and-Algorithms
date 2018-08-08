import numpy as np

def insertSort(seq):
    "插入排序"
    n = len(seq)
    print("待排序列表")
    print(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value
    print("排序后列表")
    print(seq)
    return seq

a = np.random.randint(100, size = 10)
b = insertSort(a)


