import numpy as np

#计数排序
def countingSort(seq, min, max):
    "计数排序,输入的seq范围在min~max间"
    couter = list(range(min, max + 1))
    n = len(seq)
    for i in range(0, n):
        couter[seq[i] - min] += 1
    newseq = []
    for j in range(0, max - min + 1):
        newseq += couter[j] * [j + min]
    print(newseq)
    return  newseq

a = np.random.randint(3, 6, size = 10)
mina = min(a)
maxa = max(a)
b = countingSort(a, mina, maxa)








