#!/usr/bin/python3
import sys
import numpy as np

# Both points and centers are numpy arrays.
current_center = None
new_center = np.zeros((1, 5))
cnt = 0
centers = []

for line in sys.stdin:
    center, *point_values = map(str.strip, line.split(','))
    
    point = np.array(list(map(float, point_values))).reshape(1, 5)
      
    # If current_center is the same as the center of the new line
    if current_center == center:
        # Points for the same center
        new_center += point
        cnt += 1
    else:
        # If this is not the first center
        if current_center is not None:
            # Compute the new center 
            new_center /= cnt
            centers.append(new_center)
            # Resent Counter
            cnt = 1
            new_center = point.copy()
        else:
            # First ever Center 
            cnt = 1
            new_center = point.copy()

        # Update current_center to new center
        current_center = center

# Account for the last key
if current_center is not None:
    new_center /= cnt
    centers.append(new_center)

# Print the computed centers as comma-separated values 
for center in centers:
    print(','.join(map(str, center[0])))
