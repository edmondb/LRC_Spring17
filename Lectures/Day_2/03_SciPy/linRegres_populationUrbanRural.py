#!/usr/bin/env python
'''
    We analyze the percentages of US urban & rural population since 1790.
    We calculate a linear regression model and plot the data
    
'''

#-------------
# Load modules
#-------------
from scipy import stats
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


def predict_line(x, m, b):
    '''
      Compute: y = mx + b
    '''
    return m*x+b

#--------------
# Read the data
#--------------
fName = 'populationUS.txt'
data = np.genfromtxt(fName, skip_header=6, usecols=(0,4, 5))

x = data[:,0] # Year
y = data[:,1] # Urban percentage
z = data[:,2] # Rural percentage

#--------------------------------
# Determine the linear Regressions
#--------------------------------
m1, b1, r1, p1, m1_std_error = stats.linregress(x, y) # urban
m2, b2, r2, p2, m2_std_error = stats.linregress(x, z) # rural

# Calculate some additional outputs
predict_y1 = predict_line(x, m1, b1)
predict_y2 = predict_line(x, m2, b2)

f = lambda x: m1*x + b1
g = lambda x: m2*x + b2
h = lambda x: f(x) - g(x)

x_int = optimize.fsolve(h, 1.0)
y_int = f(x_int)

print x_int, y_int


#---------
# Plotting
#---------
plt.plot(x, y, 'o', label='original urban')
plt.plot(x, z, 'd', label='original rural')
plt.plot(x, f(x), 'r-', label='Urban Line')
plt.plot(x, g(x), 'g-', label='Rural Line')
plt.scatter(x_int, y_int, marker='x', s=150, zorder=2, 
            linewidth=2, color='black')
plt.legend(loc='center left')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Percentage of US Urban & Rural Population over Time')
plt.show()
