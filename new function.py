def bubble_sort(num): 
    i = quantity
    while i > 1: 
        for j in range(i - 1):
            if(num[j] < num[j+1]): #判別前後數字大小 以調整順序
                num[j] = num[j] + num[j+1]
                num[j+1] = num[j] - num[j+1]
                num[j] = num[j] - num[j+1]
        i -= 1 #因為已將最小的數字排至最後方 所以下一次可以少比較一個數
    return num #回傳list

quantity = int(input()) #輸入你的list有幾個數字
num = []
for i in range(quantity):
    temp = int(input()) #輸入你的list中的數字
    num.append(temp)
print(bubble_sort(num)) #印出排序完的list