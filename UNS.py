from flask import Flask, render_template, url_for
import random
import requests
import json
import time

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

    def inOrderList(self, currentNode, vecData, vecName):
        if (currentNode.left != None):
            self.inOrderList(currentNode.left, vecData, vecName)
        vecData.append(currentNode.data)
        vecName.append(currentNode.country)
        if (currentNode.right != None):
            self.inOrderList(currentNode.right, vecData, vecName)

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

app = Flask(__name__)

vecPovData = []
vecPovName = []
vecGenData = []
vecGenName = []

start = time.time()
povertyTree = AVLTree()
r = requests.get('http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=137506/year=2019')
povData = json.loads(r.text)
for goal in povData['indicator_value']:
    povertyTree.root = povertyTree.insertNode(povertyTree.root, povData['indicator_value'][goal]['137506']['2019'], povData['country_name'][goal])
povertyTree.inOrderList(povertyTree.root, vecPovData, vecPovName)
end = time.time()
avlTimePov = str(round(end - start, 4))

start = time.time()
genderTree = AVLTree()
r = requests.get('http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php/indicator_id=68606/year=2019')
genData = json.loads(r.text)
for goal in genData['indicator_value']:
    genderTree.root = genderTree.insertNode(genderTree.root, genData['indicator_value'][goal]['68606']['2019'], genData['country_name'][goal])
genderTree.inOrderList(genderTree.root, vecGenData, vecGenName)
end = time.time()
avlTimeGen = str(round(end - start, 4))

r = requests.get('https://unstats.un.org/SDGAPI/v1/sdg/Goal/List?includechildren=true')
dataGoals = json.loads(r.text)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/goals')
def goals():
    return render_template('goals.html', goalList=dataGoals)

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/milestones')
def milestones():
    return render_template('milestones.html')

@app.route('/statements')
def statements():
    return render_template('statements.html')

@app.route('/progress')
def progress():
    return render_template('progress.html', povData = vecPovData, povName = vecPovName, genData = vecGenData, genName = vecGenName, timerAVLPov = avlTimePov, timerAVLGen = avlTimeGen)

@app.route('/more-info')
def moreInfo():
    return render_template('more-info.html')