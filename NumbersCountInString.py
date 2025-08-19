#Write a program to find the numbers count in a given string.
 def count(n):
     count = 0
     for i in n:
         if i.isdigit():
             count += 1
     print(count)
 n = input()
 count(n)
