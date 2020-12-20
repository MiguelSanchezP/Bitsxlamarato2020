# BitsxlaMarato 2020
## Description
The aim of this project is to find whether a symptom or a set of symptoms among a paediatric patient can be conclusive to diagnose or refute SARS-CoV-2. In order to achieve so, a dataset with over 1600 cases has been studied with Python3. It has also been attempted to create the files as comprehensible as possible for a third person willing to make use of the codes. 

## Dependencies 
This project relies strongly on plotting and analysing data, and thus some external libraries had to be imported:
* matplotlib
* numpy

If these are not installed on the system, do NOT expect the program to work
## Structure
All algorithms and files found in this project are capable of working with different datasets or conditions without having to retype a myriad of modifications.
* ### main.py
It is the main file of the project, and it calculates the probability of having SARS-CoV-2 by combining them. By the moment, it is capable of separating between gender, positive and negative diagnosis.
* ### index_dataset.py
This file is a simple python script to retrieve a given field from the dataset and indicate its position. It is necessary as the dictionary provided was not completely precise.
* ### reto2.py
* ### covid-and-sth.py
* ### Files/
Under the directory `Files/` one can expect to find the dataset (extension `.csv`) with over 1600 paediatric patients. 
* ### Output/
Under the directory `Output/` some `.txt` files are stored. These contain the list of probabilities of having SARS-CoV-2 when presenting two different symptoms. There are a total of three files, being `GenderAwareProbabilities.txt` and `GenderUnawareProbabilities.txt` the two files with the whole list of combinations considered.
