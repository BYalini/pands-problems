#program that takes a positive floating-point number as input and outputs an approximation of its square root
# using newton's method 
# ref : https://en.wikipedia.org/wiki/Newton%27s_method 
# x(n+1) = xn - f'(xn)/f(xn) where f(x) = x^2-a 

def sqrt(number) : 
    ''' calculates the sqare root of a given positive number to accuracy of 0.001'''
    epsilon = 0.001 # define accuracy of the approximation 
    x = 1
    # loop until the difference between the current estimate and actual sqrt root is less than the required accuracy
    while (abs(x**2-number) > epsilon) :
        x = (x + number / x) * 0.5 # x(n+1) =  (xn + a / xn) / 2 
    return x

number_str = input('Please enter a positive number: ')
number = float(number_str)
sqrt_number = sqrt(number)
print('The square root of {} is approx. {:.1f}.'.format(number,sqrt_number))



