import math;

value = 600851475143;
primeArray = [2, 3];
index = 0;
length = len(primeArray);
    
def nextPrime():
    primeIndex = 0;

    nextOdd = primeArray[-1] + 2;
    
    while (primeArray[primeIndex] <= math.sqrt(nextOdd)):
        if (nextOdd % primeArray[primeIndex] == 0):
            nextOdd += 2;
            primeIndex = 0;
            continue;
        
        primeIndex += 1;
    
    return nextOdd;

largest = 2;

while (value / primeArray[index] != 0):
    if (value % primeArray[index] == 0):
        value /= primeArray[index];
        largest = primeArray[index];
        continue;
    
    index += 1;
    if (index == (length-1)):
        largest = nextPrime();
        primeArray.append(largest);
        length += 1;
    else:
        largest = primeArray[index];
        
    continue;

print (primeArray);
print (largest);