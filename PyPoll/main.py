#Import Dependencies
import os
import csv

#Declare variables:
total_votes = 0

#Assign a variable for filepath
file_path = os.path.join(".", "Resources/election_data.csv")

#Read the contents of the file
with open(file_path) as electionfile:
	csvreader = csv.reader(electionfile)

	for row in csvreader:
		total_votes = total_votes + 1




