# Quantum Computing Handson Workshop
Quantum computing has the promise of outperforming every classical computer to an extraordinary degree for certain tasks. It stands to change the world by solving problems that are intractable with today's technology, hence it will likely disrupt every industry in near future. The goal of this handson session is to provide a technical introduction to quantum computing for software developers and technology architects. We will focus on gate-model quantum computer architecture and Qiskit development kit to solve a simple problem. We will implement the Grover's search algorithm together, and run it on an IBM quantum backend. Through the exercises you will see the nuts and bolts of quantum computing and why it can make a big difference. 

These exercise are a collection of python scripts as IPython notebook files. A pre-configured online environment (Jupyter Notebook) is prepared to run the exercises. The link to the online Jupyter Notebook in Binder can be found at the bottom of the page. 

If you want to run the exercises on your own computer, you will need a working Python environment with required Python modules are **numpy**, **pandas** and **qiskit**. These can be installed using pip. An easy option to setup a new Python environment with all the tools (including Jupyter Notebook) is to download and install Anaconda (https://www.anaconda.com/download/). You can install Qiskit using Anaconda package manager or using 'pip install qiskit'. Moreover, you may signup to IBM Q Experince (https://quantumexperience.ng.bluemix.net/qx/signup) and receive you API tocken (https://quantumexperience.ng.bluemix.net/qx/account/advanced). The API tocken is necessary to configure Qiskit to connecet to IBM Q backend and run your code on an actual quantum computer.

PowerPoint slides of the workshop are in this file:
**[Quantum_Computing_Handson_2019.pdf](documentation/Quantum_Computing_Handson_2019.pdf)**

# Simple Exercises for Quantum Computing
This repository contains Jupyter Notebook files to start expremineting with gate-model quantum computers. The excersises are based on **qiskit** SDK, and are only tested on IBM Q quantum backends.

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


