def push(stack,new_val):
	stack.append(new_val)
	return stack
	
def pop(stack):
	stack.pop(len(stack)-1)
	return stack
	
def peak(stack):
	return(stack[len(stack)-1])

x=[0,1,2,3,4,5,6,7,8,9,10]
print("original")
print(x)
print("push")
x=push(x,37)
print(x)
print("Push")
x=push(x,38)
print(x)
print("pop")
x=pop(x)
print(x)
print("peak")
print(peak(x))
print(x)