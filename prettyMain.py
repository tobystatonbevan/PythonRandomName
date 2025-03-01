import tkinter as tk

import random
from modules import validityChecker,finalPairingListOfDicts,userNameInput
#declare all names  
allNames = []

allNames = userNameInput()

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

pairings = finalPairingListOfDicts(allNames,giverName,recipientName)

# Create the main window
root = tk.Tk()
root.title("Gift Exchange")
root.geometry("300x200")

# Title Label
title_label = tk.Label(root, text="Gift Pairings", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Display Pairings
for pair in pairings:
    label = tk.Label(root, text=f"{pair['Giver']} is building for {pair['Recipient']}", font=("Arial", 12))
    label.pack()

# Run the application
root.mainloop()
