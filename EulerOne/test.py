import math;

primeArray = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37];
index = 0;
primeIndex = 0;

nextOdd = primeArray[-1] + 2;

#prime = primeArray[primeIndex];

while (primeArray[primeIndex] <= math.sqrt(nextOdd)):
    if (nextOdd % primeArray[primeIndex] == 0):
        nextOdd += 2;
        primeIndex = 0;
        continue;
    
    primeIndex += 1;
    
primeArray.append(nextOdd);

print(primeArray);
    