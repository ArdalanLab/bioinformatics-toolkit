# Translate a DNA sequence in all 6 reading frames.
from Bio.Seq import Seq


def six_frame_translate(sequence: str) -> dict:
    """Translate a DNA sequence in all 6 reading frames.

    Parameters
    ----------
    sequence : str
        A DNA sequence (A/T/C/G, case-insensitive).

    Returns
    -------
    dict
        Keys like "+1", "+2", "+3", "-1", "-2", "-3" mapped to
        their translated protein sequences (as strings).
    """
    dna = Seq(sequence.upper())
    rc = dna.reverse_complement()

    frames = {}
    for i in range(3):
        frames[f"+{i+1}"] = str(dna[i:].translate(gap="X"))
    for i in range(3):
        frames[f"-{i+1}"] = str(rc[i:].translate(gap="X"))

    return frames


def print_frames(frames: dict) -> None:
    print("=== Forward frames ===")
    for label in ("+1", "+2", "+3"):
        print(f"Frame {label}: {frames[label]}")

    print("\n=== Reverse complement frames ===")
    for label in ("-1", "-2", "-3"):
        print(f"Frame {label}: {frames[label]}")


if __name__ == "__main__":
    # Edit this to whatever sequence you want to translate
    SEQUENCE = (
        "CTCACACTCACCTCCCTCACTGTGCCTCTCGCACAGTAATACACAGCCGTGTCCGCGGCGGTCACA"
        "GAGCTCAGCTTCAGGGAGAACTGGTTCTTGGACGTGTCTACTGATATGGTGACTCGACTCTTGAGG"
        "GACGGGTTGTAGTTGGTGCTTCCACTATGATTGATTTCCCCAATCCACTCCAGCCCCTTCCCTGGG"
        "GGCTGGCGGATCCAGCTCCAGTAGTAACCACTGAAGGACCCACCATAGACAGCGCAGGTGAGGGAC"
        "AGGGTCTCCGAAGGCTTCAACAGTCCTGCGCCCCACTGCTGTAGCTGCACCTGGGACAGGACCCCT"
        "GTGAACAGAGAAGACACACNGTAGCGCCTCGCGA"
    )

    frames = six_frame_translate(SEQUENCE)
    print_frames(frames)