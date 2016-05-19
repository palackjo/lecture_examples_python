# setl_to_python
Translating SetlX programs to Python

The intention of this project is to tranlate SetlX programs of Prof. Dr. Karl Stroetmanns lecture notes into Python.
The main goal is to maintain the elegance of the algorithms.
The directory Python contains the actual translation of SetlX programs to Python scripts.

*Please note that the structure of this project has been modified. All Python scripts are now in the Python directory.*
This modification has been made to manage the version of the lecture directory more easily.

# New dependancy
To run the lecture scripts the version 1.4.4 of the python package _sortedcontainers_ needs to be installed. It might be directly installed from pip.

## lecture
Lecture represents the python package containing helper functions and classes, to manage and support special setlX features that are not given in python

## Python
### diff.py
tested and working

### find_path.py
tested and working

### fixpoint.py
tested and working

### from.py
tested and working

### function.py
tested and working

### legendre.py
tested and working

### min_sort.py
tested and working

### path.py
tested and working

### path_cyclic.py
tested and working

### poker_triple_lists.py
tested and working

### prime_sieve.py
tested and working

### prime_slim.py
tested and working

### primes_eratosthenes.py
tested and working

### primes_for.py
tested and working

### primes_forall.py
tested and working

### primes_tuple.py
tested and working

### primes_while.py
tested and working

### puzzle.py
tested and working

### simple.py
tested and working

### simple_tupele.py
tested and working

### solve.py
tested and working

### sort.py
tested and working

### stops.py
tested and working

### sum.py
tested and working

### sum_recursive.py
tested and working

### switch.py
tested and working

### davis_putman.py
tested and working

### queens.py
tested and working
_attention! do not raise the number of queens to be calculated, the calculation might take too long_

### transitive_closure.py
tested and working

### watson.py
tested and working

### wolf_goat_cabbage.py
tested and working


## Testing 
This directory contains a script to test the existing Python scripts in the "Python" directory.

The subdirectory "test_results" contains the results of the single scripts. 
These are needed to be able to compare the actual results with desired results. 
The actual results of an execution of each script are in that subdirectory. 
The testing script can be used by giving it the parameter "create" or "compare".


## Documentation
There are two versions of the documentation. A tex-version can be found in this directory, whilst there also is a word-version which can be found beneath the directory in "Word_Files". Both versions also have a pdf-output, which is oftenly updated. It might be that the word-version is a bit newer than the tex-version, because the word file is also used as a draft.