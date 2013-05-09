#Scott Nadeau
#Rosalind
#Translating RNA into Protein

input = open('rosalind_prot.txt', 'r')

rna_seq = input.readline().strip()
prot_seq = ''

for x in range(0, len(rna_seq), 3):
    codon = rna_seq[x:x+3]
    if (codon == 'AUG'):
        prot_seq += 'M'
    elif (codon == 'UUU' or codon == 'UUC'):
        prot_seq += 'F'
    elif (codon == 'UUA' or codon == 'UUG'):
        prot_seq += 'L'
    elif (codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG'):
        prot_seq +='S'
    elif (codon == 'UAU' or codon == 'UAC'):
        prot_seq += 'Y'
    elif (codon == 'UAA' or codon == 'UAG' or codon == 'UGA'):
        break
    elif (codon == 'UGU' or codon == 'UGC'):
        prot_seq += 'C'
    elif (codon == 'UGG'):
        prot_seq += 'W'
    elif (codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG'):
        prot_seq += 'L'
    elif (codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG'):
        prot_seq += 'P'
    elif (codon == 'CAU' or codon == 'CAC'):
        prot_seq += 'H'
    elif (codon == 'CAA' or codon == 'CAG'):
        prot_seq += 'Q'
    elif (codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'CGU'):
        prot_seq += 'R'
    elif (codon == 'AUU' or codon == 'AUC' or codon == 'AUA'):
        prot_seq += 'I'
    elif (codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG'):
        prot_seq += 'T'
    elif (codon == 'AAU' or codon == 'AAC'):
        prot_seq += 'N'
    elif (codon == 'AAA' or codon == 'AAG'):
        prot_seq += 'K'
    elif (codon == 'AGU' or codon == 'AGC'):
        prot_seq += 'S'
    elif (codon == 'AGA' or codon == 'AGG'):
        prot_seq += 'R'
    elif (codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG'):
        prot_seq += 'V'
    elif (codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG'):
        prot_seq += 'A'
    elif (codon == 'GAU' or codon == 'GAC'):
        prot_seq += 'D'
    elif (codon == 'GAA' or codon == 'GAG'):
        prot_seq += 'E'
    elif (codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG'):
        prot_seq += 'G'

print prot_seq
