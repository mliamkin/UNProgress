from flask import Flask, render_template, url_for, request
from random import seed, random,randint
import requests
import json
import time
import sys
import os

#I also was aided by YouTube videos from Brian Faure
class Node: #Here is the Node class, this is temporary until we get the Country nodes
    def __init__(self, _data, _country):
        self.data = _data #Holds the data that will be sorted by
        self.country = _country
        self.left = None #Holds the left child
        self.right = None #Holds the right child
        self.height = 1

class AVLTree:
    def __init__(self): #Default constructor, has a root node that is set to nothing
        self.root = None

    # This code is contributed by Ajitesh Pathak from GeekForGeeks
    def insertNode(self, root, data, country):
		
		# Step 1 - Perform normal BST
        if not root:
        	return Node(data, country)
        elif data < root.data:
        	root.left = self.insertNode(root.left, data, country)
        else:
        	root.right = self.insertNode(root.right, data, country)

		# Step 2 - Update the height of the
		# ancestor node
        root.height = 1 + max(self.getHeight(root.left),
        				self.getHeight(root.right))

		# Step 3 - Get the balance factor
        balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
        if balance > 1 and data < root.left.data:
        	return self.rightRotate(root)

		# Case 2 - Right Right
        if balance < -1 and data > root.right.data:
        	return self.leftRotate(root)

		# Case 3 - Left Right
        if balance > 1 and data > root.left.data:
        	root.left = self.leftRotate(root.left)
        	return self.rightRotate(root)

		# Case 4 - Right Left
        if balance < -1 and data < root.right.data:
        	root.right = self.rightRotate(root.right)
        	return self.leftRotate(root)

        return root

    def leftRotate(self, rotatedNode):
        nodeChild = rotatedNode.right
        tempNode = nodeChild.left

        nodeChild.left = rotatedNode
        rotatedNode.right = tempNode

        rotatedNode.height = 1 + max(self.getHeight(rotatedNode.left), self.getHeight(rotatedNode.right))
        nodeChild.height = 1 + max(self.getHeight(nodeChild.left), self.getHeight(nodeChild.right))

        return nodeChild
    
    def rightRotate(self, rotatedNode):
        nodeChild = rotatedNode.left
        tempNode = nodeChild.right

        nodeChild.right = rotatedNode
        rotatedNode.left = tempNode

        rotatedNode.height = 1 + max(self.getHeight(rotatedNode.left), self.getHeight(rotatedNode.right))
        nodeChild.height = 1 + max(self.getHeight(nodeChild.left), self.getHeight(nodeChild.right))

        return nodeChild
    
    def getHeight(self, currentNode):
        if not currentNode:
            return 0
        return currentNode.height
    
    def getBalance(self, currentNode):
        if not currentNode:
            return 0
        return self.getHeight(currentNode.left) - self.getHeight(currentNode.right)



    def heightOfTree(self): #The public height function for the tree, will return the height of the current tree obj
        if self.root != None: #If the root exists, go into the private version of this function
            return self._heightOfTree(self.root, 0) 
        else: #Otherwise return 0 since if there is no root then there is no tree, and there is a height of 0
            return 0

    def _heightOfTree(self, currentNode, currentHeight): #Private height function
        if currentNode == None: #If the currentNode does not exist return the currentHeight
            return currentHeight
        leftSideHeight = self._heightOfTree(currentNode.left, currentHeight + 1) #Will recursively go down the left side of the tree and return the height of the left side
        rightSideHeight = self._heightOfTree(currentNode.right, currentHeight + 1) #Will recursively go down the right side of the tree and return its' height
        return max(leftSideHeight, rightSideHeight) #Return the maximum height of either side, that is the height of the tree


    def printInorder(self): #Function to print the tree through Inorder Traversal, which is the best way since it will print from the least value to greatest value node
        if self.root != None: #If the root exists then continue
            self._printInorder(self.root)

    def _printInorder(self, currentNode): #This is the private function of the printInorder function, that way nothing can change it outside of the class
        if currentNode != None: #If the currentNode exists
            self._printInorder(currentNode.left) #Traverse down the Left side until it reaches a node that does not exist
            print((str(currentNode.country))) #This will print that node's data and height
            self._printInorder(currentNode.right) #This will then take care of the right side of the tree

    def inOrderList(self, currentNode, names, data):
        if (currentNode.left != None):
            self.inOrderList(currentNode.left, names, data)
        names.append(currentNode.country)
        data.append(currentNode.data)
        if (currentNode.right != None):
            self.inOrderList(currentNode.right, names, data)

    def searchTree(self, data): #Public version of the search function, return true or false when asked about a data number
        if self.root != None: #If the root exists then continue onto the private version
            return self._searchTree(data, self.root)
        else: #Otherwise return false since no root means no tree and no tree means no nodes anywhere
            return False

    def _searchTree(self, data, currentNode): #Takes in the data that is trying to search for and the currentNode is the node that is currently being looked at
        if data == currentNode.data: #If the searched term is equal to the currentNode's data then return true
            return True
        elif data < currentNode.data and currentNode.left != None: #Else if the data is less than the currentNode's value and the currentNode has a left child, then recursively check left side
            return self._searchTree(data, currentNode.left)
        elif data > currentNode.data and currentNode.right != None: #Do the same thing if it is greater except on the right side of the tree
            return self._searchTree(data, currentNode.right)
        return False #If everything goes through and true is still not returned then return false since we know that it won't exist

    def minValueNode(self, startingNode): #Return the node with the minimum data value found in that tree, entire tree not always searched
        currentNode = startingNode
        while (currentNode.left != None): #Loop down to find the leftmost leaf
            currentNode = currentNode.left
        return currentNode


    def deleteNode(self, data): #Public Version of the deleteNode function, takes in the data that it wants to delete and returns the new root node
        if self.root == None: #If the root does not exist then return the root which has nothing
            return self.root
        if self.searchTree(data):
            #If there is a node with this value then go into the private version of the deleteNode function
            return self._deleteNode(data, self.root)
        
    
    def _deleteNode(self, data, currentNode): #Private Version
        if self.root == None: #Base Case
            return self.root
        if data < currentNode.data: #If the data to be deleted is less than the currentNode's data then it must be in the left tree
            currentNode.left = self._deleteNode(data, currentNode.left)
        elif data > currentNode.data: #If the data to be deleted is greater than the currentNode's data then it must be in the right tree
            currentNode.right = self._deleteNode(data, currentNode.right)
        else: #If the data is the same as the currentNode's data then this node needs to be deleted
            if currentNode.left == None: #If the node with only one child or no child
                tempNode = currentNode.right
                currentNode = None
                return tempNode
            elif currentNode.right == None:
                temp = currentNode.left
                currentNode = None
                return tempNode
            #Node with two children: Get the Inorder Successor (Smallest in the right subtree)
            temp = self.minValueNode(currentNode.right)
            #Copy the inorder successor's content to this node
            currentNode.data = temp.data
            #Delete the inorder successor
            currentNode.right = self._deleteNode(temp.data, currentNode.right)

        #If the tree has only 1 node return it
        if currentNode == None:
            return currentNode
        
        #update the height of the ancestor node
        currentNode.height = 1 + max(self.getHeight(currentNode.left), self.getHeight(currentNode.right))

        #Get the Balance Factor
        balanceFactor = self.getBalance(currentNode)

        #If node is unbalanced then balance it
        if balanceFactor > 1 and self.getBalance(currentNode.left) >= 0: #Left-Left Case
            return self.rightRotate(currentNode)
        if balanceFactor < -1 and self.getBalance(currentNode.right) <= 0: #Right-Right Case
            return self.leftRotate(currentNode)
        if balanceFactor > 1 and self.getBalance(currentNode.left) < 0: #Left-Right Case
            currentNode.left = self.leftRotate(currentNode.left)
            return self.rightRotate(currentNode)
        if balanceFactor < -1 and self.getBalance(currentNode.right) > 0: #Right-Left Case
            currentNode.right = self.rightRotate(currentNode.right)
            return self.leftRotate(currentNode)
        
        return currentNode

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
        return (index)//2

    #Returns left Child of node at an index
    def leftChild(self, index):
        return (2 * index)
    
    #Returns right Child of node at an index
    def rightChild(self, index):
        return (2 * index) + 1

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
            if (self.Heap[index] > self.Heap[self.leftChild(index)] or self.Heap[index] > self.Heap[self.rightChild(index)]):
                if self.Heap[self.rightChild(index)] > self.Heap[self.leftChild(index)]:
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

    def getHeapData(self):
        vectorFull = []
        vectorData = []
        vectorName = []
        for i in range(10):
            removeNode = self.Pop()
            vectorData.append(removeNode.data)
            vectorName.append(removeNode.nameOfCountry)
        vectorFull.append(vectorName)
        vectorFull.append(vectorData)
        return vectorFull

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
        return (index)//2

    #Returns left Child of node at an index
    def leftChild(self, index):
        return (2 * index)
    
    #Returns right Child of node at an index
    def rightChild(self, index):
        return (2 * index) + 1

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
            if (self.Heap[index] < self.Heap[self.leftChild(index)] or self.Heap[index] < self.Heap[self.rightChild(index)]):
                if self.Heap[self.rightChild(index)] < self.Heap[self.leftChild(index)]:
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
    
    def getHeapData(self):
        vectorFull = []
        vectorData = []
        vectorName = []
        for i in range(10):
            removeNode = self.Pop()
            vectorData.append(removeNode.data)
            vectorName.append(removeNode.nameOfCountry)
        vectorFull.append(vectorName)
        vectorFull.append(vectorData)
        return vectorFull

class specialCountryNode:
    def __init__ (self, nameOfCountry, data):
        self.nameOfCountry = nameOfCountry
        self.data = data

def specialCountryGenerator():
    seed(time.ctime())
    specialCountryList = []    
    
    for x in range(100000):
        
        specialCountryName = "Country " + str(x+1)
        
        pHolder = 0.0
        while(pHolder < .394 or pHolder > .957):
            pHolder = float( int(random() * 10000000) / 10000000)
                


        sC = specialCountryNode(specialCountryName, pHolder)
        specialCountryList.append(sC)

    return specialCountryList

app = Flask(__name__)

heapNames = []
heapData = []

treeNames = []
treeData = []

heapTimes = []
treeTimes = []

def getHeaps():
    #Poverty Data Heap
    povertyHeap = minHeap(195)

    #Conecting to API with URL and converting to JSON format for ease of use
    r = requests.get('http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=137506/year=2019')
    data = json.loads(r.text)
    start = time.time()
    for goal in data['indicator_value']:
        povertyHeap.insert(countryNode(data['country_name'][goal], data['indicator_value'][goal]['137506']['2019']))

    #Generate list of names and data to iterate through in HTML
    datas = povertyHeap.getHeapData()
    heapData.append(datas[1])
    heapNames.append(datas[0])
    end = time.time()

    #Time for process
    heapTimes.append(str(round(end - start, 6)))

    #Hunger Data Heap
    hungerHeap = maxHeap(195)

    #Conecting to API with file name and converting to JSON format for ease of use
    start = time.time()
    filename = os.path.join(app.static_folder, 'data', 'GlobalHunger2018.json')
    with open(filename) as test_file:
        hungerData = json.load(test_file)
    for goal in hungerData:
        hungerHeap.insert(countryNode(goal['Entity'], goal['Global Hunger Index (IFPRI (2016))']))
    
    #Generate list of names and data to iterate through in HTML
    datas = hungerHeap.getHeapData()
    heapData.append(datas[1])
    heapNames.append(datas[0])
    end = time.time()

    #Time for process
    heapTimes.append(str(round(end - start, 6)))

    #Expectancy Data Heap
    expHeap = minHeap(250)

    #Conecting to API with file name and converting to JSON format for ease of use
    start = time.time()
    filename = os.path.join(app.static_folder, 'data', 'LifeExpectancy2019.json')
    with open(filename) as test_file:
        expData = json.load(test_file)
    for goal in expData:
        expHeap.insert(countryNode(goal['Entity'], goal['Life expectancy']))

    #Generate list of names and data to iterate through in HTML
    datas = expHeap.getHeapData()
    heapData.append(datas[1])
    heapNames.append(datas[0])
    end = time.time()

    #Time for process
    heapTimes.append(str(round(end - start, 6)))

    #Female Literacy Heap
    fLitHeap = minHeap(180)

    #Conecting to API with file name and converting to JSON format for ease of use
    start = time.time()
    filename = os.path.join(app.static_folder, 'data', 'YouthLiteracyFemale2015.json')
    with open(filename) as test_file:
        fLitData = json.load(test_file)
    for goal in fLitData:
        fLitHeap.insert(countryNode(goal['Entity'], goal['Youth literacy rate, population 15-24 years, female (%)']))

    #Generate list of names and data to iterate through in HTML
    datas = fLitHeap.getHeapData()
    heapData.append(datas[1])
    heapNames.append(datas[0])
    end = time.time()

    #Time for process
    heapTimes.append(str(round(end - start, 6)))

    #Gender Data Heap
    genderHeap = maxHeap(195)

    #Conecting to API with URL and converting to JSON format for ease of use
    r = requests.get('http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=68606/year=2019')
    genData = json.loads(r.text)
    start = time.time()
    for goal in genData['indicator_value']:
        genderHeap.insert(countryNode(genData['country_name'][goal], genData['indicator_value'][goal]['68606']['2019']))

    #Generate list of names and data to iterate through in HTML
    datas = genderHeap.getHeapData()
    heapData.append(datas[1])
    heapNames.append(datas[0])
    end = time.time()

    #Time for process
    heapTimes.append(str(round(end - start, 6)))

def getTrees():
    #Poverty Data AVL Tree
    povertyTree = AVLTree()

    #Conecting to API with URL and converting to JSON format for ease of use
    r = requests.get('http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=137506/year=2019')
    data = json.loads(r.text)
    start = time.time()
    for goal in data['indicator_value']:
        povertyTree.root = povertyTree.insertNode(povertyTree.root, data['indicator_value'][goal]['137506']['2019'], data['country_name'][goal])

    #Generate list of names and data to iterate through in HTML
    names = []
    data = []
    povertyTree.inOrderList(povertyTree.root, names, data)
    treeNames.append(names)
    treeData.append(data)
    end = time.time()

    #Time for process
    treeTimes.append(str(round(end - start, 6)))

    #Hunger Data AVL Tree
    start = time.time()
    hungerTree = AVLTree()

    #Conecting to API with file name and converting to JSON format for ease of use
    filename = os.path.join(app.static_folder, 'data', 'GlobalHunger2018.json')
    with open(filename) as test_file:
        hungerData = json.load(test_file)
    for goal in hungerData:
        hungerTree.root = hungerTree.insertNode(hungerTree.root, goal['Global Hunger Index (IFPRI (2016))'], goal['Entity'])

    #Generate list of names and data to iterate through in HTML
    names = []
    data = []
    hungerTree.inOrderList(hungerTree.root, names, data)
    treeNames.append(names)
    treeData.append(data)
    end = time.time()

    #Time for process
    treeTimes.append(str(round(end - start, 6)))

    #Life expectancy Data AVL Tree
    start = time.time()
    expTree = AVLTree()

    #Conecting to API with file name and converting to JSON format for ease of use
    filename = os.path.join(app.static_folder, 'data', 'LifeExpectancy2019.json')
    with open(filename) as test_file:
        expData = json.load(test_file)
    for goal in expData:
        expTree.root = expTree.insertNode(expTree.root, goal['Life expectancy'], goal['Entity'])

    #Generate list of names and data to iterate through in HTML
    names = []
    data = []
    expTree.inOrderList(expTree.root, names, data)
    treeNames.append(names)
    treeData.append(data)
    end = time.time()

    #Time for process
    treeTimes.append(str(round(end - start, 6)))

    #Life expectancy Data AVL Tree
    start = time.time()
    litTree = AVLTree()

    #Conecting to API with file name and converting to JSON format for ease of use
    filename = os.path.join(app.static_folder, 'data', 'YouthLiteracyFemale2015.json')
    with open(filename) as test_file:
        litData = json.load(test_file)
    for goal in litData:
        litTree.root = litTree.insertNode(litTree.root, goal['Youth literacy rate, population 15-24 years, female (%)'], goal['Entity'])

    #Generate list of names and data to iterate through in HTML
    names = []
    data = []
    litTree.inOrderList(litTree.root, names, data)
    treeNames.append(names)
    treeData.append(data)
    end = time.time()

    #Time for process
    treeTimes.append(str(round(end - start, 6)))

    #Gender Data AVL Tree
    genderTree = AVLTree()

    #Conecting to API with URL and converting to JSON format for ease of use
    r = requests.get('http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=68606/year=2019')
    genData = json.loads(r.text)
    start = time.time()
    for goal in genData['indicator_value']:
        genderTree.root = genderTree.insertNode(genderTree.root, genData['indicator_value'][goal]['68606']['2019'], genData['country_name'][goal])

    #Generate list of names and data to iterate through in HTML
    names = []
    data = []
    genderTree.inOrderList(genderTree.root, names, data)
    treeNames.append(names)
    treeData.append(data)
    end = time.time()

    #Time for process
    treeTimes.append(str(round(end - start, 6)))

def specialStructures():
    fullList = []
    timeList = []

    countries = specialCountryGenerator()

    start = time.time()
    specialTree = AVLTree()

    for c in countries:
        specialTree.root = specialTree.insertNode(specialTree.root, c.data, c.nameOfCountry)

    names = []
    data = []
    specialTree.inOrderList(specialTree.root, names, data)

    end = time.time()

    timeList.append(str(round(end - start, 6)))

    start = time.time()
    specHeap = minHeap(100000)

    for c in countries:
        specHeap.insert(countryNode(c.nameOfCountry, c.data))

    datas = specHeap.getHeapData()
    end = time.time()

    timeList.append(str(round(end - start, 6)))
    fullList.append(timeList)

    fullList.append(names)
    fullList.append(data)

    fullList.append(datas[0])
    fullList.append(datas[1])

    return fullList

def specialStructuresSearch():
    fullList = []

    countries = specialCountryGenerator()

    specialTree = AVLTree()
    specHeap = minHeap(100000)
    for c in countries:
        specialTree.root = specialTree.insertNode(specialTree.root, c.data, c.nameOfCountry)
        specHeap.insert(countryNode(c.nameOfCountry, c.data))

    start = time.time()

    country = specHeap.Pop()
    while (specHeap.size > 0):
        country = specHeap.Pop()

    fullList.append(country)
    end = time.time()

    fullList.append(str(round(end - start, 10)))

    start = time.time()
    if (specialTree.searchTree(country.data)):
        end = time.time()

    fullList.append(str(end - start))

    return fullList




r = requests.get('https://unstats.un.org/SDGAPI/v1/sdg/Goal/List?includechildren=true')
dataGoals = json.loads(r.text)

if __name__ == "__main__":
    listOfSpecialCountries = specialCountryGenerator()
    print(len(listOfSpecialCountries))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/goals')
def goals():
    return render_template('goals.html', goalList=dataGoals)

@app.route('/documents', methods=['GET', 'POST'])
def documents():
    tag = "None"
    if (request.method == 'POST'):
        tag = request.form['tag']
    return render_template('documents.html', tag = tag)

@app.route('/milestones')
def milestones():
    return render_template('milestones.html')

@app.route('/statements')
def statements():
    timeList = []
    timeList = specialStructures()
    return render_template('statements.html', 
        treeData = timeList[2], treeName = timeList[1],
        heapData = timeList[4], heapName = timeList[3],
        treeTime = timeList[0][0],
        heapTime = timeList[0][1]
        )

@app.route('/progress')
def progress():
    getHeaps()
    getTrees()
    return render_template('progress.html', 
        heapTimes = heapTimes,
        treeTimes = treeTimes,
        heapData = heapData,
        heapNames = heapNames,
        treeData = treeData,
        treeNames = treeNames
        )

@app.route('/more-info')
def moreInfo():
    fullList = specialStructuresSearch()
    return render_template('more-info.html',
        country = fullList[0].nameOfCountry,
        treeTime = fullList[1],
        heapTime = fullList[2]
    )