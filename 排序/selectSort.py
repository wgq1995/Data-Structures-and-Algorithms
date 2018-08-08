import numpy as np
def selectSort(seq):
    "选择排序"
    n = len(seq)
    print("待排序列表")
    print(seq)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
    print("排序后列表")
    print(seq)
    return seq
a = np.random.randint(10, size = 10)
a = selectSort(a)

