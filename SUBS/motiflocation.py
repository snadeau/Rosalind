#Scott Nadeau
#Rosalind
#Finding a Motif in DNA

input = open('rosalind_subs.txt', 'r')

dna_seq = input.readline().strip()
motif = input.readline().strip()

motif_locations = []

for x in range(0, len(dna_seq)-len(motif)):
    if (dna_seq[x:x+len(motif)] == motif):
        motif_locations.append(x+1)


for x in range(len(motif_locations)):
    print motif_locations[x],

