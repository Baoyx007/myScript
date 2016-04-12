# -*- coding:utf-8 -*-
__author__ = 'haven'


def getKmax(A, k):
    def heapify(A, start, end):
        l = start * 2 + 1
        r = l + 1
        largest = start
        if l < end and A[l] > A[largest]:
            largest = l
        if r < end and A[r] > A[largest]:
            largest = r
        if largest != start:
            A[start], A[largest] = A[largest], A[start]
            heapify(A, largest, end)

    def bulidheap(A, l):
        for i in range(l // 2)[::-1]:
            heapify(A, i, l)

    # 建立K大小的堆
    bulidheap(A, k)
    for i in range(k, len(A)):
        if A[0]>A[i]:
            A[0],A[i]=A[i],A[0]
        heapify(A, 0, k)
    return A[:k]


li = list(range(1000))
print(getKmax(li, 10))
