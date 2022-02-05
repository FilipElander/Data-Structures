
""" 
a custom stack, uses the python list to create a stack. 

Push: to add an element to the top of the stack.
Pop: to retrieve the element at the top of the stack.
Size: to get the size of the stack.
Empty: to check if the stack is empty.
Peek: to get the value of the element at the top of the stack.

"""



class Stack:
	# Init
	def __init__(self):
		#the list
		self.elements = []



	# Pushes a element to the top of the stack	
	def push(self,data):
	
		self.elements.append(data)
	#pops the element on the top of the list (includes error handle if empty) 	
	def pull(self):
		if self.elements:
			return self.elements.pop()
		else:
			return None	

	# returns the size of the stack 		
	def size(self):
		return len(self.elements)

	# check if stack is empty	
	def empty(self):
		return True if self.size() == 0 else False

	# peeks at the elemnt of the top of the stack 
	def peek(self):
		return self.elements[-1]




