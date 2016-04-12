# -*- coding:utf-8 -*-
__author__ = 'haven'


def heapsort(A):
    def heapify(A, start, end):
        l = start * 2+1
        r = l + 1
        largest = start
        if l < end and A[l] > A[largest]:
            largest = l
        if r < end and A[r] > A[largest]:
            largest = r
        if largest != start:
            A[start], A[largest] = A[largest], A[start]
            heapify(A, largest, end)

    def bulidheap(A):
        for i in range(len(A) // 2)[::-1]:
            heapify(A, i, len(A))

    bulidheap(A)
    for i in range(len(A))[::-1]:
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)

li = [1, 9, 2, 3, 6, 5, 7, 4, 8, 0]
heapsort(li)
print(li)
