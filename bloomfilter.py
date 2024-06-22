
#!/usr/bin/env python3

import hashlib

def hash_function(depaulid, number, i):
    hash_value = hashlib.sha256(f"{depaulid} {number} {i}".encode()).hexdigest()
    return hash_value

def set_bloom_filter_slots(depaulid, numbers):

    bloom_filter = [0] * 256000  # Initialize Bloom filter with 256000 slots
    for number in numbers:

        hash_value = hash_function(depaulid, number, 0)
        for i in range(6):  # Use the first 6 positions of the hash value for 6 hash functions
            index = int(hash_value[i], 16) % 256000
            bloom_filter[index] = 1  # Set the corresponding bit to 1
    return bloom_filter

def check_bloom_filter(depaulid, number, bloom_filter):
    for i in range(6):  # Using the first 6 positions in the hash_value
        hash_value = hash_function(depaulid, number, i)
        index = int(hash_value[i], 16)
        if bloom_filter[index] == 0:
            return False  # Definitely not in the Bloom filter
    return True  # Possibly in the Bloom filter (or a false positive)

depaulid = 'pmaniar1'

lineorder_numbers = []

lineorder_file_path = 'lineorder.tbl'
with open(lineorder_file_path, 'r') as file:
    for line in file:
        data = line.strip().split('|')
        if len(data) > 0:
            lineorder_numbers.append(int(data[0]))


bloom_filter = set_bloom_filter_slots(depaulid, lineorder_numbers)
indexes_of_ones = [str(i) for i, val in enumerate(bloom_filter) if val == 1]
print(f"{','.join(indexes_of_ones)} bits have been set \n")

with open('bloom_filter.txt', 'w') as f:
  for val in bloom_filter:
    f.write(str(val))

# Testing hash functions with DePaulID 'pmaniar1' and number 10000
for i in range(6):
    hash_value = hash_function('pmaniar1', 10000, i)
    index = int(hash_value[i], 16)
    print(f"Hash Value {i}: {hash_value}, Index: {index}, Bit Value: {bloom_filter[index]}")
