#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 13:05:18 2018

@author: hassan.naseri
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:32:01 2018

@author: hassan.naseri
"""

import numpy as np
import pandas as pd

# This is the number of bits used to address the dataset
# In our example, the shelf number of a fruit is a 4 bit unsigned integer.
NBITS = 4;


def uint4(int_or_string):
    # Simulate 4-bit unsigned integer by masking 4 bits of numpy.unit8
    unit8_type = np.uint8(int_or_string)
    mask = np.uint8(2**4 - 1)
    return(unit8_type & mask)

fileurl = "https://raw.githubusercontent.com/HassanNaseri/quantum-computing-handson/master/fruits.csv"
data_frame = pd.read_csv(fileurl)

def black_box_check(key, value):
    # Black box function to encode a winner entry in a dataset
    # Returns inverse (NOT) of 'value' arguments if 'key' and 'value' pair match,
    # otherwise it returns the 'value' argument unchanged.
    # Note: this function is not implemented efficiently, but its details are not importnat!
    data_dict = data_frame.set_index('name').T.to_dict('records')[0]
    try:
        winner = uint4(data_dict[key])
    except:
        raise ValueError('Invalid key! There is no ' + key)
    result = value
    if value == winner:
        result = ~value
    return result


###############################################################################
# The main body code starts here

# The name of fruit to search for its shelf number: 
# Options: avocado, apple, banana, grape, apricot, peach, cherry, orange, 
# blueberry, pear, pineapple, mandarin, mango, raspberry, strawberry, kiwi
fruit_to_find = 'apple'

# >>>>>>>> Complete the follwing line:
maximum_number_of_steps = 2**NBITS
step_counter = 0
for i in range(maximum_number_of_steps):
    shelf = uint4(i)
    step_counter += 1
    if black_box_check(fruit_to_find, shelf) == ~shelf:
        break;

print("I found '{:}'! The shlef number is: {:}".format(fruit_to_find, shelf))
print("Number of iterations: ", step_counter)    
print("")


# We can also search in any random order, but the average number of iteartions 
# will be same .
# random_indices = np.random.permutation(np.arange(maximum_number_of_steps))


