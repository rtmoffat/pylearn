def get_integer():
	return int(input("Number:"))

def chk_prime(num):
	if (num == 1):
		return False

	for x in range(2,num):
		if not (num % x):
			print(x)
			return False
	return True

num=get_integer()
prime=chk_prime(num)
print (prime)

