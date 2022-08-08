from xml.etree.ElementPath import prepare_parent


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Dlist:
    def __init__(self):
        self.head = None
        
    def addNodeAtBegining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node.next
            self.head = new_node

    def addAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.addNodeAtBegining(data)
        else:
            current = self.head
            while(current.next):
                current = current.next
            
            new_node.next = current.next
            new_node.prev = current.prev
            current.next = new_node
                            
    def printNode(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

if __name__ == "__main__":
    dlist = Dlist()
    dlist.addNodeAtBegining(10)
    dlist.addNodeAtBegining(20)
    dlist.addAtEnd(5)
    dlist.addAtEnd(4)
    dlist.addNodeAtBegining(15)
    # slist.addAtEnd(2)
    # slist.addAtEnd(1)
    # slist.addNodeAtBegining(30)
    # slist.addNthPosition(2, 3)
    # slist.addNodeAtBegining(10)
    # slist.deleteNode(1)
    # slist.deleteNode(50)
    dlist.printNode()