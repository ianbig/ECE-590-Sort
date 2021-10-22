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
MergeSort
"""
def MergeSort(listToSort):
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
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
