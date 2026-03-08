import csv

filename = input("Enter CSV file: ")

try:
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    print("Rows:", len(rows)-1)
    print("Columns:", len(rows[0]))

except:
    print("Error reading file")
