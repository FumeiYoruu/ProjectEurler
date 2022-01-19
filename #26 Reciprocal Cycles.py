def div(x):
    #calculate the  cycle length
    #store the remainders that have existed with the dictionary nums
    nums = {}
    length = -1
    re = 10
    while re:
        an = int(re/x)
        length+=1
        re -= an * x
        if not re in nums.keys():
            #store the new remainder
            nums[re] = length
        else:
            #return if the remainder recurs
            return length - nums[re]
        re *= 10
        
    return 0
d = 2
ans = 0
num = 0
while d<1000:
    #see the length of the cycle for every number smaller than 1000
    i = div(d)
    #find the longest one
    if (i > ans):
        ans = i
        num = d
    d+=1
print(num)
        
    

        
