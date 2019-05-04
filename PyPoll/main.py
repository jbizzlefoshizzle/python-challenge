# I do declare
import os
import csv
# new stuff!
# need for final printout of winner
from collections import Counter

# Vote or die
vote_csv = os.path.join('..','Resources','election_data.csv')
# Open and read
with open(vote_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Skip headers
    csv_header = next(csvfile)
    # Create empty lists
    list_voter_id = []
    list_county = []
    list_candidate = []
    # Put stuff in lists
    for row in csvreader:
        id = row[0]
        county = row[1]
        vote_name = row[2]
        list_voter_id.append(id)
        list_county.append(county)
        list_candidate.append(vote_name)
        
# Print or die
print("Election Results")
print("-------------------------")
# How to total votes
print("Total Votes: " + str(len(list_voter_id)))
print("-------------------------")
# Counts for candidates
khan = list_candidate.count('Khan')
correy = list_candidate.count('Correy')
li = list_candidate.count('Li')
o_tooley = list_candidate.count("O'Tooley")
# Percents
khan_percent = khan*100 / len(list_voter_id)
correy_percent = correy*100 / len(list_voter_id)
li_percent = li*100 / len(list_voter_id)
o_tooley_percent = o_tooley*100 / len(list_voter_id)
# Percents (but nicer)
khan_percent_formatted = format(khan_percent, '.3f')
correy_percent_formatted = format(correy_percent, '.3f')
li_percent_formatted = format(li_percent, '.3f')
o_tooley_percent_formatted = format(o_tooley_percent, '.3f')

# Printy McPrintface
# Print names, percents, counts
print("Khan: " + str(khan_percent_formatted)+"% (" + str(khan) + ")")
print("Correy: " + str(correy_percent_formatted)+"% (" + str(correy) + ")")
print("Li: " + str(li_percent_formatted)+"% (" + str(li) + ")")
print("O'Tooley: " + str(o_tooley_percent_formatted)+"% (" + str(o_tooley) + ")")
print("-------------------------")

# So who won?
for x in list_candidate:
    d[x] = += 1
    winner = max(d.iteritems())
#winner = Counter(list_candidate).most_common(1)
print("Winner: " + str(winner))