digits = 2
#calculate the most digits a number can have to equal to the sum of the 5th power of its digits
while digits*(9**5)>=10**(digits-1):
    digits +=1
ans = 0
#go over every digit and the corresponding numbers
for i in range (2,digits):
    for j in range (10**(i-1),10**i):
        #find each digit of the number
        num = str(j)
        sum = 0
        #test if the sum of the digits equal to the number
        for k in num:
            sum+=int(k)**5
        #add to the result
        if j == sum:
            ans+=j
print(ans)
