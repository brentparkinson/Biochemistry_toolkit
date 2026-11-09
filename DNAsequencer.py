while True:
    print("Enter Coding DNA Sequence")
    coding_dna_sequence = input()
    coding_dna_sequence = coding_dna_sequence.upper()
    valid_bases = {"A", "C", "G", "T"}
    if not coding_dna_sequence:
        continue
    if not set(coding_dna_sequence).issubset(valid_bases):
        print("Invalid DNA sequence.")
        continue
    break
print("Sequence length:", len(coding_dna_sequence), "bp")
print("The nucleotide composition of the DNA sequence is:")
A = coding_dna_sequence.count("A")
C = coding_dna_sequence.count("C")
G = coding_dna_sequence.count("G")
T = coding_dna_sequence.count("T")
print("A:", A)
print("C:", C)
print("G:", G)
print("T:", T)
print("The GC content of the DNA sequence is:")
gc_content = (G + C) / len(coding_dna_sequence) * 100
print(f"{gc_content:.2f}%")
while True:
    print("Select an option:")
    print("1. View Reverse Complement")
    print("2. Transcribe to RNA")
    print("3. Translate to AA Sequence")
    print("4. Exit")
    option = input("Enter your choice: ")
    if option == "1":
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
        template_dna_sequence = "".join(complement[base] for base in reversed(coding_dna_sequence))
        print("Reverse Complement:", template_dna_sequence)
    elif option == "2":
        rna_sequence = coding_dna_sequence.replace("T", "U")
        print("RNA Sequence:", rna_sequence)
    elif option == "3":
        codon_table = {
            "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
            "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
            "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
            "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
            "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
            "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
            "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
            "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
            "TAT": "Y", "TAC": "Y", "TAA": "Stop", "TAG": "Stop",
            "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
            "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
            "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
            "TGT": "C", "TGC": "C", "TGA": "Stop", "TGG": "W",
            "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
            "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
            "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
        }
        aa_sequence = ""
        for i in range(0, len(coding_dna_sequence), 3):
            codon = coding_dna_sequence[i:i+3]
            aa = codon_table.get(codon, "")
            if aa == "Stop":
                break
            aa_sequence += aa
        print("AA Sequence:", aa_sequence)
    elif option == "4":
        break
    else:
        print("Invalid option. Please select 1, 2, 3, or 4.")