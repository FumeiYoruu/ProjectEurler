import math
#start testing from the first triangular number
i = 1
while (True):
    #calculate the sum
    ans=int(i*(i+1)/2)
    cnt = 0
    j=1
    #check how many divisors are there
    while j * j <= ans:
        if(ans % j == 0):
            cnt+=1
        j+=1
    #if the divisor exceeds 500 output
    if (cnt >= 250):
        print(ans)
        break
    #add to the iterator
    i+=1
