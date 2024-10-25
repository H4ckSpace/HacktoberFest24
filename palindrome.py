'''
Question :
You are given a number. Check if it is palindrome or not.

A palindrome is a sequence of characters (like numbers or letters) that reads the same forwards and backwards. For Example: "121" and "radar" are palindromes because they remain the same if you reverse them.

User Task:
This is a function problem. You don't have to take any input. You are required to complete the function isPalindrome() that takes a positive integer N as a parameter and returns True if the number is a palindrome, otherwise returns False.


Input
First Line will contain a positive integer N .
No need to use input() for taking input. It's already done by checker.

Output
Return True if the number is a palindrome, otherwise return False.
No need to use print() for printing output. It's already done by checker

Solution:
'''
def reverse_number(N):
    reversed_num=0
    temp=N 
    while temp>0:
        last_digit=temp%10
        temp = temp//10
        reversed_num=reversed_num*10+last_digit
    return reversed_num

def isPalindrome(N):
    return (N==reverse_number(N))