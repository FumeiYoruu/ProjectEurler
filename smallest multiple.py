i =20
ans=1

#list of prime factors under 20
p=[2,3,5,7,9,11,13,17,19]

#a function that can find the number of each prime factor
def prime_factor(x):
    d={}
    j=0
    #check every prime number in the list p
    while(j<len(p)):
        if (x%p[j]==0):
            if(p[j] in d.keys()):
                 d[p[j]]+=1
            else:
                d[p[j]]=1
            x/=p[j]
        else:
            j+=1
    return d

d={}

while i!=1:
    #if the prime factor in the new number is greater than the current one, add to the dictionary
    for key, value in prime_factor(i).items():
        if(key in d.keys() and d[key]<value):
            d[key]=value
        elif not key in d.keys():
            d[key]=value

    i-=1

#time all the prime factors together
for key,value in d.items():
    ans*=key**value
print(ans)
    
