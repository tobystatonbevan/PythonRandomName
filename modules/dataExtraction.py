import csv
from pathlib import Path


def previousNamesExtraction():
    #names list
    returningNames = []
    #pairings
    bannedPairings = {}
    #open previous.csv
    with open(Path.cwd() / "data" / "previous.csv") as preNamefile:
        PreviousNamesFile = csv.DictReader(preNamefile)
        for i in PreviousNamesFile:
            if int(i["giver_returning"]) == 1 and i["giver"] not in returningNames:
                returningNames.append(i["giver"])
            bannedPairings.update({i["giver"]:i["recipient"]})
    return returningNames,bannedPairings

def pairingLog(pairings):
    finalPairingsList = []
    for pair in pairings:
        finalPairingsList.append([pair['Giver'],"0",pair['Recipient']])
    print(finalPairingsList)
    with open (Path.cwd() / "data" / "output.csv", mode= "w", newline="") as outputFile:
        scribe = csv.writer(outputFile)
        scribe.writerow(["giver","giver_returning","recipient"])
        scribe.writerows(finalPairingsList)