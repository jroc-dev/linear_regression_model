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