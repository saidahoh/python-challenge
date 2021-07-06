import os
import csv

filename = open('budget_data.csv','r')
 
file = csv.DictReader(filename)
TotalMonth = []
TotalAmt = []
Differences= []

for col in file:
    TotalMonth.append(col['Date'])
    TotalAmt.append(col['Profit/Losses'])
TotalMonths = len(TotalMonth)

for i in range(0, len(TotalAmt)):
    TotalAmt[i] = int(TotalAmt[i])



Total_Change = (TotalAmt[85] - TotalAmt[0])
Average_Change = (Total_Change/85)

# Find greatest increase and decrease
for x, y in zip(TotalAmt[0::], TotalAmt[1::]):
    Differences.append(y-x)

Maximum = max(Differences)
Minimum = min(Differences)

#Identify the index to fnd corresponding date
position = Differences.index(Maximum)
position2 = Differences.index(Minimum)

#View positions
# print(position)
# print(position2)

#In the next steps print out the results
Total_M = "Total Months: " + str(TotalMonths)
Total_R = "Total: " + "$" + str(sum(TotalAmt))
Avg_C = "Average Change: " + "$" + str(round(Average_Change, 2))
Great_In = "Greatest Increase in Profit: " + str(TotalMonth[25]) + " " +  "(" + str(Maximum) + ")"
Great_De = "Greatest Decrease in Profit: " + str(TotalMonth[44]) + " " +  "(" + str(Minimum) + ")"

lines = ['Financial Analysis', Total_M, Total_R, Avg_C, Great_In, Great_De]
with open ('analysis_results.txt','w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')