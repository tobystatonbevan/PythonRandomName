def userNameInput():
    nameList = []
    #collects user input for the names in the generator, ends when user types END
    while True:  
        namer = input("Enter the name of your channel:\n")
        if namer == "END":
            break
        else:
            nameList.append(namer)
    return nameList