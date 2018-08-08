import numpy as np
import random

def partition(seq, l, r):
    change_index = random.randint(l, r)
    seq[change_index], seq[r] = seq[r], seq[change_index]
    num = seq[r]
    less_index = l - 1
    more_index = r + 1
    p = l
    while more_index > p:
        if seq[p] < num:
            less_index += 1
            seq[p], seq[less_index] = seq[less_index], seq[p]
            p += 1
        elif seq[p] == num:
            p += 1
        else:
            more_index -= 1
            seq[p], seq[more_index] = seq[more_index], seq[p]

    p = [less_index + 1, more_index - 1]
    return p


def quickSort(seq, l, r):
    if r - l < 1:
        return seq
    else:
        p = partition(seq, l, r)
        quickSort(seq, l, p[0] - 1)
        quickSort(seq, p[1] + 1, r)




a = np.random.randint(20, size = 10)
n = len(a)
print(a)
quickSort(a, 0, n - 1)
print(a)
