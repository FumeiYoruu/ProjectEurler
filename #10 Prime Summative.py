#the number to test if is prime
i=2
#the output
sum=0
#go over every number below four million
while i<=2*1e6:
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
        sum+=i
    i+=1
    
print(sum)
