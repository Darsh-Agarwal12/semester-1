# Worksheet 1.3: Task 3

# Your code for the overall grade classification
import csv
# ask for filename of the student file
file=input("Enter the name of the student data file: ")
address=f'/workspaces/semester-1/week1.3/worksheet/task3/{file}'
# open the file
with open(address, 'r') as f:
    reader = csv.reader(f)
    # read the header
    header = next(reader)
    # read the data
    data = [row for row in reader]
# read in the data, and for each student calculate their average grade and classification
output_rows = []

for row in data:
    if not row:
        continue
        
    student_id = row[0]
    
    # Extract grades, filtering out empty fields caused by trailing commas
    grades = []
    for item in row[1:]:
        if item.strip():  # Only keep fields containing numbers
            grades.append(int(item))
            
    # Calculate the mean safely
    if len(grades) > 0:
        average_grade = sum(grades) / len(grades)
    else:
        average_grade = 0.00
        
    # Determine classification boundary
    if average_grade >= 70:
        classification = "1"
    elif average_grade >= 60:
        classification = "2:1"
    elif average_grade >= 50:
        classification = "2:2"
    elif average_grade >= 40:
        classification = "3"
    else:
        classification = "F"
    #output the updated data
    output_rows.append([student_id, f"{average_grade:.2f}", classification])


# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}

# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'
output_address = address + "_out.csv"

with open(output_address, 'w', newline='') as out_f:
    writer = csv.writer(out_f)
    writer.writerows(output_rows)