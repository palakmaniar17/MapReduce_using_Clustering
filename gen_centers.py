#!/usr/bin/python
import random
import csv

#Get the initial cluster centers using random points selection.'''
def clusterCenters(data, k):
    random.seed(2116147)
    return random.sample(data, k)

df = []
with open('kmeans_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        df.append([float(val) for val in row])

kNum = 4

initialCenters = clusterCenters(df, kNum)
with open('centers.txt', 'w') as f:
    for center in initialCenters:
        f.write(','.join(map(str, center)) + '\n')
