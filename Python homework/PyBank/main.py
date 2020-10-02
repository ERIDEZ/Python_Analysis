import os
import csv

PyBank = os.path.join("..","Resources","PyBank.csv")

ProfitLosses=[]
Date=[]
TotalProfit = 0
counter=0
diff=[]

# CSV reader and list append
with open(PyBank,"r", encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    csv_header=next(csvreader)

    for row in csvreader:

        Date.append(row[0])

        ProfitLosses.append(row[1])


# Converts strings into integers
ProfitLosses[:]=list(map(int, ProfitLosses))

# List of differences of integer list
xdiff = [ProfitLosses[n]-ProfitLosses[n-1] for n in range(1,len(ProfitLosses))]

# Gets the average of the differences
Avrg=(sum(xdiff)/len(xdiff))

# Sums every integer or float within a list
TotalProfit=sum([i for i in ProfitLosses if isinstance(i,int) or isinstance(i, float)])

# I have to create a value of index[0] for the xdiff lists, because when I use zip command, the list of dates wont match according to the difference
differences=[0]

differences.extend(xdiff)

minimun=(differences.index(min(differences)))
maximun=(differences.index(max(differences)))


print(f'Financial Analysis')
print("----------------------")
print(f'Total months: {len(Date)}')
print(f'Total: ${TotalProfit}')
print(f'Average change: ${round(Avrg,2)}')
print(f'Greatest Increase in Profits: {Date[maximun]} ${differences[maximun]}')
print(f'Greatest Decrease in Profits: {Date[minimun]} ${differences[minimun]}')
