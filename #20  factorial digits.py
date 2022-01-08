num = 1
#calculate the factorial
for i in range(98):
    num*=i+2
#turn the number into a string so can iterate over every digit
num = str(num)
ans=0
for i in num:
    ans+=int(i)
print(ans)
