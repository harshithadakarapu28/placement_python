#Write a program that prints the first n numbers of the Fibonacci series.
def Fibonacci(n):
    a , b = 0 , 1
    for i in range(n):
        a ,b = b, a+b
    return a
n =  int(input())
print(Fibonacci(n))
