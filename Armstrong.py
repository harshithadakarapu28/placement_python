#Write a program to find the given number is Armstrong or not.
 def Armstrong(n):
     sum = 0
     total = 0
     for i in n:
         total = int(i)**3
         sum += total
     if sum == int(n):
         print("Armstrong")
     else:    
         print("Not an armstrong")
 n = input()
 Armstrong(n)
