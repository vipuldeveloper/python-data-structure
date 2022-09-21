from xml.etree.ElementPath import prepare_parent


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Slist:
    def __init__(self):
        self.head = None
        
    def addNodeAtBegining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def addAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
    
    def addNthPosition(self, position, data):
        if(position == 0):
            self.addNodeAtBegining(data)
            return
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            currentPosition = 0
            while(currentPosition < position and current):
                prevNode = current
                current = current.next
                currentPosition += 1         
             
            if(currentPosition == position):    
                new_node.next = current
                prevNode.next = new_node
    
    def deleteNode(self, data):
        if(self.head is None):
            print("list is empty")
        else:
            isFound = False
            current = self.head
            privious = None
            while(current):
                if(current.data == data):
                    isFound = True
                    break
                previous = current
                current = current.next

            if(isFound):
                if current == self.head:
                    self.head = self.head.next
                else:
                    previous.next = current.next
                    print(str(data) + " is found and deleted")
            else:
                print(str(data) + " is not found")
                    
    def printNode(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

if __name__ == "__main__":
    slist = Slist()
    slist.addNodeAtBegining(10)
    slist.addNodeAtBegining(20)
    slist.addAtEnd(50)
    # slist.addNodeAtBegining(30)
    # slist.addNthPosition(1, 3)
    slist.deleteNode(50)
    slist.printNode()