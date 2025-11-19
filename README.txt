README

BINP28 course mini-project

Program description:
This program searches a blastp file for query results and stores them with
corresponding targets, e-values, identities, and scores to an output file.
Queries without a hit are included (corresponding value fields are left empty).

Procedure:
    1. Check if optional output file name is given.
    2. Iteration over the blastp file, searching for the required info by keywords.
       Results are stored to a matrix.
    3. Setting the header for the output file.
    4. Writing the header and matrix to the output file.
    
Input: blastp file, name of output file (optional)
Output: output file
Usage: blastParser.py yourblastpfile.blastp youroutputfile.txt
