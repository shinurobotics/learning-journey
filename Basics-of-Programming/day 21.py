import random as r
random.seed(1)
randInt = r.randint(0,10) # start <= N <= end
same as randInt = random.randint(0,10)
print(randInt)

from random import uniform
randUniform = uniform(1,1100) # 0.0 <= N <= 1.0
print(randUniform)

from random import random #,....,....
randFloat = random()
print(randFloat)

simplelist = [1,3,5,7,9,11]
pickElement = r.choice(simplelist)
print(pickElement)
print(simplelist)
r.shuffle(simplelist)
print(simplelist)

# ln 1 interfere with ln 7 and 11 so to avoid error use # on any two of the ln
#random python reference to random library
