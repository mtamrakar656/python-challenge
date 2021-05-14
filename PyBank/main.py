#Import Dependencies
import os
import csv

#Declare variables:
total_months = 0
net_amount = 0
prev_amount = 0
month_of_change = []
amount_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

#Assign a variable for filepath
file_path = os.path.join(".", "Resources/budget_data.csv")

#Read the contents of the file
with open(file_path) as csvfile:
	csvreader = csv.reader(csvfile)

	#Skip the header
	next(csvreader)

	for row in csvreader:
		# Count the totals
		total_months = total_months + 1
		net_amount = net_amount + int(row[1])
		
		#Track the revenue change
		amount_change = int(row[1]) - prev_amount
		prev_amount = int(row[1])
		amount_change_list = amount_change_list + [amount_change]
		month_of_change = month_of_change + [[row[0]]]
		
		#Calculate the greatest increase
		if (amount_change > int(greatest_increase[1])):
			greatest_increase[0] = row[0]
			greatest_increase[1] = row[1]
			
		if (amount_change < int(greatest_decrease[1])):
			greatest_decrease[0] = row[0]
			greatest_decrease[1] = row[1]



#Calculate the Average Amount Change
amount_change_avg = sum(amount_change_list) / len(amount_change_list)

#Generat Output Summary
output = (
	f"\nFinancial Analysis\n"
	f"-----------------------------\n"
	f"\nTotal Months:  {total_months}\n"
	f"\nTotal Revenue: ${net_amount}\n"
	f"\nAverage Change: ${amount_change_avg}\n"
	f"\nAverage Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
	f"\nAverage Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
	)

#Print the output
print(output)

#Create variable for output file
file_output_path = os.path.join(".", "analysis/analysis_file.txt")

#Export the results to a text file
with open(file_output_path, "w") as output_file:
	output_file.write(output)

