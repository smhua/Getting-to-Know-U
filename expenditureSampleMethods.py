
#returns a list tuples of PIs and $/ASF if their $/ASF is greater than number.
def piASFGreater(filename, number):
    file = open(filename)
    header = file.readline()
    data = file.readlines()
    file.close()
    newlist = []
    retlist = []
    for each in data:
        newlist.append(each.strip("\n").split(","))

    for row in newlist:
        comp = 0
        if row[4][0] == "(":
            comp = -1 * int(row[4][1:-1])
        else:
            comp = int(row[4])
        if comp > number:
         retlist.append((row[0], comp))
    return retlist

##print(piASFGreater("2018CSV.csv", 200))
##piASFGreater("2018CSV.csv", 200) <- returns list of (LAST_NAME  FIRST_NAME, $/ASF) for $/ASF > 200
