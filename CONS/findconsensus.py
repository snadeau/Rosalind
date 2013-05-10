#Scott Nadeau
#Rosalind
#Consensus and Profiles

def process_FASTA_sequences(file):
    """
    Input file containing <= 10 DNA sequences in FASTA format (<= 1kbp)
    Returns a list with alternating ID "Rosalind_xxxx" and DNA sequence
    ID precedes the associated sequence
    """
    new_sequence = ''
    sequences = []
    for line in file:
        current_line = line.strip()
        if current_line[0] == '>':
            if new_sequence != '':
                sequences.append(new_sequence)
            new_sequence = ''
        else:
            new_sequence += line.strip()

    sequences.append(new_sequence)
    return sequences


def generate_counts_dictionary(sequences):
    """
    Input array of DNA sequences
    Calculate frequency of each base at each position in each
    respective sequence
    Return dictionary of arrays of counts of each base at each position
    """
    seq_len = len(sequences[0])

    counts_A = [0] * seq_len
    counts_C = [0] * seq_len
    counts_G = [0] * seq_len
    counts_T = [0] * seq_len

    counts = {'A': counts_A, 'C': counts_C, 'G': counts_G, 'T': counts_T}

    for x in range(len(sequences)):
        for i in range(seq_len):
            if sequences[x][i] == 'A':
                counts_A[i] += 1
            elif sequences[x][i] == 'C':
                counts_C[i] += 1
            elif sequences[x][i] == 'G':
                counts_G[i] += 1
            elif sequences[x][i] == 'T':
                counts_T[i] += 1
            else:
                print "Invalid base"

    return counts

def print_formatted_matrix(base_counts):
    """
    Input dictionary containing arrays of counts of base pairs
    at each position of a group of DNA sequences
    Print the formatted arrays in matrix format
    """
    length = len(base_counts['A'])
    print "A:",
    for x in xrange(length):
        print base_counts['A'][x],
    print
    print "C:",
    for x in xrange(length):
        print base_counts['C'][x],
    print
    print "G:",
    for x in xrange(length):
        print base_counts['G'][x],
    print
    print "T:",
    for x in xrange(length):
        print base_counts['T'][x],
    print

    
def find_consensus_sequence(base_counts):
    """
    Input dictionary containing arrays of counts of base pairs
    at each position of a group of DNA sequences
    Calculate consensus sequence using counts and return consensus
    """
    consensus = ''
    for x in range(len(base_counts['A'])):
        max_count = base_counts['A'][x]
        new_base = 'A'
        if max_count < base_counts['C'][x]:
            max_count = base_counts['C'][x]
            new_base = 'C'
        if max_count < base_counts['G'][x]:
            max_count = base_counts['G'][x]
            new_base = 'G'
        if max_count < base_counts['T'][x]:
            new_base = 'T'
        consensus += new_base
    return consensus


input = open('rosalind_cons.txt', 'r')

sequences_list = process_FASTA_sequences(input)

counts_dictionary = generate_counts_dictionary(sequences_list)
print find_consensus_sequence(counts_dictionary)    
print_formatted_matrix(counts_dictionary)
