#turn 3 letter Protein name into one letter:
class ProteinTools:
    def __init__(self):
        self.code = {
            'Ala': 'A', 'Arg': 'R', 'Asn': 'N', 'Asp': 'D',
            'Cys': 'C', 'Gln': 'Q', 'Glu': 'E', 'Gly': 'G',
            'His': 'H', 'Ile': 'I', 'Leu': 'L', 'Lys': 'K',
            'Met': 'M', 'Phe': 'F', 'Pro': 'P', 'Ser': 'S',
            'Thr': 'T', 'Trp': 'W', 'Tyr': 'Y', 'Val': 'V',
        }

    def three2one(self, prot):
        s = ''
        for i in prot.split():
            s += self.code.get(i, '?')
        return s

    def from_file(self, filename):
        with open(filename, "r") as f:
            prot = f.read()
        return self.three2one(prot)