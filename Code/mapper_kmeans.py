#!/usr/bin/python3
import sys
import numpy as np

try:  # if centers have been generated
    with open('centers.txt', 'r') as f:
        centers = [np.array(list(map(float, line.strip().split(',')))) for line in f]

except FileNotFoundError:  
    num_centers = 4
    num_dimensions = 4  # Ensure num_dimensions matches the dimensions of each center
    centers = [np.random.rand(num_dimensions) for _ in range(num_centers)]

for line in sys.stdin:
    point = np.array(list(map(float, line.strip().split(','))))
    # Distance
    dist = [np.linalg.norm(point - center) for center in centers]
    # Minimum distance for Kmeans Clustering
    min_distance_id = np.argmin(dist)
    # Center and Point
    print(min_distance_id, *point, sep=', ', end='\n')
