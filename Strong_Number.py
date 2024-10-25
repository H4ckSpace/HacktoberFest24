'''
Question:
Given a number n, determine whether it qualifies as a Strong Number or not.

A Strong Number is defined as a number where the sum of the factorials of its digits equals the original number itself.
Factorials is the product of all positive integers up to a given number x.
You need to return 1 if the given number is Strong number, otherwise 0.

Note:- This is a functional problem. You do not need to take any input. You just need to complete the function and just return 1 or 0 accordingly.

Input
First line contains an Integer n.

Output
Print 1 if n is a Strong Number, otherwise print 0.

Example

Input
145
Output
1

Explanation
1! + 4! + 5! = 145 So, 145 is a Strong
Number and therefore the Output 1.

Solution:
'''
def is_strong_number(n):
    num=n
    fact=1
    sum=0
    while num>0:
        x=num%10
        fact=1
        for i in range(1,x+1):
            fact=fact*i
        sum+=fact    
        num=num//10
    if sum==n:
        return 1
    else:
        return 0