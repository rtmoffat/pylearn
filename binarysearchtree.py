class binNode:
	def __init__(self,value=None):
		self.value=value
		self.left=None
		self.right=None
	
	def add(self,val):
		if (val<=self.value):
			if (self.left):
				self.left.add(val)
			else:
				self.left=binNode(val)
		else:
			if (self.right):
				self.right.add(val)
			else:
				self.right=binNode(val)
	
	def inorder(self):
		if (self.left):
			for x in self.left.inorder():
				yield x
		
		yield self.value
		
		if self.right:
			for x in self.right.inorder():
				yield x
		
class binTree:
	def __init__(self):
		self.root=None
	
	def __iter__(self):
		if (self.root):
			return self.root.inorder()
	
	def __contains__(self,val):
		node=self.root
		while node:
			if val>node.value:
				print("right"+str(node.value))
				node=node.right
			elif val<node.value:
				print("left"+str(node.value))
				node=node.left
			else:
				return True
		return False
	
	def add(self,value):
		if self.root is None:
			self.root=binNode(value)
		else:
			self.root.add(value)

myTree=binTree()
myTree.add(25)
myTree.add(32)
myTree.add(45)
myTree.add(15)
myTree.add(9)
#print (myTree.root.value)
#print(myTree.root.left.value)
#print(myTree.root.right.value)
#print(myTree.root.left.left.value)
for x in myTree:
	print(x)
if (15 in myTree):
	print("Yes")
else:
	print("No")