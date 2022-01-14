a={}

def abundant(x):
    #test if the number is abundant
    i = 2
    sum = 1
    #go over all the divisors and add them up
    while (i*i < x):
        if x%i == 0:
            sum+=i + x/i
        i+=1
    if (i * i == x):
        sum+=i
    #if the divisor is greater than x, it is abundant
    return sum > x

for i in range (28124):
    #make a dictionary that store whether each number is abundant
    if (i == 0 or i == 1):
        continue
    if (abundant(i)):
        a[i] = True
    else:
        a[i] = False

ans = 0
for i in range (28124):
    #go over every number under 28124
    if i==0 or i==1:
        continue
    flag = True
    for j in range (i-1):
        if j==0 or j==1:
            continue
        #if can be expressed as the sum of two abundant numbers, break
        if a[j] and a[i-j]:
            flag = False
            break
    if flag:
        ans+=i      
    
#the program does not count 1, so add one finally
print(ans+1)
