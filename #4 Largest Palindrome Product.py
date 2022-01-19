
#define a function that can check if the number is palindrome
def ifpal(x):
    l=len(str(x))
    i=0
    while(i<int(l/2)):
        if int(x/(10**i))%10 != int(x/(10**(l-i-1)))%10:
            return False
        i+=1
    return True

#check all multiplication of three digit numbers and find the max
ans = 0

for i in range(100,1000):
    for j in range (100,i+1):
        if(ifpal(i*j) and i*j>ans):
            ans=i*j
print(ans)

