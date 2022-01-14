index = 1
#count how many numbers are went over
first  = 1
#store the two number needed for calculating the sum
second = 1
while True:
    index += 1
    tmp = second
    second = first + second
    first = tmp
    #determine the length of the number 
    if len(str(first)) == 1000:
        print(index)
        break
