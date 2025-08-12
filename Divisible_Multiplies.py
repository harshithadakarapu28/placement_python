"""1.Accepts a list of integers from the user (space-separated).
2.Finds all numbers in the list that are divisible by 7.
3.Multiplies each of those numbers by 3.
4.Prints the resulting list."""
n = list(map(int, input().split()))
result = []
s = []
for i in n:
    if i % 7 == 0:
        s.append(i)
for j in s:
    k = j*3
    result.append(k)
print(result)
