# -*- coding: utf-8 -*-
__author__ = 'PCPC'


# 以A[b-1]分割成左小，右大
def partition(A, a, b):
    key = A[b - 1]
    i = a  # i 是分割点
    for j in range(a, b):
        if A[j] < key:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[b - 1], A[i] = A[i], A[b - 1]
    return i


# 左闭右开
def qsort(A, a, b):
    if a >= b:
        return

    i = partition(A, a, b)
    qsort(A, a, i)
    qsort(A, i + 1, b)


li = [5, 6, 3, 7, 45, 1, 4, 8, 9, 2]
qsort(li, 0, len(li))
print(li)
