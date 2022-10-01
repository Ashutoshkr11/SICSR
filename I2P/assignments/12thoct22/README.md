# Introduction To Python | Assignment 1

[Q1]

Accept a number from the user. Assume that the user enters a 3-digit
number. Check whether it is an Armstrong number by using string to
list/tuple conversion.
Notes:
1. A 3-digit Armstrong number is a number that is equal to the cube of its
digits.
2. To access an element of a list/tuple, use its index as follows:
list_name[0] will refer to the first element.

Method:
1. Use `input()` to get number from user
2. Use `list()` to cast input string to list
3. Use `int()` and the exponential operator `**` to get the sum of cubes of all digits
4. Compare to original number
5. Use `print()` to display result

Solution: 
```py
num = input("Enter a number")
nums = list(num)

total = int(nums[0])**3 + int(nums[1])**3 + int(nums[2])**3

if total == int(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
```


[Q2]

Accept the user’s nationality (country). If the user enters “India”, ask the
them to enter their state. If the user enters “Pune”, display “You are on
the waitlist for hostel accommodation”. Otherwise, display “You are
eligible for hostel accommodation”. If the user enters a country other than
India, display “Please visit the International Office.”.


Solution:
```py
cntry = input("Enter your country: ")
if cntry == "India":
    state = input("Enter your state: ")
    if state == "Pune":
        print("You are on the waitlist for hotel accomodation.")
    else:
        print("You are eligible for hostel accomodation.")
else:
    print("Please visit the International Office.")
```
