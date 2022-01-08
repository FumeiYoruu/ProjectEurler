



#store the answer
ans = 0
for i in range(10000):

    num=i+1
    sum = 0
    #add up the divisors of the number
    div = 1
    while div * div < num:
        div+=1
        if num%div == 0:
            sum+=int(num/div)
            sum+=div
    if (div+1)**2 == num:
        sum+=div+1
    sum+=1
    #add up the divisors of the sum 
    div = 1
    while div * div < sum:
        div+=1
        if sum%div == 0:
            num-=int(sum/div)
            num-=div
    if (div+1)**2 == sum:
        num-=div+1
    num-=1
    #compare and add to the final value
    #amicable numbers cannot be the same
    if num==0 and sum != i+1:
        ans+=i+1
        print(i+1, sum)
print(ans)
