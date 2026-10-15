# Week 1.3, Session 2: Calculate Average Grade and Write to a File
import csv
# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]


# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f

with open('student_data.csv', 'r') as f:
    data = list(csv.reader(f))
    students = data[1:]  # This is the student data
    for student in students:
        name = student[1]
        maths = int(student[2])
        science = int(student[3])
        history = int(student[4])
        average = (maths + science + history) / 3

        with open('report.txt', 'a') as report_file:
            report_file.write(f"{name}: {average:.2f}\n")