cnt = [0] #store how many permutations have been gone over
st=[0,0,0,0,0,0,0,0,0,0] #store if the number is used
res=[0,0,0,0,0,0,0,0,0,0] #store the permutation

def dfs(x):
    if (x == 10):
        cnt[0]+=1
        #if it is the millionth, print
        if cnt[0]==1e6:
            for i in range (10):
                print(res[i],end="")
    for i in range (10):
        #check if the number is used
        if not st[i]:
            res[x] = i
            st[i] = 1
            #go to next step
            dfs(x+1)
            st[i] = 0
dfs(0)
