#GUI elements are written by ChatGPT... I feel dirty and ashamed

import tkinter as tk

import random
from modules import validityChecker,finalPairingListOfDicts,userNameInput,bannedPairingInput,listDisplacer
#declare last year's pairings
lastYearPairings=[]
#declares two list variables; one of known returning names and one list of dictionaries which are banned pairings
returningNames,lastYearPairings = bannedPairingInput()

#declare all names  
allNames = []
#collects remaining names for this year's draw
allNames = userNameInput(returningNames)

#copy all names to a giver list
giverName = allNames.copy()
#randomly shiffles the giverName list
random.shuffle(giverName)
#displaces the list by one, causing a circular gifting result, and creates a variable called recipientName to hold it
recipientName = listDisplacer(giverName)

#declare list of final pairing dictionaries with Giver and Recipient keys
finalPairings = []
#declares current list as invalid until checks are completed
invalid = True

#BOOKMARK: continue to work from here. No longer need shuffle, and validation is now based on identifying repeated gifting from last year

while invalid:
    #shuffles both lists randomly
    random.shuffle(giverName)
    random.shuffle(recipientName)

    #if no errors have been found, the pairings are deemed valid
    if validityChecker(giverName,recipientName) == 0:
        invalid = False 
#call function to create a properly formed dictionary {'Giver':name,'Recipient':name} and sets it to finalPairings variable

pairings = finalPairingListOfDicts(allNames,giverName,recipientName)

# Create the main window
root = tk.Tk()
root.title("Toolroom Exchange 2026")
root.geometry("600x400")

# Title Label
title_label = tk.Label(root, text="Gift Pairings", font=("Arial", 52, "bold"))
title_label.pack(pady=20)

# Display Pairings
for pair in pairings:
    label = tk.Label(root, text=f"{pair['Giver']} is building for {pair['Recipient']}", font=("Arial", 18))
    label.pack()

# Run the application
root.mainloop()
