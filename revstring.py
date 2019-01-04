#Reverse a sentence given via user input
def rev(s):
	sl=s.split()
	print (sl)
	nl=[]
	ctr=0
	for ctr in range(len(sl)):
		print (str(ctr)+"-"+str(sl[ctr])+"-"+str(len(sl)-ctr))
		nl.append(sl[len(sl)-(ctr+1)])
		ctr=ctr+1
	
	return nl

s=raw_input("Enter a sentence:")
print(rev(s))
