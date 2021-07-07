import os
import csv

filename = open('election_data.csv','r')
 
file = csv.DictReader(filename)

Votes = []
CandNm = []
Khan = []
Correy = []
Li = []
Tooley = []


VoteCnt = 0

for row in file:
    VoteCnt += 1
    Votes.append(row['Voter ID'])

TotalVotes = len(Votes)
Total_Votes = "Total Votes: " + str(TotalVotes)

for col in file:
    if col not in CandNm:
        CandNm.append(row[2])

print (CandNm[0])


# print('Financial Analysis','===================', Total_M, Total_R, Avg_C, Great_In, Great_De, sep = '\n')

# lines = ['Financial Analysis','===================' Total_M, Total_R, Avg_C, Great_In, Great_De]
# with open ('analysis_results.txt','w') as f:
#     for line in lines:
#         f.write(line)
#         f.write('\n')

