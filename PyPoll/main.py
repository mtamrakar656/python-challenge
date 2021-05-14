#Import Dependencies
import os
import csv

#Declare variables:
total_months = 0
net_amount = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

#Assign a variable for filepath
file_path = os.path.join(".", "Resources/budget_data.csv")

#Read the contents of the file
with open(file_path, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ",")

	for row in csvreader:
		#Count the totals
		total_months = total_months + 1
		net_amount = net_amount + int(row[1])

print(f"Total Months:  {total_months}")
print(f"Total: {net_amount}" )

