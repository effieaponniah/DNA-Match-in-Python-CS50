# This program was written by Effiea on November 24th 2020
# Last modified December 16th 2020
# This program checks the DNA sequence data from csv file with 
# people and dna data from csv file to identify the person
from sys import argv
from cs50 import get_string

# Find maximum number of occurances of a dna pattern in the dna sequence string
# from csv file
def maximum_occurances(dna_seq, dna_pattern):
    temp_dna_pattern = [0] * len(dna_seq)
    # print(len(dna_seq))
    # print(dna_pattern)
    for x in range(len(dna_seq) - len(dna_pattern), -1, -1):
        # print(x)
        if dna_seq[x: x + len(dna_pattern)] == dna_pattern:
            if x + len(dna_pattern) > len(dna_seq) - 1:
                temp_dna_pattern[x] = 1
            else:
                temp_dna_pattern[x] = 1 + temp_dna_pattern[x + len(dna_pattern)]
    return max(temp_dna_pattern)

# Main program to read both dna persons along with pattern and dns sequence file
# match the dna pattern and print the person name or 'No match' if not found
def main():

    person_dict = {}; 
    matched_dna_patterns = []; 

    if len(argv) != 3: 
        print("Error")
        exit(1)

    csv_file = open(argv[1], 'r')
    for data_row, row in enumerate(csv_file):
        # 1st row in persons file - read header DNA pattern values
        rows = row.strip().split(',')
        # ignore the first value 'name' and capture the rest of DNA patterns
        if (data_row == 0):
            dna_patterns = rows[1:]
        else:
            person_dict[rows[0]] = [int(dna_counts) for dna_counts in rows[1:]]
        
    #print(dna_patterns)
    #print(person_dict)
    
    # Read the sample DNA sequence file to check repeated patterns
    dna_sequence = open(argv[2], 'r').read()
    # print(dna_sequence)
    
    # Iterate through the dna patterns that we captured from the persons database to check
    # in sample dna sequence file that was provided
    # get maximum number of occurances of dna pattern to check against the persons database
    for i in range(len(dna_patterns)):
        matched_dna_patterns.append(maximum_occurances(dna_sequence, dna_patterns[i]))
        
    #print(matched_dna_patterns)
    # Check matched dna patterns with the persons dictonary to see whether we have a match
    for name, data in person_dict.items():
        #print(data)
        if data == matched_dna_patterns:
            print(name)
            exit(0)
    
    print('No match')

# Call to Main program
main()

