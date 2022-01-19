#store the numbers on the diagonal in a list
seq = [1]
#the final matrix is 1001 by 1001, therefore there are 501 layers
for i in range(501):
    if not i:
        continue
    #for each layer, calculate the numbers on the corner and add to the list
    #the num is the sum of the last number and the layer number times two
    for j in range(4):
        seq.append(seq[-1]+i*2)
#add them all up
ans = 0
for i in seq:
    if i<100:
        print(i)
    ans += i
print(ans)
