import os
import csv
import numpy as np
from os.path import split

# path to collect data from the Resources folder
budget_data_path = "Resources/budget_data.csv"

# data file
budget_data = os.path.join(budget_data_path)

# months as list
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# creating a function to perform the analysis
# def budget_analysis(budget_data):

# lists to store data
month_year = []
month = []
year = []
profit_loss = []
months_years = []

# reading csv data and defining variables
with open(budget_data, newline="") as b_file:
    csvreader = csv.reader(b_file, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        # variable for month_year
        month_year.append(row[0])
        months_years = row[0].split("-")
        month.append(months_years[0])
        # year.append(months_years[1])
        # month = months_years[0]
        # year = months_years[1]
        # months_years = month[row[0]].split("-")
        profit_loss.append(int(row[1]))

# total_pnl = sum(profit_loss)
# print(months_years)
# print(month)
# Zip lists together
# cleaned_csv = zip(month, month_year, profit_loss)

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total +=number
    return total/length

total_pnl = sum(profit_loss)
average_pnl = average(profit_loss)

# creating array for monthly difference
a = np.array(profit_loss)
average_change_pnl = round(average(np.diff(a)),2)
diff_array = np.diff(a)

# grabbing max from array of monthly difference
max_change = 0
for num in diff_array:
    if (max_change is None or num > max_change):
        max_change = num

# grabbing min from array of monthly difference
min_change = 0
for num in diff_array:
    if (min_change is None or num < min_change):
        min_change = num



print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {len(month_year)}")
print(f"Total: ${total_pnl}")
print(f"Average Change: ${average_change_pnl}")

# used numpy index to find index for month_year list... details in lines below
print(f"Greatest Increase in Profits:  {month_year[25]} (${max_change})")
print(f"Greatest Decrease in Profits:  {month_year[44]} (${min_change})")

print("----------------------------------")
print("numpy indices")
# gives out put of [24], which will be [25] in the month_year list ^ using in the above
print(np.where(diff_array == max_change))
# gives out put of [43], which will be [44] in the month_year list ^ using in the above
print(np.where(diff_array == min_change))

# path for final analysis
analysis_path = os.path.join("Analysis","analysis_final.txt")

# open the file in write mode
with open(analysis_path, "w", newline="") as txtfile:

    txtfile.write("Financial Analysis")
    txtfile.write("\n----------------------------------")
    txtfile.write(f"\nTotal Months: {len(month_year)}")
    txtfile.write(f"\nTotal: ${total_pnl}")
    txtfile.write(f"\nAverage Change: ${average_change_pnl}")
    txtfile.write(f"\nGreatest Increase in Profits:  {month_year[25]} (${max_change})")
    txtfile.write(f"\nGreatest Decrease in Profits:  {month_year[44]} (${min_change})")
