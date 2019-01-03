res=input("[p,q]:")
#Define response lists
#p>r
#r>s
#s>p
r1=["p","r","s"]
r2=["r","s","p"]

while res != 'q':
	print ("Rock, Paper, Scissors")
	p1=input("Player 1 [r,p,s]:")
	p2=input("Player 2 [r,p,s]:")
	print(p1,p2)
	if (r2[r1.index(p1)]==p2):
		print("Player 1 wins!")
		res=input("[p,q]")
	elif (p1 != p2):
		print("Player 2 wins!")
		res=input("[p,q]")
	else:
		print("Tie!")