def bubble_sort(num):

    i = quantity

    while i > 1:
        for j in range(i - 1):
            if(num[j] < num[j+1]): #判別前後數字大小 以調整順序
                num[j] = num[j] ^ num[j+1]
                num[j+1] = num[j] ^ num[j+1]
                num[j] = num[j] ^ num[j+1]
        i -= 1
    return num

quantity = int(input())

num = []

for i in range(quantity):
    temp = int(input())
    num.append(temp)
    
print(bubble_sort(num))