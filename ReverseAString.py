#Write a program to take a string input and print it in reverse.
def Reverse(n):
    for i  in range(len(n)-1 , -1, -1):
        print(n[i], end = "")
n = input()
Reverse(n)
