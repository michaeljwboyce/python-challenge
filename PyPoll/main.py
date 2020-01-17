import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

Candidates = []
Votes = 0

K = 0
C = 0
L = 0
O = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        Votes += 1
        if row[2] == "Khan":
            K += 1
        elif row[2] == "Correy":
            C += 1
        elif row[2] == "Li":
            L += 1
        elif row[2] == "O'Tooley":
            O += 1

Khan_Percentage = K/Votes*100
Correy_Percentage = C/Votes*100
Li_Percentage = L/Votes*100
OTooley_Percentage = O/Votes*100

if Khan_Percentage > Correy_Percentage and Khan_Percentage > Li_Percentage and Khan_Percentage > OTooley_Percentage:
    Winner = "Khan"
elif Correy_Percentage > Li_Percentage and Correy_Percentage > OTooley_Percentage:
    Winner = "Correy"
elif Li_Percentage > OTooley_Percentage:
    Winner = "Li"
else:
    Winner = "O'Tooley"

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Votes))
print("-------------------------")
print("Khan: " + str(round(Khan_Percentage,2)) +"00%"+ " ("+ str(K)+ ")")
print("Correy: " + str(round(Correy_Percentage,2)) +"0%"+ " ("+ str(C)+ ")")
print("Li: " + str(round(Li_Percentage,2)) +"00%"+ " ("+ str(L)+ ")")
print("O'Tooley: " + str(round(OTooley_Percentage,2)) +"00%"+ " ("+ str(O)+ ")")
print("-------------------------")
print("Winner: " + str(Winner))

output_path = os.path.join('Resources',"polls_result.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Candidate', 'Votes'])
    csvwriter.writerow(['Khan',K])
    csvwriter.writerow(['Correy',C])
    csvwriter.writerow(['Li',L])       
    csvwriter.writerow(["O'Tooley",O])
    csvwriter.writerow(["Total Votes",TotalVotes])    