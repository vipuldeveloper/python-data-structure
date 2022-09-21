class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			queue = []
			queue.append(self.root)
			while(len(queue)):
				current = queue.pop(0)
				if not current.left:
					current.left = Node(data)
					break
				else:
					queue.append(current.left)

				if not current.right:
					current.right = Node(data)
					break
				else:
					queue.append(current.right)

	def search(self, data):
		if self.root is None:
			return False
		else:
			return self.search_node(self.root, data)

	def search_node(self, root, data):
		if root is None:
			return False
		elif root.data == data:
			return True
		else:
			found = self.search_node(root.left, data)
			if not found:
				found = self.search_node(root.right, data)
			return found

	def delete(self, key):
		if self.root is None:
			print("Tree is empty!")
		elif self.root.left == None and self.root.right == None:
			if self.root.data == key:
				self.root = None
		else:
			q = []
			q.append(self.root)
			delete_node = None
			while(len(q)):
				temp = q.pop(0)
				
				if temp.data == key:
					delete_node = temp

				if temp.left:
					q.append(temp.left)

				if temp.right:
					q.append(temp.right)

			if delete_node:
				last_r_data = temp.data
				self.delete_deepest(temp)
				delete_node.data = last_r_data
			else:
				print("Key doesn't exist")


	def delete_deepest(self, deepest_node):
		q = []
		q.append(self.root)
		while(len(q)):
			temp = q.pop(0)
			if temp == deepest_node:
				temp = None
				return
			if temp.right == deepest_node:	
				temp.right = None
				return
			else:
				q.append(temp.right)

			if temp.left == deepest_node:
				temp.left = None
				return
			else:
				q.append(temp.left)


	def printTree(self):
		self.print(self.root)

	def print(self, root):
		if root:
			print(root.data)
			self.print(root.left)
			self.print(root.right)

if __name__ == "__main__":
	bt = BinaryTree()
	# bt.root = Node(10)
	# bt.root.left = Node(20)
	# bt.root.right = Node(30)
	bt.insert(10)
	bt.insert(20)
	bt.insert(30)
	found = bt.search(30)
	print("Search result", found)
	bt.delete(10)
	bt.printTree()