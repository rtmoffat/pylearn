name=input("Enter your name:")
age=int(input("Enter your age:"))
cent=100-age
year=str(cent+2018)
my_msg=name+" will be 100 in the year "+year+"\n"
print(my_msg)
times=int(input("How many times do you want to see this?"))
print(times*my_msg)
