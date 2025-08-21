#Find Prime Numbers in a Range.
def PrimeNum(n):
    result = []
    for j in n:
        count  = 0
        for i in range(1,j+1):
            if j % i == 0:
                count += 1
        if count == 2:
            result.append(j)
    return result
n =  list(map(int, input().split()))
print(f"Prime Numbers are:",PrimeNum(n))
