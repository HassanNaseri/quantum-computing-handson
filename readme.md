# Quantum Computing Handson Workshop
Quantum computing has the promise of outperforming every classical computer to an extraordinary degree for certain tasks. It stands to change the world by solving problems that are intractable with today's technology, hence it will likely disrupt every industry in near future. The goal of this handson session is to provide a technical introduction to quantum computing for software developers and technology architects. We will focus on gate-model quantum computer architecture and Qiskit development kit to solve a simple problem. We will implement the Grover's search algorithm together, and run it on an IBM quantum backend. Through this exercise you will see the nuts and bolts of quantum computing and why it can make a big difference. 

Requirements of the session are as follows. Please bring your own laptop. The exercises are in Python, and an online environment (Jupyter Notebook) is prepared to run the exercises. However, it is recommended to have a working Python environment on your laptop with Qiskit module installed as a fallback solution. An easy option to setup a new Python environment with all the tools (including Jupyter Notebook) is to download and install Anaconda (https://www.anaconda.com/download/). You can install Qiskit using Anaconda package manager or using 'pip install qiskit'. Moreover, you may signup to IBM Q Experince (https://quantumexperience.ng.bluemix.net/qx/signup) and receive you API tocken (https://quantumexperience.ng.bluemix.net/qx/account/advanced). The API tocken is necessary to configure Qiskit to connecet to IBM Q backend and run your code on an actual quantum computer.

Biography: 
Hassan Naseri has received his M.Sc. in Information Technology from University of Turku, Finland, in 2013, and his Ph.D. in Signal Processing Technology from Aalto University, Finland, in 2018.  Years 2007-2010, he worked in Huawei Technologies Co. Ltd. as a telecommunication engineer and a project manager. He was a researcher at the Department of Signal Processing and Acoustics, Aalto University, from 2012 to early 2018. He joined Accenture Liquid Studio, Helsinki in April 2018 to work as an artificial intelligence expert.  Hassan Naseri has more than 10 years of work experience in the ICT sector, with recent projects including integration and optimization of telecommunication software and systems, positioning and synchronization of mobile and IoT devices in a network, imaging and map building for indoor environments using  ad hoc measurements. He was an author of several articles in flagship IEEE journals and conferneces. His areas of expertise inlculde data modeling, statistical signal processing, mathematical optimization, machine learning, Bayesian inference and data fusion. He recently started a resaerch and prototyping project on quantum computing.



%     
He has been with  
%
His current research interests include super-resolution parameter estimation, network synchronization, cooperative localization, and indoor radio imaging.


PowerPoint slides of the workshop are in this file:
**[TechArch_Day_2018_Quantum_Computing_HandsOn.pptx](TechArch_Day_2018_Quantum_Computing_HandsOn.pptx)**

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


