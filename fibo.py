def fibo(limit,cur_num):
	print (cur_num)
	if (cur_num<limit):
		return(fibo(limit,cur_num+1))

x=input("Enter number of fibonacci numbers to generate:")
fibo(x,1)
