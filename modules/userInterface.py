def userNameInput(knownNames):
    #namelist variable for known names and new names
    nameList = []
    nameList.extend(knownNames)
    #a list of lowercased and whitespace stripped names for duplication checking
    knownNamesSanitised = []
    #strips and lowers names from known list for sanitiation check
    for i in knownNames:
        knownNamesSanitised.append(i.replace(" ","").lower())
    #print known names to console
    print("The following are already known to be participating in this year's event:")
    for i in knownNames:
        print(f"{i}")
    #collects user input for the names in the generator, ends when user types END
    while True:  
        namer = input("Enter the name of other participants to be added to the event (type \"END\" when complete):\n")
        if namer.upper() == "END":
            break
        elif namer.replace(" ","").lower() in knownNamesSanitised:
            print("This user is already known\n")
            pass
        elif not namer:
            print("Value cannot be empty.")
        else:
            nameList.append(namer)
    return nameList