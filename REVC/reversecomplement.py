#Scott Nadeau
#Rosalind
#Complementing a Strand of DNA

def process_sequence_file(file):

    sequence = file.readline()
    return sequence

def reverse_complement(dna_sequence):
    """
    Input a string containing DNA nucleotide sequence
    Write the reverse complement of the input sequence to 'output.txt'
    """

    rev_complement = ''
    x = len(dna_sequence)-1

    while x > -1:
        if (dna_sequence[x] == 'A'):
            rev_complement += 'T'
        elif (dna_sequence[x] == 'T'):
            rev_complement += 'A'
        elif (dna_sequence[x] == 'G'):
            rev_complement += 'C'
        elif (dna_sequence[x] == 'C'):
            rev_complement += 'G'

        x -= 1

    output = open('output.txt', 'w')
    output.write(rev_complement)

input = open('rosalind_revc.txt', 'r')
reverse_complement(process_sequence_file(input))
