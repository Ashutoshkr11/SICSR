"""
Q1)
Accept a number from the user. Assume that the user enters a 3-digit
number. Check whether it is an Armstrong number by using string to
list/tuple conversion.
Notes:
i. A 3-digit Armstrong number is a number that is equal to the cube of its
    digits.
ii. To access an element of a list/tuple, use its index as follows:
    list_name[0] will refer to the first element.
"""


num = input("Enter a 3-digit number: ")
digits = list(num)

lhs = int(digits[0])**3 + int(digits[1])**3 + int(digits[2])**3
rhs = int(num)

if lhs == rhs:
    result = "is"
else:
    result = "is not"

print(num, result, "an Armstrong number!")