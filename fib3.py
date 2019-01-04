def fib(n):
	if (n<2):
		return 2
	else:
		return(fib(n-1)+fib(n-2))

n=input("Enter number:")
print(fib(n))
