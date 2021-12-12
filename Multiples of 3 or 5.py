
cnt_3=int(999/3)
cnt_5=int(999/5)
cnt_15=int(999/15)

#count all the multiples of 3,5 and 15
#the answer would be the sum of multiples of 3 and 5 subtracted by the sum of multiples of 15

def add(x):
    return int((1+x)*x/2)
print(3*add(cnt_3)+5*add(cnt_5)-15*add(cnt_15))
