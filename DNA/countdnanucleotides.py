#Scott Nadeau
#2013-04-26
#Rosalind
#Counting DNA Nucleotides

def process_sequence_file(file):

    sequence = file.readline()
    return sequence

def print_num_dna_nucleotides(dna_sequence):
    """
    Input a string containing DNA nucleotide sequence
    Count and print the number of respective 'A', 'C', 'G', and 'T'
    present in the sequence
    """

    num_A = 0
    num_C = 0
    num_G = 0
    num_T = 0

    index = 0

    while index < len(dna_sequence):
        if(dna_sequence[index] == 'A'):
            num_A += 1
        elif(dna_sequence[index] == 'C'):
            num_C += 1
        elif(dna_sequence[index] == 'G'):
            num_G += 1
        elif(dna_sequence[index] == 'T'):
            num_T += 1
        else:
            print "Invalid base found", dna_sequence[index], str(index)
        index += 1

    print str(num_A) + ' ' + str(num_C) + ' ' + str(num_G) + ' ' + str(num_T)

f = open('rosalind_dna.txt', 'r')

print_num_dna_nucleotides(process_sequence_file(f))
