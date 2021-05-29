''' Program for Sum of the digits of a given number
Difficulty Level : Easy
Last Updated : 30 Apr, 2021
Given a number, find sum of its digits.

Examples : 

Input : n = 687
Output : 21

Input : n = 12
Output : 3
'''

a = str(input())
b = 0
for i in a :
    b += int(i)

print(b)


'''
Python program to check if a string is palindrome or not
Difficulty Level : Easy
Last Updated : 15 Feb, 2021
Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

Examples: 

Input : malayalam
Output : Yes

Input : geeks
Output : No

'''
a = str(input())

b = a[::-1]

if a == b :
    print('yes')
else:
    print('no')