a = str(2**1000)
#calculate the number and change it to a string
ans = 0
#access every digit through a string
for i in a:
    ans+=int(i)
print(ans)
