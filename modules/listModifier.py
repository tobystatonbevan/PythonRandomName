def listDisplacer(givenList):
    #declares output list as empty
    outputList = []
    #adds all elements of givenList to outputList
    outputList.extend(givenList)
    #inserts the final name in the outputList at the start
    outputList.insert(0,outputList[-1])
    #deletes the final name in outputList
    outputList.pop()
    #returns outputList
    return outputList