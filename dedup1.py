#Dedups a list using a set
def dedup(s):
	xs=set(s)
	xl=list(xs)
	return xl

names = ["Michele", "Robin", "Sara", "Michele"]
print(dedup(names))
