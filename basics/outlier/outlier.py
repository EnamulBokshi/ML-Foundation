import numpy as np
import pandas as pd

data = [-100, 1,2,3,4,5,6,7,8,9,12,14,15,20,23,100]
q1 = np.percentile(data, 25)

q3 = np.percentile(data, 75)

iqr = q3-q1

lowerBound = q1 - 1.5 * iqr
upperBound = q3 + 1.5 * iqr
print("Q1: ",q1)
print("Q2: ", q3)

print("Lower Bound: ",lowerBound)

print("Upper Bound: ",upperBound)
