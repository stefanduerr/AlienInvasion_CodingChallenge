import csv
import sys
import time
from itertools import cycle

# Codewars Coding Challenges
# Jede Funktion ist eine Challenge


def up_down(number):
    neighbors = (number-1, number+1)
    return neighbors

def format_number(param):
    if isinstance(param, int):
        if not param < 0:
            param = str(param)[::-1]
            length = len(param)
            iteration = 0
            for n in range(1, length):
                if n % 3 == 0:
                    param = param[:n+iteration] + ',' + param[n+iteration:]
                    iteration+= 1
            param = param[::-1]
            print("Your formatted number is: ", param)
        else:
            print("Please enter a non-negative number.")
    else:
        print("Only numbers are supported.")

def param_count(*args):
    return(len(args))

def simpleGrep(searchwords, files_list_):
    for file in files_list_:
        for word in searchwords:
            csv_file = csv.reader(open(file, "r"), delimiter=",")
            for index, row in enumerate(csv_file):
                if word in row[0]:
                    print(file, word, '| Row %d: ' % (index + 1), row)

def to_jaden_case(string):
    string = string.capitalize()
    string = list(string)
    for l in range(len(string)):
        if string[l] == " " and string[-1] != string[l]:
            string[l+1] = string[l+1].upper()
    string = "".join(string)
    return string

def duplicate_encode(word):
    word = list(word.lower())
    duplicates = list()
    uniques = list(range(len(word)))
    for x in range(len(word)):
        for y in range(len(word)):
            if word[y] == word[x] and y != x:
                if x not in duplicates:
                    duplicates.append(x)
                if y not in duplicates:
                    duplicates.append(y)
    uniques = list(set(uniques) - set(duplicates))
    for w in duplicates:
        word[w] = ")"
    for v in uniques:
        word[v] = "("
    word = "".join(word)
    return print(word)
                
# return masked string
def maskify(cc):
    cc = list(cc)
    if len(cc) > 4:
        nochange = cc[-4:]
        cc = cc[0:-4]
        for letter in range(len(cc)):
            cc[letter] = "#"

    cc = "".join(cc)
    nochange = "".join(nochange)
    result = cc + nochange
    print(result)

def square_digits(num):
    nums = list(str(num))
    arr = list()
    print(nums)
    for x in nums:
        arr.append(str(int(x) ** 2))
    arr = "".join(arr)
    return arr

def persistence(num, count=0):
    if len(str(num)) > 1:
        new = 1
        for n in str(num):
            new *= int(n)
        print(new)
        return persistence(new, count+1)
    else:
        return count
        
def buildsum():
    odd = list(range(1, 50, 2))
    nums = list(range(1, 10))
    iteration = iter(nums)
    x = 1
    for y in range(1,10):
        for i in range(0, len(odd), y):
            yield odd[i:i+x]
            x+=1

def row_sum_odd_numbers():
    lists = list(buildsum())
    return lists

def make_list():
    odd = list(range(1, 50, 2))
    sample_size = 1
    sums = [] 
    for i in range(0, len(odd)):
        yield odd[i:i+x]
        x+=1   

def recursion_approach(list_of_odds, list_of_sums, row, count):
    if count == 1:
        list_of_sums.append(list_of_odds[count-1])
        list_of_odds.remove(list_of_odds[count-1])
        return recursion_approach(list_of_odds, list_of_sums, row, count+1)
    elif count <= row:
        list_of_sums.append(sum(list_of_odds[0:count]))
        del list_of_odds[0:count]
        return recursion_approach(list_of_odds, list_of_sums, row, count+1)
    else:
        return list_of_sums[row-1]
    
def row_sum_odd_numbers(row):
    gaussian_max = int(row*(row+1))
    return recursion_approach(list_of_odds=list(range(1,gaussian_max,2)), list_of_sums=list(), row=row, count=1)

def create_phone_number(phone):   
    start = "".join(map(str, phone[0:3]))
    mid = "".join(map(str, phone[3:6]))
    end = "".join(map(str, phone[6:10]))
    phone_number = "(" + start + ") " + mid + "-" + end
    return(phone_number)

def to_camel_case(string):
    string = list(string)
    newstring = []
    for x in range(len(string)):
        if (string[x] == "-" or string[x] == "_") and string[-1] != string[x]:
            string[x+1] = string[x+1].upper()
    newlist = [x for x in string if "-" not in x and "_" not in x]
    string = "".join(newlist)
    return print(string)

def new_approach():
    odds = list(range(1, 50, 2))
    sample_size = 1
    sums = []
    iterate_list = iter(odds)
    operator = True
    while operator == True:
        x = 1
        for _ in range(x):
            item = next(iterate_list, "end")
            itemx = next(iterate_list, "end")
            if item == "end":
                operator = False
            sums.append(str(item) + str(itemx))
            x += 1
    print(sums)

def fibonacci(input):
    fibos = [0,1,1]
    if input > 2:
        for x in range(input-2):
            fibos.append(fibos[-1]+fibos[-2])
    return fibos[input]
            
to_camel_case("The_Stealth_Warrior")
print(row_sum_odd_numbers(5))
new_approach()
print(persistence(989))
square_digits(23498)
maskify("AT420001000200033690")
print(to_jaden_case("this is dölskj sdisodi ididi wowowow a test message."))
format_number(92875928372987)
print(fibonacci(38))