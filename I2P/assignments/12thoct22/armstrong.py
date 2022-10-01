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


num = input("Enter a number")
nums = list(num)

total = int(nums[0])**3 + int(nums[1])**3 + int(nums[2])**3

if total == int(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
