import random

length = 8
num = []
for i in range(length):
    temp = random.randint(0,99)
    num.append(temp)
i = length
while i > 1: 
    for j in range(i - 1):
        if(num[j] < num[j+1]): #判別前後數字大小 以調整順序
            num[j] = num[j] ^ num[j+1]
            num[j+1] = num[j] ^ num[j+1]
            num[j] = num[j] ^ num[j+1]
    i -= 1 #因為已將最小的數字排至最後方 所以下一次可以少比較一個數
print(num)