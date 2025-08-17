#Write a program to find the factorial of a given number using a for loop.
def Factorial(n):
    t = 1
    for i in range(1, n+1):
        t = t * i
    return t
n = int(input())
print(Factorial(n))
