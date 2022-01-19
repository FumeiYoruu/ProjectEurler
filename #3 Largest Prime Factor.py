factor=1
# a function that can test if the number is prime
def isprime(x):
    i=2
    while (i*i<=x):
        if(x%i==0):
            return False
        i+=1
    return True

#find factors of the number from big to small and test if it is prime
while (factor*factor<= 600851475143):
    if( 600851475143%factor==0 and isprime(600851475143/factor)):
        print( 600851475143/factor)
        quit()
    factor+=1

#if does not find the factor, search the rest numbers
while (factor-1):
    factor-=1
    if ( 600851475143%factor==0) and isprime(factor):
        print(factor)
        quit()


