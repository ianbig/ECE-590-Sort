"""
 Math 560
Project 1
Fall 2021

Partner 1:
Partner 2:
Date:
"""
"""
our own function
"""
def swap(listToSort, left, right):
    tmp = listToSort[left]
    listToSort[left] = listToSort[right]
    listToSort[right] = tmp
    return listToSort
"""
SelectionSort
"""
def SelectionSort(listToSort):
    for i in range(len(listToSort)):
        minIndex = i
        for j in range(i,len(listToSort)):
            if  listToSort[j] < listToSort[minIndex]:
                minIndex = j
        swap(listToSort, i, minIndex)
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    for sortedIndex in range(len(listToSort)):
        if sortedIndex + 1 < len(listToSort):
            while (listToSort[sortedIndex + 1] < listToSort[sortedIndex]) and sortedIndex >= 0:
                swap(listToSort, sortedIndex + 1,sortedIndex)
                sortedIndex -= 1
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    gotBubble = True
    while(gotBubble):
        bubbleNum = 0
        for i in range(len(listToSort)):
            if (i + 1 < len(listToSort)) and listToSort[i + 1] < listToSort[i]:
                swap(listToSort, i, i + 1)
                bubbleNum += 1
        if bubbleNum == 0:
            gotBubble = False
    return listToSort

"""
Merge

usage:
return:
"""

def Merge(left, right):
    li = 0
    ri = 0
    retList = []

    # print(left)
    # print(right)

    while (li < len(left) and ri < len(right)):
        if (left[li] < right[ri]):
            retList.append(left[li])
            li += 1
            pass
        else:
            retList.append(right[ri])
            ri += 1
            pass
        pass

    while (li < len(left)):
        retList.append(left[li])
        li += 1
        pass
        
    while (ri < len(right)):
        retList.append(right[ri])
        ri += 1
        pass
    
    # print('Merged: ' + str(retList))
    return retList

"""
MergeSort
"""
def MergeSort_help(listToSort):
    # import pdb; pdb.set_trace()
    if (len(listToSort) == 1):
        # print(listToSort)
        return listToSort
    
    mid = len(listToSort) // 2
    left = listToSort[:mid]
    right = listToSort[mid:]
    
    left = MergeSort_help(left)
    right = MergeSort_help(right)
    retList = Merge(left, right)
    
    return retList

import copy
def MergeSort(listToSort):
    # import pdb; pdb.set_trace()
    listToSort[:]  = MergeSort_help(listToSort)
    return listToSort

"""
partition

usage: divide number lower than pivot to left side, and otherwise to right side of pivot
return: retutn pivot location
"""

def partition(listToSort, left, right):
    low = left - 1
    right -= 1
    pivot = listToSort[right]
    for cur in range(left, right):
        if (listToSort[cur] < pivot):
            low += 1
            swap(listToSort, low, cur)
            pass
        pass
    swap(listToSort, low + 1, right)
    return low + 1

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    # import pdb; pdb.set_trace()
    # print('i: ' + str(i) + 'j:' + str(j))
    # print(listToSort)
    if j == None:
        j = len(listToSort)
        pass
    if (i >= j):
        return
    
    pivot = partition(listToSort, i, j)
    QuickSort(listToSort, i, pivot)
    QuickSort(listToSort, pivot + 1, j)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
