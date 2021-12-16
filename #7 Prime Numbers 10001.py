cnt=0 #number of primes
i=2 #the current number
num=2 #the current prime number
while cnt<10001:
    j=2
    isprime=True
    #check if the number has factors
    while(j*j<=i):
        if(i%j==0):
            isprime=False
            break
        else:
            j+=1
    #add to the number if it is prime
    if isprime:
        cnt+=1
        num=i
    i+=1
    
print(num)
