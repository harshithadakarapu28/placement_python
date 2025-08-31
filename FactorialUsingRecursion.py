#Write a function that calculates the factorial of a given number using recursion.
def Factorial(n):
   if n == 0 or n == 1:
      return 1
   else:
      return n * Factorial(n -1)
n = int(input())
print("Factorial of given number is:" , Factorial(n))  
