def sumOfNaturalNums(n, num):
    for i in range(1, n+1):
        num += i
    print(num)
n = int(input())
num = 0
sumOfNaturalNums(n, num)
