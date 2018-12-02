"""
Course: CS2302 Data Structures
Author: Javier Navarro
Assignment: Lab 5 Option B
Instructor: Diego Aguirre
TA: Manoj Saha
Last modified: 11/28/18
Purpose: Implement a heap and use heap sort
"""

import Heap

def main():
    heap = Heap.Heap()
    validInput = False
    
    while(validInput == False):
        try:
            fileName = input("Enter file name:")
            fill_heap(fileName, heap)
            validInput = True
            
        except FileNotFoundError:
            print("File not found. Try again.")
    
    print("\nHeap before heapsort:")
    heap.printHeap()
    
    heap.heap_sort()
    
    print("\nHeap after heapsort:")
    heap.printHeap()
    
    
#receives a heap and fills it with the given fileName
def fill_heap(fileName, heap):
    with open(fileName, "r") as file:       #opens file with given fileName
        for line in file:
            line = line.split(",")
            for item in line:
                try:    #catch errors in the input file
                    if item != "":
                        heap.insert(int(item))
                except ValueError:
                    pass


main()
