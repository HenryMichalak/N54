#This code is the solution to Euler problem number one. Euler Problem Number one asks
#"what is the sum of the integers between 0 and 1000 that
#are divisible by both 3 and five"

print sum(x for x in range(0,1000)  #print sum of numbers b/n 0-1000

    if (x % 3 == 0 or x % 5 == 0))  #if they are divisible by 3 or 5 w/o remainder,
    #find the sum of those digits
