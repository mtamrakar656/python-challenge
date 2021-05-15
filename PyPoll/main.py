#Import Dependencies
import os
import csv

#Declare variables:
total_votes = 0
winning_candidate = ""
winning_count = 0

#Create empty lists
candidates_list = []
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
		if candidate_name not in candidates_list:

			#Add it to the list of candidates
			candidates_list.append(candidate_name)

			#Start number of votes for that candidate
			num_of_votes[candidate_name] = 0

		#Count number of votes for that candidate
		num_of_votes[candidate_name] = num_of_votes[candidate_name] + 1

#Set output file path
output_file_path = os.path.join(".", "analysis/election_output_file.txt")

#Print the results and export the data to text file
with open(output_file_path, "w") as election_output_file:

	#Print the final vote count
	election_results = (
		f"\nElection Results\n"
		f"-------------------------\n"
		f"Total Votes: {total_votes}\n"
		f"-------------------------\n"
	)
	print(election_results)

	# Save the final vote count to the text file
	election_output_file.write(election_results)

#Determine the winner by looping through the counts
for candidate in num_of_votes:

	#Retrieve the final vote count and calculate percentage
	votes = num_of_votes.get(candidate)
	vote_percentage = float(votes) / float(total_votes) * 100

	#Determine the winning vote count and percentage
	if (votes > winning_count):
		winning_count = votes
		winning_candidate = candidate

	#Set variable for voter count and percentage
	voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"


#Set output
output = (
	"f\nElection Results\n"
	"f-------------------------------\n"
	"f\nTotal Votes: {total_votes}\n"
	"f-------------------------------\n"
	"f\n{voter_output}"
	"f\nWinner: {winning_candidate}"
)

#Print output to terminal
print(output)

