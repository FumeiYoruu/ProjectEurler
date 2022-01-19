#a function calculating fib numbers
def fib(a):
    if (a<=2):
        return 1
    else: 
        return fib(a-2)+fib(a-1)

i=0
sum=0
#count all the fibs under 4 million
while(fib(i+1)<=1e6*4):
    i+=1
    ans=fib(i)
    if(ans%2==0):
        sum+=ans
print(sum)
