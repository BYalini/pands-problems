# Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
import matplotlib.pyplot as plt
import numpy as np 

x_values = np.arange(0,4)

plt.plot(x_values, x_values,linestyle='-', marker='o')
plt.title('f(x)=x')
plt.show()

#x^2
plt.plot(x_values, x_values **2,linestyle='-', marker='o')
plt.title('g(x)=x^2')
plt.show()

#x^3
plt.plot(x_values, x_values **3,linestyle='-', marker='o')
plt.title('h(x)=x^3')
plt.show()
