#the greates c is 499 for a+b>c
for c1 in range(499):
    c=c1+1
    #for every c, assume a is smaller than b, go over all the a
    for a1 in range(int((1000-c)/2)):
        a=a1+1
        b=1000-c-a
        #test if the three numbers satisfied the phythagorean theorum
        if (c**2==a**2+b**2):
            print(a*b*c)
