
#!/usr/bin/env python3

import sys

# Load Bloom filter from file
bloom_filter_file = '/home/ec2-user/bloom_filter.txt'

with open(bloom_filter_file, 'r') as f:
    bloom_filter_str = f.read().strip()

# Convert the binary string to a list of integers (0 or 1)
bloom_filter = [int(bit) for bit in bloom_filter_str]

# Check if any value in the Bloom filter is 1
#if 1 in bloom_filter:
#    print("At least one value is set as 1 in the Bloom filter.")
#else:
#    print("No value is set as 1 in the Bloom filter.")

index = None  # Define index outside the loop

for line in sys.stdin:
    data = line.strip().split('|')
    if len(data) <= 17:
        continue

    if data[1].isdigit():  # Assuming if the first column is an integer, it's from lineorder table
        lo_orderdate_index = 5
        lo_orderdate = int(data[lo_orderdate_index])

        # Check if lo_orderdate exists in the Bloom filter
        index = lo_orderdate % len(bloom_filter)
        if bloom_filter[index] == 1:
            # Emit data with identifiers for join result
            print(f"{line.strip()}")
        #else:
            #print(f"NotBloom_lineorder|{line.strip()}")  # Debugging print

    else:  # If the first column is not an integer, assume it's from dwdate table
        d_sellingseason_index = 12
        d_sellingseason = data[d_sellingseason_index]

        # Check if the selling season is 'Fall'
        if d_sellingseason == 'Fall':
            # Emit data with identifiers for join result
            print(f"{line.strip()}")

#print(f"Final index: {index}")  # This will print the last value of index after the loop ends
