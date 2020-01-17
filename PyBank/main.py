import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, 'r') as budget_data_csv:
    csvreader = csv.reader(budget_data_csv,delimiter=',')
    csv_header = next(csvreader)
    
    Months = 0
    Total = 0
    This_Month = 0
    Last_Month = 0
    Change = 0
    Total_Change = 0
    Greatest_Inc = 0
    Greatest_Dec = 0
    Greatest_Inc_Date = 0
    Greatest_Dec_Date = 0

    for row in csvreader:
        Months += 1
        Total += int(row[1])
        This_Month = int(row[1])
        if Months > 1:
            Change = This_Month - Last_Month
        if Change > Greatest_Inc:
            Greatest_Inc = Change
            Greatest_Inc_Date = row[0]
        if Change < Greatest_Dec:
            Greatest_Dec = Change
            Greatest_Dec_Date = row[0]
        Total_Change = Change + Total_Change
        Last_Month = This_Month
    
    Average_Change = Total_Change/(Months-1)
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(Months))
    print("Total: $" + str(Total))
    print("Average  Change: $" + str(Average_Change))
    print("Greatest Increase in Profits: " + Greatest_Inc_Date +" ($" + str(Greatest_Inc) + ")")   
    print("Greatest Decrease in Profits: " + Greatest_Dec_Date +" ($" + str(Greatest_Dec) + ")") 
    output_path = os.path.join('Resources',"PyBank_analysis.csv")

    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits'])
        csvwriter.writerow([str(Months), str(Total), str(Average_Change), Greatest_Inc_Date + ": $" + str(Greatest_Inc), Greatest_Dec_Date + ": $" + str(Greatest_Dec) ])