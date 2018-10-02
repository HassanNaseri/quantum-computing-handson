import numpy as np
import pandas as pd

def uint4(int_or_string):
    # Simulate 4-bit unsigned integer by masking 4 bits of numpy.unit8
    unit8_type = np.uint8(int_or_string)
    mask = np.uint8(2**4 - 1)
    return(unit8_type & mask)

def black_box_check(circuit, key, q):
    # Black box oracle function to encode a winner entry in a dataset
    # Inverts the phase of 'q' if 'key' and 'q' are matching, otherwise the 'q' remains unchanged.
    # Note: the implementation of the oracle here is only for simulation purposes, and its details may noy have 
    # any ptractical relevance. In practice, the oracle is generated systematically for each problem ecncoding 
    # a function (or dataset) that cannot be inverted (or efficiently searched).
    data_frame = pd.read_csv("fruits2.csv")
    data_dict = data_frame.set_index('name').T.to_dict('records')[0]
    try:
        winner = uint4(data_dict[key])
    except:
        raise ValueError('Invalid key! There is no ' + key)
    if winner&2 == 0:
        circuit.s(q[0])
    if winner&1 == 0:
        circuit.s(q[1])
    circuit.h(q[1])
    circuit.cx(q[0], q[1])
    circuit.h(q[1])
    if winner&2 == 0:
        circuit.s(q[0])
    if winner&1 == 0:
        circuit.s(q[1])

def reflection_about_average(circuit, q):
    # Reflection about average for amplitude amplification
    circuit.h(q)   
    circuit.x(q)
    circuit.h(q[1])
    circuit.cx(q[0], q[1])
    circuit.h(q[1])
    circuit.x(q)
    circuit.h(q)

