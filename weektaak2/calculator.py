print("Filepath example:  /Users/daan/Downloads/School/Bio-Informatica/Lig1-DNA-Homo Sapiens.fasta.txt")
print("Make sure there are no other 'G', 'C', 'T' or 'A' characters in the file!")
var = input('Your filepath: ')
if var == "" :
    var = input('Please enter a valid sequence: ')
else :
    bestand = open(var)
    seq = bestand.read()
    length = seq.count("G") + seq.count("C") + seq.count("T") + seq.count("A")
    gc = seq.count("G") + seq.count("C")
    check = round(gc/length * 100)
    seqL = round(length / 4)
    lengthStr = str(length) + ""
    nucL = str(seqL) + ""
    print("\n", "This sequence has ", lengthStr, " nucleotides.")
    print(" The GC percentage is: ", check, "%")
