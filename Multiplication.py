"""Multiplication Table Of a Number"""
def multiplication(multiplicand, multiplier, result):
    for i in range(1, multiplier+1):
        result = multiplicand* i
        print(f"{multiplicand} * {i} = {result}")  
multiplicand = int(input())
multiplier = int(input())
result = 0
multiplication(multiplicand, multiplier, result)
