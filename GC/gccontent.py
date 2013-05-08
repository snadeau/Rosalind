#Scott Nadeau
#Rosalind
#Computing GC Content

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
            sequences.append(current_line[1:])
            new_sequence = ''
        else:
            new_sequence += line.strip()

    sequences.append(new_sequence)
    return sequences


def determine_highest_GC_sequence(sequence_list):
    """
    Input list containing alternating ID "Rosalind_xxxx" and DNA sequence
    ID precedes the associated sequence
    Calculate GC content of each sequence in the list and prints sequence ID
    and GC content of the highest
    """
    highest_gc = 0
    highest_gc_index = 0
    for x in range(1, len(sequence_list), 2):
        current_string = sequence_list[x]
        gc_num = 0
        total_num = 0
        for i in range(len(current_string)):
            if current_string[i] == 'G' or current_string[i] == 'C':
                gc_num += 1
                total_num += 1
            else:
                total_num += 1
                
        if (round((float(gc_num)/total_num * 100), 6)) > highest_gc:
            highest_gc = round((float(gc_num)/total_num * 100), 6)
            highest_gc_index = x-1

    print sequence_list[highest_gc_index]
    print highest_gc
        
        


input_file = open("rosalind_gc.txt", 'r')


determine_highest_GC_sequence(process_FASTA_sequences(input_file))
