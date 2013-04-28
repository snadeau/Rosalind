#Scott Nadeau
#Rosalind
#Transcribe DNA into RNA

def process_sequence_file(file):

    sequence = file.readline()
    return sequence

def transcribe_dna_to_rna(dna_sequence):
    """
    Input a string containing DNA nucleotide sequence
    Return the transcribed RNA string
    """

    rna_sequence = ''
    x = 0
    while x < len(dna_sequence):
        if(dna_sequence[x] == 'T'):
            rna_sequence += 'U'
        else:
            rna_sequence += dna_sequence[x]
        x += 1

    return rna_sequence

f = open('rosalind_rna.txt', 'r')

print transcribe_dna_to_rna(process_sequence_file(f))
