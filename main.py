import array
from operator import truediv
from textwrap import indent
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
        dict[char] = dict.get(char, 0) + 1
    return dict


def uniqueChar(str: str):
    dict = {}

    for char in str:
        dict[char] = dict.get(char, 0) + 1

    for char in dict:
        if dict.get(char) == 1:
            return char


def merge(a, b):
    output = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            output.append(a[i])
            i += 1
        elif b[j] < a[i]:
            output.append(b[j])
            j += 1
    return output + a[i:] + b[j:]


def fact(factorial):
    output = 1
    for i in range(2, factorial + 1):
        output = output * i
    return output


def removedupe(arr):
    return list(set(arr))


def evenorodd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def vowelcounter(string):
    sum = 0
    for char in string:
        if char in "aeiou":
            sum += 1
    return sum


def numofvowels(string):
    dict = {}
    for char in string:
        if char in "aeiou":
            dict[char] = dict.get(char, 0) + 1

    return dict


def commonelemnets(a, b):
    return list(set(a) & set(b))


def fibonacci(num):
    fib_series = [0, 1]

    while len(fib_series) - 1 < num:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series[: num + 1]


def primenumber(num):
    if num < 2:
        return False
    elif num > 2:
        for i in range(2, (int(num**0.5) + 1)):
            if num % i == 0:
                return False
        return True
    else:
        return True


def primenumberlist(numlist):
    primeresult = []
    for num in numlist:
        if num < 2:
            primeresult.append("False")
        elif num > 2:
            is_prime = True
            for i in range(2, (int(num**0.5) + 1)):
                if num % i == 0:
                    is_prime = False
                break
            primeresult.append(is_prime)
        else:
            primeresult.append("True")

    return primeresult


def primenumberlistwithfunc(list):
    primeresultlist = []
    for num in list:
        primeresultlist.append(primenumber(num))

    return primeresultlist


def secondlargets(numlist):
    uniquenums = list(set(numlist))
    # uniquenums.sort(reverse=True)
    # return uniquenums[1]
    return uniquenums[-2]


def binarysearch(arr, target):
    # sorted array required, start at midle and compare less or more, move boundries in
    left = 0
    right = len(arr) - 1
    mid = 0

    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid

    return "Target not Found"

def mergesort(arr):
# recursive algo, divide array down into lowest possible element, sort and combine, repeat process 
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #recurssion
        mergesort(left_arr)
        mergesort(right_arr)

        #merge
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else: 
                arr[k] = right_arr[j]
                j+=1

            k+=1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
    return arr

def insertionsort(arr):
# start at zero and compare left/right move forward, if larger element is found compare all the way back down
    
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:

            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        i += 1

    return arr   

def bubblesort(arr):
# start at zero compare left/right all the way to end of array and reset back to start
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
        

import json
def jsonmodulesample():
    people_string = """
    {
        "people": [
            {
                "name": "Sajishan Sivakanthan",
                "phone": "555-555-5555",
                "email": "ss@gmail.com",
                "has_license": true
            },
            {
                "name": "Saji Siva",
                "phone": "555-555-5556",
                "email": null,
                "has_license": false
            }
        ]

    }


    """
    #loads() - loads a string
    data = json.loads(people_string)
    #print(type(data['people']))
    #print(data['people'])

# Looping through an array which is now python list and accessing the name which is a dict value (people is key, name is value)
    #for person in data['people']:
    #    print(person['name'])

    for person in data['people']:
        del person['phone']

    new_string = json.dumps(data, indent = 2, sort_keys=True)

    print (new_string)


def jsonmodulefromfile():
    
    with open('data.json') as f:
        #load() - loads a file 
        data = json.load(f)

    for state in data['states']:
        #print(state['name'],state['abbreviation'])
        del state["area_codes"]

    with open ('new_states.json', "w") as f:    
        json.dump(data, f, indent = 2)

import json
import requests
def jsonmodulefromapi():
    response = requests.get("https://catfact.ninja/breeds")

    data = response.json()

    #print(len(data['data']))
    #print(json.dumps(data, indent = 2))

    cats = {}
    
    
    i = 1
    for item in data['data']:
        cats[i] = {
        'breed' : item['breed'],
        'origin' : item['origin']
        }
        
        #print(f"Breed is: {breed}, Origin is: {origin}")
        i += 1

    with open('new_cats.json', "w") as f:
        json.dump(cats, f, indent = 2)
    
def completeAnagram(A,B):
    # Return Int
    # Input A,B
    # Go through both strings, get a count for each char in the string
    # compare the char count to second string
    # delete the difference
    dictA = {}
    dictB = {}
    count = 0

    for char in A:
        dictA[char] = dictA.get(char,0) + 1
    
    for char in B:
        dictB[char] = dictB.get(char,0) + 1
    
    print(dictA)
    print(dictB)

    for index in dictA:
   
        if index in dictB:
            if dictA.get(index) != dictB.get(index):
                count = count + abs(dictA.get(index) - dictB.get(index))
        else:
            count = count + dictA.get(index)

            
    for index in dictB:

        if index not in dictA:
            count = count + dictB.get(index)

    
    return count

def alternatingChar(string):

    # given a string, that only Contains A & B
    # iterate through that string and delete characters to ensure we only have A and B repeat
    # return INT, min number of chars to delete

    array = list(string)
    count = 0

    for i in range(len(array)-1):
        if(array[i] == "A" and array[i+1] == "B") or ((array[i] == "B" and array[i+1] == "A")):
            continue
        else:
            count +=1
    
    return count
            
  
    

def romantoint(string):

    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for i in range(len(string)):
        curr_char = string[i]
        if i + 1 < len(string):
            next_char = string[i+1]
        else: 0

        if dict[curr_char] >= dict[next_char]:
            total = total + dict[curr_char]

        else: 
            total = total - dict[curr_char]
    
    return total    
    
def runlenencoding(s):
    if len(s) == 0:
        return ""

    results = []

    #aaabbc a3b2c1

    i = 0
    while i < len(s):
        count = 1

        while (i + 1 < len(s)) and (s[i] == s[i+1]):
            count += 1
            i +=1
        
        results.append(s[i] + str(count))

        i+=1
    return "".join(results)


def stripe():
    transactions = [
    {'id': 'txn_001', 'user_name': 'Alice', 'amount': 5000,  'type': 'charge'},
    {'id': 'txn_002', 'user_name': 'Bob',   'amount': 12000, 'type': 'charge'},
    {'id': 'txn_003', 'user_name': 'Alice', 'amount': -5000, 'type': 'refund'},
    {'id': 'txn_004', 'user_name': 'Carol', 'amount': 8000,  'type': 'charge'},
    {'id': 'txn_005', 'user_name': 'Bob',   'amount': -3000, 'type': 'refund'},
    {'id': 'txn_006', 'user_name': 'Dave',  'amount': 8000,  'type': 'charge'},
    {'id': 'txn_007', 'user_name': 'Dave',  'amount': 8000,  'type': 'charge'},  # potential dup
    {'id': 'txn_008', 'user_name': 'Bob',   'amount': 12000, 'type': 'charge'},  # potential dup
]

    newlist = []
    for trans in transactions:
        if trans['amount'] > 9000:
            data = {'name':trans['user_name'],
                    'balance':trans['amount']
            }
            newlist.append(data)
    
    return newlist

def apiinterview():
    # API Endpoint returns authors and the number of publishings, we want to retrieve a list of authors above a certain threshold of publishing (200)

    # import modules

    # set varibales

    # get number of pages

    # get response for both pages 

    # check threshold and save if above

    # return list

    initial_response = requests.get("https://jsonmock.hackerrank.com/api/article_users")
    data = initial_response.json()
    total_pages = data['total_pages']

    i = 1
    list = []

    while i <= total_pages:
        params = {"page":i}
        response = requests.get("https://jsonmock.hackerrank.com/api/article_users",params=params)
        data = response.json()
      

        for author in data['data']:
            if author['submission_count'] > 2000:
                author_name = author['username']
                author_count = author['submission_count']

                author_final = {"author" : author_name,
                                "count" : author_count}


                list.append(author_final)

        i += 1        
    
    return list



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
    # print (fibonacci(5))
    # print (primenumberlist((0,1,3,4,5,6,7,8)))
    # print (primenumberlistwithfunc((0,1,3,4,5,6,7,8)))
    # print (secondlargets([9,2,3,7,1,2,3,4,4,2,2,4,6,7]))
    # print(binarysearch([1, 2, 7, 16, 22, 27, 34, 56, 59, 60, 67, 69, 100], 67))
    # print(mergesort([1, 12,4,6,11,2,9]))
    # print(insertionsort([1,67,3,7,4,2]))
    # print(bubblesort([8,7,6,5,4,2,1]))
    # jsonmodulesample()
    # jsonmodulefromfile()
    #jsonmodulefromapi()
    # print(completeAnagram('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke'))
    # print(alternatingChar('ABBABAAA'))
    # print(romantoint("CM"))
    # print(runlenencoding("aaabbc"))
    # print(stripe())
    print(apiinterview())
   

if __name__ == "__main__":
    main()
