a = 1; b = 2; fibSum = 0;

while (b <= 4000000):
    fibSum += b;
    temp = a + 2*b;
    b = 2*a + 3*b;
    a = temp;
    
print "Fib %d" % (fibSum);