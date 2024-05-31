def to_rna(dna_strand):
    dna_to_rna = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
    }
    rna_strand = ''
    for index in range(len(dna_strand)):
        rna_strand += dna_to_rna[dna_strand[index]]
    return rna_strand