#infile is the file you need to convert
#out_format is the format you want the infile to be converted to
#outfile is your final product

from Bio import SeqIO
import os


OUTPUT_FORMATS = sorted(SeqIO._FormatToWriter.keys())

INPUT_FORMATS = {
    ".fasta": "fasta", ".fa": "fasta", ".fna": "fasta",
    ".faa": "fasta", ".ffn": "fasta", ".frn": "fasta",
    ".gb": "genbank", ".gbk": "genbank",
    ".embl": "embl", ".phy": "phylip",
    ".aln": "clustal", ".clustal": "clustal",
    ".sto": "stockholm", ".stockholm": "stockholm",
    ".fastq": "fastq", ".fq": "fastq",
}

infile = input("Enter your file's path: ").strip()
ext = os.path.splitext(infile)[1].lower()
in_format = INPUT_FORMATS.get(ext)

if not in_format:
    print(f"Unknown input format for extension '{ext}'")
    print(f"Supported: {sorted(INPUT_FORMATS.keys())}")
    raise SystemExit(1)

print(f"Detected input format: {in_format}")

out_format = input(f"Enter output format {OUTPUT_FORMATS}: ").strip().lower()
if out_format not in OUTPUT_FORMATS:
    print(f"❌ Unsupported format: {out_format}")
    raise SystemExit(1)

outfile = input("Enter your output path: ").strip()

records = SeqIO.parse(infile, in_format)
count = SeqIO.write(records, outfile, out_format)

print(f"Converted {count} records: {in_format} → {out_format}")