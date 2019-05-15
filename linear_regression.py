import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from matplotlib import style
style.use('seaborn')

x_values = np.array([1,2,3,4,5,6,7,8,9,30], dtype=np.float64)
y_values = np.array([1,4,1,16,4,1,4,6,10,8], dtype=np.float64)


def best_fit_line(x_values,y_values):
    m = (((mean(x_values)*mean(y_values)) - mean(x_values*y_values)) /
         ((mean(x_values)*mean(x_values)) - mean(x_values*x_values)))

    b = mean(y_values) - m*mean(x_values)

    return m, b


# establish best fit line
m, b = best_fit_line(x_values, y_values)

# establish regression line
print("regression line: " + "y = " + str(round(m,2)) + "x + " + str(round(b,2)) )

# linear regression prediction model
x_prediction = 18
y_prediction = (m*x_prediction)+b
print("predicted coordinate: (" + str(round(x_prediction,2)) + ", " + str(round(y_prediction,2)) + ")")

# find the r squared value
# y values of regression line
regression_line = [(m*x)+b for x in x_values]


def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig) * (ys_line - ys_orig)) # helper function to return the sum of the distances between the two y values squared


def r_squared_value(ys_orig,ys_line):
    squared_error_regr = squared_error(ys_orig, ys_line) # squared error of regression line
    y_mean_line = [mean(ys_orig) for y in ys_orig] # horizontal line (mean of y values)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line) # squared error of the y mean line
    return 1 - (squared_error_regr/squared_error_y_mean)


r_squared = r_squared_value(y_values, regression_line)
print("r^2 value: " + str(r_squared))

# plot the values on a graph
plt.title('Linear Regression')
plt.scatter(x_values, y_values,color='#5b9dff',label='data')
plt.scatter(x_prediction, y_prediction, color='#fc003f', label="predicted")
plt.plot(x_values, regression_line, color='000000', label='regression line')
plt.legend(loc=4)
plt.savefig("graph.png")