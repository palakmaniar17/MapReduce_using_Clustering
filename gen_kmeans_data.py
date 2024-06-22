#!/usr/bin/python
import random

random.seed(2116147)

#Generate 2M 5-dimensional data points with random values between 0 and 1.
k_meansData = [[random.random() for column in range(5)] for row in range(2000000)]

#Output the data file
with open('kmeans_data.csv', 'w') as f:
    for row in k_meansData:
        f.write(','.join(map(str, row)) + '\n')
