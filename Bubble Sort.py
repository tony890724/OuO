import random

length = 8

num = []

for i in range(length):
    temp = random.randint(0,99)
    num.append(temp)

#num.sort()
#print(num)

i = length

while i > 1:
    for j in range(i-1):
         if(num[j] > num[j+1]):
            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp
    i -= 1