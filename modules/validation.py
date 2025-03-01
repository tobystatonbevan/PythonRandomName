def validityChecker(gName,rName):
    errors = matchingNameCheck(gName,rName)+directSwapCheck(gName,rName)
    return errors

def matchingNameCheck(gName,rName):
    #counts errors found in checking
    errors = 0
    #loops through both lists and checks that giver and recipient don't match at a certain index
    for g,r in zip(gName,rName):
        #if giver and recipient match, an error is counted and the for loop is broken
        if g == r:
            errors += 1
            break
    return errors

def directSwapCheck(gName,rName):
    #counts errors found in checking
    errors = 0
    #declare dictionary where key is giver initials and value is recipient initials
    pairsDict = {}
    #builds the pairsDict dictionary (g:r)
    for g,r in zip(gName,rName):
        pairsDict[g] = r
    #checks every name in the givers list as a key in the pairsDict which returns their recipient. If the current giver is a recipient for other another giver, an error is counted and the for loop is broken
    for i in gName:
        if pairsDict.get(pairsDict[i]) == i:
            errors += 1
            break
    return errors

def finalPairingListOfDicts(aName,gName,rName):
    #local list of properly formed dict
    fPairings = []
    #creates a properly formed dictionary {'Giver':name,'Recipient':name} and appends it to the finalPairings list
    for i in range(len(aName)):
        pairing = {}
        pairing["Giver"] = gName[i]
        pairing["Recipient"] = rName[i]
        fPairings.append(pairing)
    return fPairings