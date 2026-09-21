#Analyze codon usage in a DNA sequence using collections.Counter

from collections import Counter


class CodonAnalyzer:
  

    def __init__(self, dna):
        self.dna = dna.strip().upper()
        self.codon_counts = self._count_codons()

    def _count_codons(self):
        #Split into triplets and count them with Counter
        codons = [self.dna[i:i+3] for i in range(0, len(self.dna) - 2, 3)]
        return Counter(codons)

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            return cls(f.read())

    def length(self):
        return len(self.dna)

    def gc_content(self):
        if not self.dna:
            return 0.0
        counts = Counter(self.dna)
        gc = counts["G"] + counts["C"]
        return gc / len(self.dna) * 100

    def top_codons(self, n=5):
        #Return the n most common codons using Counter.most_common().
        return self.codon_counts.most_common(n)

    def report(self):
        print("=" * 40)
        print("CODON ANALYSIS REPORT")
        print("=" * 40)
        print(f"Length:     {self.length()}")
        print(f"GC content: {self.gc_content():.2f}%")
        print(f"Unique codons: {len(self.codon_counts)}")
        print("-" * 40)
        for codon, count in sorted(self.codon_counts.items()):
            print(f"{codon}: {count}")
