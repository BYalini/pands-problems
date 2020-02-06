#Weekly task 4
#Program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

user_number = input("Enter any positive integer:")
While user_number > 1: 
    if user_number % 2 == 0:
        user_number = user_number/2
    else:
        user_number = (user_number * 3) + 1
    print( user_number)


