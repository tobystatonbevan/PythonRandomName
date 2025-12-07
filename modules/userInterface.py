def userNameInput(knownNames):
    nameList = []
    nameList.extend(knownNames)
    print("The following are already known to be participating in this year's event:")
    for i in knownNames:
        print(f"{i}")
    #collects user input for the names in the generator, ends when user types END
    while True:  
        namer = input("Enter the name of other participants to be added to the event (type \"END\" when complete):\n")
        if namer == "END":
            break
        elif namer in knownNames:
            print("This user is already known\n")
            pass
        else:
            nameList.append(namer)
    return nameList

def bannedPairingInput():
    nameList = []
    returningNameList = []
    bannedNameList = []
    #collects user input for the names in the generator, ends when user types END
    while True:  
        namer = input("Enter the name of last year's entrants (type \"END\" when complete):\n")
        if namer == "END":
            break
        else:
            nameList.append(namer)
    for x in nameList:
        bannedPairingDict = {}
        returningUser = input(f"Is {x} returning this year? Y or N\n")
        if returningUser.upper() == "Y" or returningUser.upper() == "YES":
            returningNameList.append(x)
            print(f"{x} has been added to returning users")
        previousRecipient = input(f"Who did {x} gift to last year?\n")
        bannedPairingDict["giver"] = x
        bannedPairingDict["recipient"] = previousRecipient
        bannedNameList.append(bannedPairingDict)
    return returningNameList,bannedNameList