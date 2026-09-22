import os
import pandas as pd
import matplotlib.pyplot as plt

from Bio import SeqIO, Phylo
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import (
    DistanceCalculator,
    DistanceTreeConstructor,
    DistanceMatrix,
)


def main():
        #1. Ask for the file 
    path = input("Enter your file's containing aligned sequences path: ").strip()

    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    #2. Read sequences 
    records = list(SeqIO.parse(path, "fasta"))
    name = os.path.splitext(os.path.basename(path))[0]

    if len(records) < 2:
        print("Need at least 2 sequences.")
        return
    lengths = {len(record.seq) for record in records}

    if len(lengths) != 1:
        print("Error: sequences must all have the same length.")
        return

    print(f"Loaded {len(records)} sequences from {name}")

    #3. Build alignment container
    alignment = MultipleSeqAlignment(records)
    print(f"Alignment length: {alignment.get_alignment_length()}")

    #4. Distance matrix 
    calc = DistanceCalculator("blosum62")
    dm = calc.get_distance(alignment)

    names = [rec.id for rec in alignment]
    data = [[dm[i, j] for j in range(len(names))] for i in range(len(names))]
    df = pd.DataFrame(data, index=names, columns=names)
    

    #5. UPGMA tree 
    matrix = df.values.tolist()
    lower = [[matrix[i][j] for j in range(i + 1)] for i in range(len(matrix))]
    dm_obj = DistanceMatrix(list(df.index), lower)
    tree = DistanceTreeConstructor().upgma(dm_obj)

    #6. Draw 
    out_png = f"{name}_tree.png"
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)
    Phylo.draw(tree, axes=ax, do_show=False)
    plt.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.show()
    print(f"Tree saved to {out_png}")


if __name__ == "__main__":
    main()
