import math # imports module to the program
def compute():  #defining compute
	hi = math.factorial(100)   #finds 100!
	howdy = sum(int(c) for c in str(hi)) #takes each individual integer in 100!
	#and adds them together
	return (howdy) #finds value

print compute()   #shows me the value, which is 648
