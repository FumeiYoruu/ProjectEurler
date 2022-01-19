'''
use a set to store the numbers in order to get rid of the same numbers
'''
#the set is initialized
nums = {1}
#go over every possible a and b
for a in range(2,101):
    for b in range(2,101):
        #add to the set the power
        nums.add(a**b)
#print the length
#we add a one to the set in order to make it a set instead of a dict, now a minus one is needed
print(len(nums)-1)
