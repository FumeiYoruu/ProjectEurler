#store all possible coins 
coins = [0,1,2,5,10,20,50,100,200]
#initialize the dp matrix
#the dimensions stand for the largest coin used and the value of the sum of the coins
dp = [[]]
#for instances that have a sum of 0, there is only one way
for i in range (1,9):
    dp.append([1])
#for sums that are created with 1 pence coins, there is only one way
for i in range (1,201):
    dp[1].append(1)
#uses some dynamic programming techniques to calculate this instance from the former instance
for i in range (2,9):
    for j in range(1,201):
        if (j>=coins[i]):
            dp[i].append(dp[i][j-coins[i]]+dp[i-1][j])
        else:
            dp[i].append(dp[i-1][j])
#print the answer that uses all eight possible coins and forms 200
print(dp[8][200])    

