
"""Write a program to take an integer input and print the sum of its digits."""
 def SumOfDigits(n):
     total_Sum  = 0
     for i in n:
         total_Sum += int(i)
     return total_Sum
 n = input()
 print(SumOfDigits(n))
