import random
import string

num = list()

for item in range(6):
    randomInt = random.randint(1, 33)
    while (randomInt in num):
        randomInt = random.randint(1, 33)
    num.append(randomInt)
num.sort()
num.append(random.randint(1, 16))
print(num)

