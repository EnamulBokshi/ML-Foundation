import numpy as np
import pandas as pd

data = [6,7,8,8,9,10,10,11,12,13,14,15,16,17,18,19,20]

q1 = np.percentile(data, 25,interpolation = 'midpoint')

q3 = np.percentile(data, 75, interpolation = 'midpoint')

iqr = q3 - q1
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)