from xml.etree.ElementPath import prepare_parent


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Slist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addNodeAtBegining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            new_node.next = self.tail
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            
    def addAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.addNodeAtBegining(data)
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
    
    def addNthPosition(self, position, data):        
        if (position == 0):
            self.addNodeAtBegining(data)
            return
        
        new_node = Node(data)
        current_position = 0
        current = self.head
        previous = None
        while(current_position < position and current):
            previous = current
            current = current.next
            current_position += 1
        
        new_node.next = current
        previous.next = new_node
        
    def deleteNode(self, data):
        if self.head is None:
            print("List is empty")
        else:
            current =  self.head
            previous = None
            isFound = False
            while(current and current.next != self.head):
                if(current.data == data):
                    isFound = True
                    break
                
                previous = current
                current = current.next

            if(current.data == data):
                isFound = True
                
            if(isFound):
                if current is self.head:
                   self.head = self.head.next
                else:
                    previous.next = current.next
                    print(str(data)+" is deleted")
            else:
                print(str(data)+" is not found, so cannt delete")
                    
    def printNode(self):
        current = self.head
        while(current and current.next != self.head):
            print(current.data)
            current = current.next
        print(current.data)

if __name__ == "__main__":
    slist = Slist()
    slist.addNodeAtBegining(10)
    slist.addNodeAtBegining(20)
    # slist.addNodeAtBegining(30)
    slist.addAtEnd(5)
    slist.addAtEnd(2)
    # slist.addAtEnd(1)
    # slist.addNodeAtBegining(30)
    slist.addNthPosition(2, 3)
    # slist.addNodeAtBegining(10)
    # slist.deleteNode(1)
    # slist.deleteNode(20)
    # slist.deleteNode(10)
    slist.deleteNode(2)
    slist.printNode()