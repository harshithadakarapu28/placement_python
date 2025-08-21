"""Write a program to take a list of numbers and print the sum of only even numbers."""
def SumOfEvenNum(n):
    total_sum = 0
    for i in n:
        if i % 2 == 0:
            total_sum += i
    return total_sum
n = list(map(int, input().split()))
print(f"the sum of even numbers is", SumOfEvenNum(n))
