import csv
import os

PyPoll=os.path.join("Resources","PyPoll.csv")

ID=[]
Country=[]
Candidate=[]
Votes=[]


with open(PyPoll,"r", encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    csv_header=next(csvreader)

    for row in csvreader:

        ID.append(row[0])

        Country.append(row[1])

        Candidate.append(row[2])


Total_votes=len(ID)

my_set=set(Candidate)
Cand_list=list(my_set)

for x in Cand_list:
    Votes.append(Candidate.count(x))

output_file ="pypoll_analysis.txt"

with open(output_file, "w") as file:
    file.write(f"Election Results\n")
    file.write(f"------------------\n")
    file.write(f'Total votes: {Total_votes}\n')
    file.write(f"------------------\n")

    for (a,b) in zip(Cand_list,Votes):
        file.write(f'{a}: {round((b/Total_votes)*100,3):.3f}% ({b})\n')

    winner=Votes.index(max(Votes))

    file.write(f"-----------------\n")
    file.write(f'Winner: {Cand_list[winner]}\n')
    file.write(f"------------------\n")