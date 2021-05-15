#Import Dependencies
import os
import csv

#Declare variables:
total_votes = 0
winning_candidate = ""
winning_count = 0

#Create empty lists
candidates = []
num_of_votes = {}

#Assign a variable for filepath
file_path = os.path.join(".", "Resources/election_data.csv")

#Read the contents of the file
with open(file_path) as electionfile:
	csvreader = csv.DictReader(electionfile)

	for row in csvreader:
		total_votes = total_votes + 1

		#Extract candidate name from each row
		candidate_name = row["Candidate"]

		#Does candidate match existing candidate
		if candidate_name not in candidates:

			#Add it to the list of candidates
			candidates.append(candidate_name)

			#Start number of votes for that candidate
			num_of_votes[candidate_name] = 0

		#Count number of votes for that candidate
		num_of_votes[candidate_name] = num_of_votes[candidate_name] + 1

#Determine the winner by looping through the counts
for candidate in num_of_votes:
	

#Set output
output = (
	"f\nElection Results\n"
	"f-------------------------------\n"
	"f\nTotal Votes: {total_votes}\n"
	"f-------------------------------\n"
	"f\n{num_of_votes[0]}: {num_of_votes[1]}"
	"f\nWinner: "
)
#Set output file path
output_file_path = os.path.join(".", "analysis/election_output_file.txt")

#Exports the results to a text file
with open(output_file_path, "w") as election_output_file:




