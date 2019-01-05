class queue:
	def __init__(self):
		self.arr=[]
	
	def isempty(self):
		if (self.arr==[]):
			return True
		else:
			return False
	
	def enqueue(self,data):
		self.arr.append(data)
		
	def dequeue(self):
		del self.arr[0]
	
	def peek(self):
		return self.arr[0]
		
	def sizeOf(self):
		return len(self.arr)

q=queue()
q.enqueue(1)
q.enqueue(2)
print (q.arr)