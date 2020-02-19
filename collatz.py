# Weekly task 4
# This program prompts the user for an integer input and prints out the hailstone sequence
# Collatz conjecture : Regardless of the starting of a postive integer n , the the sequence will always reach 1
# Proposed by German mathematician Lothar Collatz is 1937. No mathematical proof exists
# f(n) = n /2 if n is even
#      = 3n+1 if n is odd
# The program will stop if the current value is 1 
# Ref:https://en.wikipedia.org/wiki/Collatz_conjecture

n = int(input("Please enter a positive integer: "))

if n < 1:
    print("Please try again with a positive integer greater than 1")
else :
    print(n, end = " ")  

while n > 1:  
    if n % 2 == 0: 
        n = n/2
    else: # n is odd and greater than 1
        n = (n * 3) + 1
    print(int(n), end = " ") #print next number in sequence

