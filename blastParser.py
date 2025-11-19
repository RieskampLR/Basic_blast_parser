#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
blastParser.py

Description:
This program searches a blastp file for query results and stores them with
corresponding targets, e-values, identities, and scores to an output file.
Queries without a hit are included (corresponding value fields are left empty).


User-defined functions: None
Non-standard modules: None

Procedure:
    1. Check if optional output file name is given.
    2. Iteration over the blastp file, searching for the required info by keywords.
       Results are stored to a matrix.
    3. Setting the header for the output file.
    4. Writing the header and matrix to the output file.
    

Input: blastp file, name of output file (optional)
Output: output file

Usage: blastParser.py yourblastpfile.blastp youroutputfile.txt

Version: 1.00
Date: 2025-01-28
Author: Lea Rachel Rieskamp

"""



# Imports:

import sys
from pathlib import Path



# Assigning inputs to variables:

closedblastfile = Path(sys.argv[1])

if len(sys.argv) > 2:                       # Optional output file
    closedoutfile = Path(sys.argv[2])
else:
    closedoutfile = "./output.txt"



# Search blast file for required info and store to matrix:

myblastmatrix = []

with open (closedblastfile, "r") as blastfile:
    for line in blastfile:
        if "Query=" in line:                            # Find Query
            words = line.split()
            ID = words[1]
        if "No hits" in line:                           # If no hit
             rowvector = [ID,"","","",""]               # Empty strings added
             myblastmatrix.append(rowvector)
             continue                                   # Find next Query
        if ">" in line:                                 # If target hit
            target = line[1:-1] # removes > and \n
        if "Score =" in line:
            words = line.split()            
            score = words[2]                            # Corresponding Score
            evalue = words[7][:-1] # removes comma      # E-value,
        if "Identities" in line:                        # and Identity
            words = line.split()
            identity = words[3][1:-3] # removes brackets, %, and comma
            rowvector = [ID,target,evalue,identity,score]
            myblastmatrix.append(rowvector)



# Header:
header = "#query\ttarget\te-value\tidentity(%)\tscore"


# Write header and matrix to output file:

with open (closedoutfile, "w") as outputfile:
    outputfile.write(header + "\n")
    for i in myblastmatrix:
        outputfile.write("\t".join(i) + "\n")




