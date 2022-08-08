class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_begining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node


    def print(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

if __name__ == "__main__":
    slist = SList()
    slist.add_begining(10)
    slist.add_begining(20)
    # slist.add_begining(30)
    # slist.add_begining(40)
    slist.add_at_end(50)
    slist.print() 