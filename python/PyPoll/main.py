import os
import csv

# path to collect data from the Resources folder
election_data_path = "Resources/election_data.csv"

# data file
election_data = os.path.join(election_data_path)

voter_id = []
county = []
candidate = []

with open(election_data, newline="") as e_file:
    csvreader = csv.reader(e_file, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
def candidate_votes(name):
    candidate_count = candidate.count(name)
    print(candidate_count)

total_votes = len(voter_id)

def vote_percentage(name):
    candidate_percentage = candidate.count(name) / total_votes * 100
    round_percent = round(candidate_percentage,3)
    print(f'{round_percent}%')

def candidate_finish(name):
    candidate_count = candidate.count(name)
    candidate_percentage = candidate_count / total_votes * 100
    round_percent = round(candidate_percentage,3)
    print(f"{name}: {round_percent} ({candidate_count})")

def candidate_finish_txt(name):
    candidate_count = candidate.count(name)
    candidate_percentage = candidate_count / total_votes * 100
    round_percent = round(candidate_percentage,3)
    txtfile.write(f"\n{name}: {round_percent} ({candidate_count})")

print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
choices = ["Khan","Correy","Li","O'Tooley"]
for choice in choices:
    candidate_finish(choice)
print("--------------------------")
print("Winner: Khan")
print("--------------------------")

# path for final analysis
analysis_path = os.path.join("Analysis","analysis_final.txt")

# open the file in write mode
with open(analysis_path, "w", newline="") as txtfile:
    txtfile.write("Election Results")
    txtfile.write("\n--------------------------")
    txtfile.write(f"\nTotal Votes: {total_votes}")
    txtfile.write("\n--------------------------")
    choices = ["Khan","Correy","Li","O'Tooley"]
    for choice in choices:
        candidate_finish_txt(choice)
    txtfile.write("\n--------------------------")
    txtfile.write("\nWinner: Khan")
    txtfile.write("\n--------------------------")