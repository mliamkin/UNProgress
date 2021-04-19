import sys

#Node used for testing, contains name of country and a data value
#Handles less-than-comparison through comparing two data values
class countryNode:
    
    def __init__(self, nameOfCountry = "", data = 0):
        self.nameOfCountry = nameOfCountry
        self.data = data
    
    
    def __lt__(self, rms):          
        if(self.data < rms.data):
            return True
        else:
            return False  
          

#minHeap class and it's respective functions
class minHeap:
    
    #Constructor: Creates capacity of Heap, size of Heap, and Heap List
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = -1
        pHolder = countryNode()
        self.Heap = [pHolder] * (self.capacity)        
    
    #Returns the parent of node at an index
    def parent(self, index):
        return (index - 1)//2

    #Returns left Child of node at an index
    def leftChild(self, index):
        return (2 * index) + 1
    
    #Returns right Child of node at an index
    def rightChild(self, index):
        return (2 * index) + 2

    #Switches values of Heap between two indices: first_index and second_index
    def swap(self, first_index, second_index):
        self.Heap[first_index], self.Heap[second_index] = self.Heap[second_index], self.Heap[first_index]

    #Inserts a new Node - newCountry - into Heap unless size >= capacity
    #Swaps values in Heap until Heap is organized with country with minimum 
    # value on top
    def insert(self, newCountry):
        if(self.size >= self.capacity):
            return        
        self.size += 1
        self.Heap[self.size] = newCountry

        currIndex = self.size        

        while (self.Heap[currIndex] < self.Heap[self.parent(currIndex)] ):
            self.swap(currIndex, self.parent(currIndex))
            currIndex = self.parent(currIndex)  

    #Prints country name from lowest data value to highest data value
    #Can be adjusted to print the first 10 values by changing for loop to the one below
    # for i in range(0, 10)
    def Print(self):        
        for i in range (0, (self.size+1) ):            
            print(self.Heap[i].nameOfCountry)

    #Heapify Function Steps
    # Step 1: Check that node at index has children
    # Step 2: Check if node at index is a greater value than either left or right child
    # Step 3: If node at index is greater value than left child, 
    # Step 3a (cont.): Swap values then repeat Steps 1 & 2 with left Child index value    
    # Step 4: Swap values at index node and index's right child node
    # Step 4a (cont.): Repeat Steps 1 & 2 with right Child index value
    def heapify(self, index):
        if not (index >= self.size//2 and index <= self.size):
            if (self.Heap[index] > self.Heap[self.leftChild(index)] ) or (self.Heap[index] > self.Heap[self.rightChild(index)]):
                if self.Heap[index] > self.Heap[self.leftChild(index)]:
                    self.swap(index, self.leftChild(index) )
                    self.heapify(self.leftChild(index) )
                else:
                    self.swap(index, self.rightChild(index))
                    self.heapify(self.rightChild(index))
        
    #Removes and returns country with minimum value of Heap while 
    #reorganizing Heap accordingly
    #Note: Returns countryNode, not string. Therefore if desiring to print
    #Note (cont.): country name, call on nameOfCountry within print statement
    def Pop(self):
        pop = self.Heap[0]
        self.Heap[0] = self.Heap[self.size]
        self.size -= 1
        if self.size > 0:
            self.heapify(0)        
        return pop        

#maxHeap class and it's respective functions
class maxHeap:
    
    #Constructor: Creates capacity of Heap, size of Heap, and Heap List
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = -1
        pHolder = countryNode("", sys.maxsize)
        self.Heap = [pHolder] * (self.capacity)        
    
    #Returns the parent of node at an index
    def parent(self, index):
        return (index - 1)//2

    #Returns left Child of node at an index
    def leftChild(self, index):
        return (2 * index) + 1
    
    #Returns right Child of node at an index
    def rightChild(self, index):
        return (2 * index) + 2

    #Switches values of Heap between two indices: first_index and second_index
    def swap(self, first_index, second_index):
        self.Heap[first_index], self.Heap[second_index] = self.Heap[second_index], self.Heap[first_index]

    #Inserts a new Node - newCountry - into Heap unless size >= capacity
    #Swaps values in Heap until Heap is organized with maximum value on top
    def insert(self, newCountry):
        if(self.size >= self.capacity):
            return        
        self.size += 1
        self.Heap[self.size] = newCountry

        currIndex = self.size        

        while (self.Heap[currIndex] > self.Heap[self.parent(currIndex)] ):
            self.swap(currIndex, self.parent(currIndex))
            currIndex = self.parent(currIndex)  

    #Prints country names from highest data value to lowest data value
    #Can be adjusted to print the first 10 values by changing for loop to the one below
    # for i in range(0, 10)
    def Print(self):        
        for i in range (0, (self.size+1) ):            
            print(self.Heap[i].nameOfCountry)

    #Heapify Function Steps
    # Step 1: Check that node at index has children
    # Step 2: Check if node at index is a lesser value than either left or right child
    # Step 3: If node at index is greater value than left child, 
    # Step 3a (cont.): Swap values then repeat Steps 1 & 2 with left Child index value    
    # Step 4: Swap values at index node and index's right child node
    # Step 4a (cont.): Repeat Steps 1 & 2 with right Child index value
    def heapify(self, index):
        if not (index >= self.size//2 and index <= self.size):
            if (self.Heap[index] < self.Heap[self.leftChild(index)] ) or (self.Heap[index] < self.Heap[self.rightChild(index)]):
                if self.Heap[index] > self.Heap[self.leftChild(index)]:
                    self.swap(index, self.leftChild(index) )
                    self.heapify(self.leftChild(index) )
                else:
                    self.swap(index, self.rightChild(index))
                    self.heapify(self.rightChild(index))

    #Removes and returns country with maximum value of Heap 
    #while reorganizing Heap accordingly
    #Note: Returns countryNode, not string. Therefore if desiring to print
    #Note (cont.): country name, call on nameOfCountry within print statement
    def Pop(self):
        pop = self.Heap[0]
        self.Heap[0] = self.Heap[self.size]
        self.size -= 1
        if self.size > 0:            
            self.heapify(0)        
        return pop   
    

#main function to test countryNode, minHeap, and maxHeap functions
if __name__ == "__main__":
    
    minHeap = minHeap(15)
    maxHeap = maxHeap(15)

    c1 = countryNode("Angola", 6)
    c2 = countryNode("Bahamas", 3)
    c3 = countryNode("Puerto Rico",1)

    maxHeap.insert(c1)
    maxHeap.insert(c2)
    maxHeap.insert(c3)
    print(maxHeap.Pop().nameOfCountry)
    print(maxHeap.Pop().nameOfCountry)
    print(maxHeap.Pop().nameOfCountry)
    maxHeap.Print()
    
    #minHeap.insert(3)
    #minHeap.insert(5)
    #minHeap.insert(10)
    #minHeap.insert(11)
    #minHeap.insert(12)
    #minHeap.insert(15)
    #maxHeap.insert(4)
    #maxHeap.insert(2)
    #maxHeap.insert(3)
    #print(minHeap.Pop())
    #print()
    #minHeap.Print()
    
