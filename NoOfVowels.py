#Write a program to find the number of vowels in a given string.
def Vowels(n):
    count = 0
    vowel = "aeiouAEIOU"
    for char in n:
        if char in vowel:
            count += 1
    return count
n = input()
print(Vowels(n))
