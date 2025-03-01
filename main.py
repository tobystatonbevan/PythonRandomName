import random
from modules import validityChecker,finalPairingListOfDicts
#declare all names 
allNames = []
#copy all names to a giver and recipient list
giverName = allNames.copy()
recipientName = allNames.copy()

#declare list of final pairing dictionaries with Giver and Recipient keys
finalPairings = []
#declares current list as invalid until checks are completed
invalid = True

while invalid:
    #shuffles both lists randomly
    random.shuffle(giverName)
    random.shuffle(recipientName)

    #if no errors have been found, the pairings are deemed valid
    if validityChecker(giverName,recipientName) == 0:
        invalid = False 
#call function to create a properly formed dictionary {'Giver':name,'Recipient':name} and sets it to finalPairings variable
finalPairings = finalPairingListOfDicts(allNames,giverName,recipientName)

#iterates finalPairings list and prints a formatted list of Givers and Recipients
for p in finalPairings:
    print(f"{p['Giver']} is giving to {p['Recipient']}")