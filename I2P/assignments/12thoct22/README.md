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
1. Take number from user via `input()`
2. Seperate number into it's digits by casting it to a `list`
3. Convert each digit to an `int`, take it's cube and add them
4. Convert input number to an `int` and compare with the number in Step 3
5. Print result

Solution: 
```py
num = input("Enter a 3-digit number: ")
digits = list(num)

lhs = int(digits[0])**3 + int(digits[1])**3 + int(digits[2])**3
rhs = int(num)

if lhs == rhs:
    result = "is"
else:
    result = "is not"

print(num, result, "an Armstrong number!")
```


[Q2]

Accept the user’s nationality (country). If the user enters “India”, ask the
them to enter their state. If the user enters “Pune”, display “You are on
the waitlist for hostel accommodation”. Otherwise, display “You are
eligible for hostel accommodation”. If the user enters a country other than
India, display “Please visit the International Office.”.


Solution:
```py
country = input("Enter your country: ")
if country == "India":
    city = input("Enter your city: ")
    if city == "Pune":
        print("You are on the waitlist for hotel accomodation.")
    else:
        print("You are eligible for hostel accomodation.")
else:
    print("Please visit the International Office.")
```
