#Write a program to find a maximum and minimum number in a string.
def Min_Max(n):
    r = []
    for i in n:
        if i.isdigit():
            r.append(i)
    print(max(r))
    print(min(r)) 
n = input() 
Min_Max(n)
