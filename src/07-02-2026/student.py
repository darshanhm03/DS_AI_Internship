import csv

with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
