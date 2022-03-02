import csv

import pandas
import pandas as pd
# Reading from CSV and print out the content
# with open('employee_birthday.csv') as f:
#     csv_reader = csv.reader(f, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names:\t{",".join(row)}')  # csv reader produces a list for each line
#             line_count += 1
#         else:
#             print(f'\t\t{row[0]} works in {row[1]}, was born in {row[2]}')
#             line_count += 1

# Reading a csv with DictReader: uses the header line for fieldnames and for dictionary keys
# with open('employee_birthday.csv') as f:
#     csv_reader = csv.DictReader(f, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names:\t{",".join(row)}')
#             line_count += 1
#         print(f'\t\t{row["name"]} works in {row["department"]}, was born in {row["birthday month"]}')
#         # using the headers as dict keys to print the values
#         line_count += 1
# print(f'Processed {line_count} lines')

# Writing to CSV

# Reading CSV with Pandas

df=pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
# index_col= *** instead of zero index we can set an index column
# parse dates= *** dates are read as str so we need to specify which field is a date
print(df)
