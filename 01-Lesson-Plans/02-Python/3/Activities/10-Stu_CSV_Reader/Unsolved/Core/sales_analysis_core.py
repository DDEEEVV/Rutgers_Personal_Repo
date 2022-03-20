# -*- coding: utf-8 -*-
"""Student Do: Sales Analysis.

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, and iterate over each
row of the file to calculate customer sales averages.
"""

# @TODO: Import the pathlib and csv library
from pathlib import Path
import csv

from numpy import average

# @TODO: Set the file path
csvpath = Path("Rutgers_Personal_Repo/01-Lesson-Plans/02-Python/3/Activities/10-Stu_CSV_Reader/Resources/sales.csv")

# Initialize list of records
records = []

# @TODO: Open the csv file as an object
with open(csvpath, 'r') as csvfile:

    # @TODO:
    # Pass in the csv file to the csv.reader() function
    csvreader = csv.reader(csvfile, delimiter=',')
    # (with ',' as the delmiter/separator) and return the csvreader object

    # @TODO: Read the header row
    csv_header = next(csvreader)
    print(csv_header)
    csv_header.append("Average")
    records.append(csv_header)

    # @TODO: Read each row of data after the header
    for row in csvreader:

        # @TODO: Print the row
        print(row)

        # @TODO:
        # Set the 'name', 'count', 'revenue' variables for better
        # readability, convert strings to ints for numerical calculations
        name = row[0]
        count = int(row[1])
        revenue = int(row[2])

        # @TODO: Calculate the average (round to the nearest 2 decimal places)
        average = round(revenue / count, 2)

        # @TODO: Append the average to the row
        row.append(average)

        # @TODO: Append the row to the list of records
        records.append(row)

# @TODO: Set the path for the output.csv
output = Path("Rutgers_Personal_Repo/01-Lesson-Plans/02-Python/3/Activities/10-Stu_CSV_Reader/Resources/output.csv")
# @TODO:
# Open the output path as a file and pass into the 'csv.writer()' function
# Set the delimiter/separater as a ','
with open(output,'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for record in records:
        csvwriter.writerow(record)



    # @TODO:
    # Loop through the list of records and write every record to the
    # output csv file
