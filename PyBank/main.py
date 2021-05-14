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
with open(file_path) as budget_data:
	csvreader = csv.reader(budget_data)

	#Skip the headerf
	next(csvreader)

	for row in csvreader:
                
		# Count the totals
                total_months = total_months + 1
                net_amount = net_amount + int(row[1])

	
	amount_change = int(row[1]) - prev_amount

#		# Track the revenue change
#		amount_change = int(row[1]) - prev_amount
#		prev_amount = int(row[1])
#		amount_change_list = revenue_change_list + [amount_change]
#		month_of_change = month_of_change + [[row[0]]]

print(f"Total Months:  {total_months}")
print(f"Total: ${net_amount}" )
