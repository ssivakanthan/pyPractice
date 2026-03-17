import array
from operator import truediv
from typing import Any


def reverseString():
    str1 = "sajishan"
    str2 = ""

    for i in str1:
        str2 = i + str2

    print("og: " + str1)
    print("reverse: " + str2)

def reverse(s: str) -> str:
    return s[::-1]

def palindrome(s: str) -> str:
    pal = s[::-1]

    if s == pal:
        return True
    else:
        return False

def maxnum(arr: array) -> int:
    max = arr[0]
    for i in arr:
        if arr[i] > max:
            max = arr[i]

    return max

def fizzbuzz(n: int):
    s = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            s.append("fizz")
        elif i % 5 == 0:
            s.append("buzz")
        else:
            s.append(i)
    return s

def charCount(str: str):
    dict = {}
    for char in str:
        dict[char] = dict.get(char,0) + 1
    return dict

def uniqueChar(str: str):
    dict = {}

    for char in str:
        dict[char] = dict.get(char,0) + 1

    for char in dict:
        if dict.get(char) == 1: return char
        
def merge(a,b):
    output = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]: 
            output.append(a[i]) 
            i +=1
        elif b[j] < a[i]: 
            output.append(b[j])
            j +=1
    return output + a[i:] + b[j:]        
            
def fact(factorial):
    output = 1
    for i in range (2,factorial+1):
        output = output*i
    return output  

def removedupe(arr):
    return list(set(arr))

def evenorodd(num):
    if num %2 == 0: return "Even"
    else: return "Odd"

def vowelcounter(string):
    sum = 0
    for char in string:
        if char in 'aeiou':
            sum +=1
    return sum

def numofvowels(string):
    dict = {}
    for char in string:
        if char in 'aeiou':
            dict[char] = dict.get(char,0) + 1

    return dict

def commonelemnets(a,b):
    return (list(set(a) & set(b)))

def fibonacci(num):
    fib_series = [0,1]

    while len(fib_series) -1  < num:
        fib_series.append(fib_series[-1]+fib_series[-2])

    return fib_series[:num +1]
def main():
    print("Hello from pypractice!")
    # reverseString()
    # print(reverse("SAJISHAN"))
    # print(palindrome("BOB"))
    # print(max([1,32,3,41,67]))
    # print(fizzbuzz(10))
    # print(charCount("Sajishan"))
    # print (uniqueChar("baac"))
    # print(merge([2,4,6],[1,3,5]))
    # print(fact(5)) 
    # print (removedupe(['1','2','3','1']))
    # print (evenorodd(52))
    # print(vowelcounter("asa"))
    # print (numofvowels("sajishan"))
    # print ((commonelemnets(("a","b","c"),("a","y","z"))))
    print (fibonacci(5))




if __name__ == "__main__":
    main()
