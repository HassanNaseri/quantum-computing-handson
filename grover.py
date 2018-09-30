#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:32:01 2018

@author: hassan.naseri
"""

from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, execute



def black_box_check(circuit, q):
    # black box function to encode a winner entry
    w = 1 # possible winners: 0,1,2,3
    print("hidden winner: {0:#b}".format(w))
    if w&2 == 0:
        circuit.s(q[0])
    if w&1 == 0:
        circuit.s(q[1])
    circuit.h(q[1])
    circuit.cx(q[0], q[1])
    circuit.h(q[1])
    if w&2 == 0:
        circuit.s(q[0])
    if w&1 == 0:
        circuit.s(q[1])


def reflection_about_average(circuit, q):
    # Reflection about average for amplitude amplification
    circuit.h(q[0])
    circuit.h(q[1])    
    circuit.x(q[0])
    circuit.x(q[1])
    circuit.h(q[1])
    circuit.cx(q[0], q[1])
    circuit.h(q[1])
    circuit.x(q[0])
    circuit.x(q[1])
    circuit.h(q[0])
    circuit.h(q[1])
 
# Define reqisters and circuit
qreg = QuantumRegister(2)
creg = ClassicalRegister(2)
grover = QuantumCircuit(qreg, creg)

# Initialization of quantum registers
grover.h(qreg[0])
grover.h(qreg[1])

# Grover's amplitude amplification (only one iteration here)
black_box_check(grover, qreg)
reflection_about_average(grover, qreg)

# Add Measurement
grover.measure(qreg, creg)

# Execute and collect results
job_sim = execute(grover, "local_qasm_simulator")
sim_result = job_sim.result()

# Print result counts
print("simulation: ", sim_result)
print(sim_result.get_counts(grover))


