# This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axis.
# ref : https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
# ref : https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.xticks.html

import matplotlib.pyplot as plt
import numpy as np 

#define x axis values
x_values = np.arange(0,4)

# plot f(x), g(x) and h(x) on one axis
plt.plot(x_values, x_values,linestyle='-', marker='o', label='f(x)=x')
plt.plot(x_values, x_values**2,linestyle='-', marker='o', label='g(x)=x^2')
plt.plot(x_values, x_values**3,linestyle='-', marker='o', label='h(x)=x^3')
plt.title('function plots')
plt.xticks(np.arange(0, 4, step=1)) # x-axis labels
plt.legend()
plt.show()


