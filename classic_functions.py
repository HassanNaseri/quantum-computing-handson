import numpy as np
import pandas as pd

def uint4(int_or_string):
    # Simulate 4-bit unsigned integer by masking 4 bits of numpy.unit8
    unit8_type = np.uint8(int_or_string)
    mask = np.uint8(2**4 - 1)
    return(unit8_type & mask)

def black_box_check(key, value):
    # Black box function to encode a winner entry in a dataset
    # Returns inverse (NOT) of 'value' arguments if 'key' and 'value' pair match,
    # otherwise it returns the 'value' argument unchanged.
    # Note: this function is not implemented efficiently, but its details are not importnat!
    data_frame = pd.read_csv("fruits4.csv")
    data_dict = data_frame.set_index('name').T.to_dict('records')[0]
    try:
        winner = uint4(data_dict[key])
    except:
        raise ValueError('Invalid key! There is no ' + key)
    result = value
    if value == winner:
        result = ~value
    return result
