#Binary Search

def findit(l,n):
	mid_val=l[len(l)//2]
	mid_index=len(l)//2
	print(l)
	#Got lucky
	if (n==int(mid_val)):
		return True
	elif (n != int(mid_val) and len(l)==1):
		return False
	elif (n<int(mid_val)):
		return findit(l[0:mid_index],n)
	elif (n>int(mid_val)):
		return findit(l[mid_index:len(l)],n)
	else:
		return False

l=[1,5,6,8,9,10,24,82,97,100,150,200,201,203]
n=input("Enter a number:")
print(findit(l,int(n)))

