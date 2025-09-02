#Write a program to calculate the sum of all elements in the list starting from the first occurrence of i to the first occurrence of j (inclusive).
def SumOfEle(n,i,j):
    capture = False
    total = 0
    for num in n:
        if num == i:
            capture  = True
        if capture:
            total += num
        if num == j:
            break
    return total 
n = list(map(int, input().split()))
i = int(input())
j = int(input())
print(SumOfEle(n,i,j)) 
