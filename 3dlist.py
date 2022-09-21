class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

class Dlist:
	def __init__(self):
		self.head = None

	def insert_at_begining(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def insert_at_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			current = self.head
			while(current.next):
				current = current.next

			current.next = new_node
			new_node.prev = current

	def insert_at_position(self, position, data):
		new_node = Node(data)

		if self.head is None and position > 0:
			print("Position out of bound")
		else:
			if self.head is None:
				self.head = new_node
			else:
				curr_pos = 0
				current = self.head
				prev = None
				while(curr_pos < position):
					prev = current
					current = current.next
					curr_pos += 1

				if current == self.head:
					new_node.next = self.head
					self.head.prev = new_node
					self.head = new_node
				elif current is None and prev:
					prev.next = new_node
					new_node.prev = prev
				else:
					new_node.next = current
					new_node.prev = prev
					prev.next = new_node
					current.prev = new_node
				
	def remove(self, data):
		if self.head is None:
			print("List is empty")
		else:
			current = self.head
			prev = None
			exist = False
			while(current):
				if current.data == data:
					exist = True
					break
				prev = current
				current = current.next

			if not exist or current is None:
				print("element doesn't exist")
			else:
				if current == self.head and current.next is None:
					self.head = None
				elif current == self.head:
					self.head.next.prev = None
					self.head = self.head.next
				elif current.next is None:
					prev.next = None
				else:
					prev.next = current.next
					current.next.prev = prev


	def print(self):
		print(">>>>>>>>")
		current = self.head
		while(current):
			print(current.data)
			current = current.next
		print(">>>>>>>>")

if __name__ == "__main__":
	dlist = Dlist()
	# dlist.insert_at_begining(10)
	# dlist.insert_at_begining(20)
	# dlist.insert_at_begining(30)

	# dlist.insert_at_end(10)
	# dlist.insert_at_end(20)
	# dlist.insert_at_end(30)
	dlist.insert_at_position(0, 10)
	dlist.insert_at_position(1, 20)
	dlist.insert_at_position(2, 30)

	# dlist.remove(10)
	# dlist.remove(20)
	# dlist.remove(30)
	
	dlist.print()