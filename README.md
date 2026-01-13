# PythonRandomName
 A basic random name generator built in Python. It is intended for use in deciding a "secret santa" style gifting arrangement. 

 Dependencies:

 There is a requirement to have a "previous.csv" file in the data directory. This csv should follow the following column structure:
 giver,giver_returning,recipient

 where

 giver is a String
 giver_returning is an Integer (1 for true or 0 for false)
 recipient is a String

 There are three key features to the logic:

 1. The gifter cannot match the recipient (no self gifting)
 2. The gifter cannot be the recipient for the person they draw (no direct swaps)
 3. The gifter cannot have gifted to someone in a previous event

 GiftPairings.py takes user input through CLI, but opens a basic window to display the output in a prettier manner

 A CSV file of the draw results will be written to the data folder, called "output.csv". This CSV follows the "previous.csv" format so it may be used as input. Please note that this file will be overwritten on each run, and so you should make a copy after each running of the script if you wish to log the results of repeated draws. 