sum1=0
sum2=0
#sum 1: sum of squares sum2: sum of numbers
for j in range(100):
    i=j+1
    sum1+=i**2
    sum2+=i
#sum2 squared minus sum1
print(sum2**2-sum1)
