#length of each month in a year
months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
#record how many days past from 1900 Jan 1st
days = 1
#count the Sundays
cnt = 0
for i in range(101):
    #check if it is a leap year
    if i%4 == 0 and i != 0:
        months[2]=29
    else:
        months[2]=28
    #calculate the day count at the start of each month
    for j in range(12):
        days+=months[j+1]
        if(days%7 == 0):
            print(1900 + i, j+2)
            cnt+=1

print(cnt)
#we can see there are two days from 1900
#the answer is 173 minus the two days from 1900
