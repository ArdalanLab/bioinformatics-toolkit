# Find every occurrence of a user-given codon in a DNA sequence
dna = input("Enter your sequence: ").lower()
codon = input("Enter the codon to find (3 letters): ").lower()

for i in range(len(dna) - 2):
    if dna[i:i+3] == codon:
        print(f"'{codon}' found at position {i}")