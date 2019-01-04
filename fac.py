def fac(n):
	if (n<=1):
		return 1
	else:
		return (n * fac(n-1))

x=input("Enter number:")
print(fac(x))
