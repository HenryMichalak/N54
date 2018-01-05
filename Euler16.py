def compute():    #defining compute
	hi = 2**1000      #finds the value of 2^1000
	howdy = sum(int(c) for c in str(hi))     #sets howdy equal to the sum of each
	#individual integer in 2^1000
	return (howdy)     #finds the value


print(compute())    #shows me the value, which is 1366
