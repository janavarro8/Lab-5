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

        #swaps if larger value found
        if parent != index:
            self.swap(index, parent)
            self.heapify(size, parent)

    #sorts the heap in descending order
    def heap_sort(self):
        size = len(self.heap_array)
        
        temp = []   #holds item at root every time it's removed

        for i in range(size):
            temp.append(self.heap_array[0])
            self.swap(0, len(self.heap_array) - 1)
            self.heap_array = self.heap_array[:len(self.heap_array) - 1]
            self.heapify(len(self.heap_array) - 1, 0)

        self.heap_array = temp

    
    #removes and returns min
    def extract_min(self):
        if self.isEmpty():
            return None
        
        heapMin = self.heap_array[0]
        lastIndex = len(self.heap_array)-1
        
        self.swap(0, lastIndex) #the root is now swapped and heapified
        self.heapArr = self.heap_array[:lastIndex]
        self.heapify(lastIndex,0)

        return heapMin

    #checks if the heap is empty
    def isEmpty(self):
        return len(self.heap_array) == 0

    #prints all elements in the heap
    def printHeap(self):
        print(self.heap_array)