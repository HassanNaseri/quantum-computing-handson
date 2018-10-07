
# Simple Exercises for Quantum Computing
This repository contains Jupyter Notebook files to start expremineting with gate-model quantum computers. The excersises are based on **qiskit** SDK, and are only tested on IBM Q quantum backends.

PowerPoint slides of the workshop are in this file:
**[TechArch_Day_2018_Quantum_Computing_HandsOn.pptx](TechArch_Day_2018_Quantum_Computing_HandsOn.pptx)**

## Let's start with a classic search example
Run **[search_classic.ipynb](search_classic.ipynb)** to review the complexity of an unstructured search problem.

## Qiskit Hello World!
Run **[hello_qiskit.ipynb](hello_qiskit.ipynb)** to start with Qiskit programming.

## Grover's algorithm 
The Grover's algorithm brings quadratic speedup to the problem of unstructured search.

### Overall structure of the lagorithm
Run **[grover_1.ipynb](grover_1.ipynb)** to experminet with Grover's algorithm. The task is to complete the code by calling two functions **black_box_check(circuit, key, q)** and **reflection_about_average(circuit, q)**.

### Building the rotation function
Run **[grover_2.ipynb](grover_2.ipynb)** to experminet with details of Grover's algorithm. The task is to implement the fucntion **reflection_about_average(circuit, q)**.

## Jupyter Notebooks in Binder 
You can find the executable Jupyter Notebook files from the follwing link: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/HassanNaseri/quantum-computing-handson/master)
https://mybinder.org/v2/gh/HassanNaseri/quantum-computing-handson/master




