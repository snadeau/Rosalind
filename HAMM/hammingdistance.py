#Scott Nadeau
#Rosalind
#Counting Point Mutations

input = open('rosalind_hamm.txt', 'r')

string1 = input.readline().strip()
string2 = input.readline().strip()

def calculate_hamming_distance(sequence1, sequence2):
    """
    Input two DNA strings of equal length
    Calculate Hamming distance (number of corresponding bases that differ
    between the two DNA strings)
    """

    hamm = 0
    
    if len(sequence1) != len(sequence2):
        print "Sequences not equal length"
        return

    for i in range(0, len(sequence1)):
        if sequence1[i] != sequence2[i]:
            hamm += 1

    return hamm

print calculate_hamming_distance(string1, string2)
