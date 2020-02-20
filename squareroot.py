#program that takes a positive floating-point number as input and outputs an approximation of its square root.
def sqrt (number) :
    # sqrt(x) is the same as x to the power 1/2
    square_root= number ** 0.5
    return square_root

number_str = input('Please enter a positive number: ')
number = float(number_str)

if number > 0 :
        sqrt_number = sqrt(number)
        # format floating point to one decimal
        print('The square root of {} is approx. {:.1f}.'.format(number,sqrt_number))
else :
        print('Negative number entered')



