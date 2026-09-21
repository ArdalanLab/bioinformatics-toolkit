# Count codons from a DNA sequence stored in a text file

filename = input("Enter the file name: ")

with open(filename, "r") as f:
    dna = f.read().strip().upper()

bases = ['A', 'T', 'C', 'G']

codon_counts = {}
for i in bases:
    for j in bases:
        for k in bases:
            codon = i + j + k
            codon_counts[codon] = dna.count(codon)

for codon, count in codon_counts.items():
    if count:
        print(f"{codon}: {count}")
move codon_position.py into sequence_analysis/
