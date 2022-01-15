import math
def isprime(x):
    #test if it is prime
    i = 2
    while (i * i <= x):
        if (x % i == 0):
            return False
        i +=1
    return True

a = -999
ans = 0
al = 0
bl = 0
#iterate over every possible a and b
while (a<1000):
    b = -1000
    while (b<=1000):
        n =0
        #test how far n can get
        while (isprime(abs(n*n+a*n+b))):
            n+=1
        if (ans < n):
            ans = n
            al = a
            bl = b
        b+=1
    a+=1
print(al*bl)
