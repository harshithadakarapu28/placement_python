#Find Frequency of Each Character in a String.
def FreqChar(n):
    r ={}
    for char in n:
        if char in r:
            r[char] += 1
        else:
            r[char] = 1
    return r
n = input()
print(FreqChar(n)) 
