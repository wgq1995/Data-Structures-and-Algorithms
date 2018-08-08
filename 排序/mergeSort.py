import numpy as np

def mergeSort(seq, l, r):
    "归并排序"
    if r == l:
        return seq
    mid = int((r - l) / 2) + l
    mergeSort(seq, l, mid)
    mergeSort(seq, mid + 1, r)
    merge(seq, l, mid, r)

def merge(seq, l, mid, r):

    a, b = l, mid + 1
    new_sorted_seq = list()

    while a <= mid and b <= r:
        if seq[a] <= seq[b]:
            new_sorted_seq.append(seq[a])
            a += 1
        else:
            new_sorted_seq.append(seq[b])
            b += 1

    while a <= mid:
        new_sorted_seq.append(seq[a])
        a += 1

    while b <= r:
        new_sorted_seq.append(seq[b])
        b += 1
    for i in range(0, len(new_sorted_seq)):
        seq[l + i] = new_sorted_seq[i]

a = list(np.random.randint(100, size = 10))
print("待排序列表", a)
mergeSort(a, 0, 9)
print("排序完列表", a)
