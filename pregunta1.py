import math

sum = 1000
for a in range(1, int(sum/3)):
    for b in range(1, int(sum/2)):
        c = sum - a - b;
        if ( a*a + b*b == c*c ):
            print("a={}, b={}, c={}".format(a, b, c))

