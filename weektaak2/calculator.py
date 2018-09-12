var = input('Your sequence: ')
if var == "" :
    var = input('Please enter a valid sequence: ')
else :
    var = var.replace("\n", " ").replace("\r", " ").replace(" ", "")
    # var = var.replace(' ', '')
    length = var.count("G") + var.count("C") + var.count("T") + var.count("A")
    gc = var.count("G") + var.count("C")
    check = round(gc/len(var) * 100)
    seqL = round(len(var) / 4)
    lengthStr = str(length) + ""
    nucL = str(seqL) + ""
    print("\n", "This sequence has ", lengthStr, " characters.")
    #print(" This sequence has ", nucL, " nucleotides.")
    print(" The GC percentage is: ", check, "%")