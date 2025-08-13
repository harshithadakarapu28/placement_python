"""Reverse of a number"""
def rev(n,a,b):
    while(n!=0):
        a = n%10
        b = (b*10)+a
        n = n//10
    return b
n = int(input())
a = n
b = 0
print(rev(n,a,b))
