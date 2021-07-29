#class Data_prep:
# read file
with open("/Users/thiphan/Desktop/HCMC_scores/clean_data.csv", encoding = "utf8") as file:
     data = file.read().split("\n")

header = data[0]
students = data[1:]

students.pop()
total_student = len(students)

header = header.split(",")
subjects = header[5:]

for i in range (total_student):
    students[i] = students[i].split(",")

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]
for s in students:
    for i in range (5,16):
        if s[i] == "-1":
            not_take_exam[i-5] += 1

not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]
for i in range (0,11):
    not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student, 2)

#import matplotlib.pyplot as plt
import numpy as np


#print(not_take_exam_percentage)

