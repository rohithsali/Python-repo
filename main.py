# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from os import path
def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    #name = input("wht is yr name?")
    print("Hi,")  # Press Ctrl+F8 to toggle the breakpoint.

def files():
    file_temp = open("myfile.txt", "w+")
    for i in range(10):
        file_temp.write("this is some text\n")
    file_temp.close()

def file_read():
    file_temp = open("myfile.txt", "r")
    contents = file_temp.read()
    print(contents)

def osPath():
    print("path:", path.realpath("myfile.txt"))
    print("path and name", path.split(path.realpath("myfile.txt")))

def pow(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

def multiadd(*args):
    result = 0
    for i in args:
        result = result + i
    return result

def loops():

    days = ["Mon", "Tue", "Wed", "Thur"]
    for d in days:
        print(d)

    for i,day in enumerate(days):
        print(i,day)

def is_palindrome(teststr):
    # Your code goes here.
    teststr = teststr.lower()
    print(teststr)
    reverseStr = teststr[::-1]
    print(reverseStr)
    if reverseStr == teststr:
        return True
    else:
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
#   print(print_hi())
#    print(pow(2, 3))
#    print(multiadd(1, 2, 3, 5))
#    loops()
    #print(is_palindrome("Madam"))
    total = 0
    test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.",
    "Race car!"]
    for word in test_words:
        print(is_palindrome(word))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    file_read()
    osPath()
    try:
        x=int("five")
    except ValueError:
        print("There is a value error.")
    finally:
        print("Something went wrong.")
