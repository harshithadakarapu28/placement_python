"""REPEATED LETTER CAN'T EXECUTED"""
def repeatedLetter(string):
    count = ""
    for char in string:
        if  char not in count:
            count += char
    return count
string = input()
print(repeatedLetter(string))
