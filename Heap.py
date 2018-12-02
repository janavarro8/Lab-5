"""
Course: CS2302 Data Structures
Author: Javier Navarro
Assignment: Lab 4 Option B
Instructor: Diego Aguirre
TA: Manoj Saha
Last modified: 11/30/18
Purpose: Hold contents for a heap class
"""

class Heap:
    def __init__(self):
        self.heap_array = []

    #inserts k at appropriate index
    def insert(self, k):
        self.heap_array.append(k) #adds k to the list
        
        index = len(self.heap_array) - 1

        while index > 0:
            parentIndex = (index - 1) // 2
            
            #if child is greater than parent
            if (self.heap_array[index] >= self.heap_array[parentIndex]): 
                return
            else:
                self.swap(parentIndex, index)
            index = parentIndex
            
    #swaps positions of node1 and node2
    def swap(self, node1, node2):
        temp = self.heap_array[node1]
        self.heap_array[node1] = self.heap_array[node2]
        self.heap_array[node2] = temp

    #checks the min heap property 
    def heapify(self, size, index):
        parent = index
        
        left = index * 2 + 1
        right = index * 2 + 2

        #checks if child is larger than the parent
        if left < size and self.heap_array[index] > self.heap_array[left]:
            parent = left
            
        #checks if child is larger than the parent
        if right < size and self.heap_array[parent] > self.heap_array[right]:
            parent = right

        #swaps if parent isn't root
        if parent != index:
            self.swap(index, parent)
            self.heapify(size, parent)

    #sorts the heap in descending order
    def heap_sort(self):
        if self.is_empty():
            return
        
        for i in range(len(self.heap_array) - 1, 0, -1):
            self.swap(0, i)
            self.heapify(i, 0)

    #removes and returns min
    def extract_min(self):
        if self.is_empty():
            return None
        
        min_elem = self.heap_array.pop(0)

        return min_elem

    #checks if the heap is empty
    def is_empty(self):
        return len(self.heap_array) == 0

    #prints all elements in the heap
    def printHeap(self):
        print(self.heap_array)