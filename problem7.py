import matplotlib.pyplot as plt
import numpy as np

# read file
with open("/Users/thiphan/Desktop/HCMC_scores/clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

# remove empty list (end of file)
students.pop()
total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# turn each student to a list
for i in range(len(students)):
	students[i] = students[i].split(",")

max_name_length = 0 # length of name
index = 0 
for i in range(len(students)):
	if len(students[i][1]) >= max_name_length:
		max_name_length = len(students[i][1])
		index = i

print(students[index][0])
print(students[index][1])