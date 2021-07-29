# read file
with open("/Users/thiphan/Desktop/HCMC_scores/HCMC_scores_2020/clean_data.csv", encoding = "utf8") as file:
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

import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()
y_pos = np.arange(len(subjects))
axis.set_ylim(0,100)

plt.bar(y_pos, not_take_exam_percentage)
plt.xticks(y_pos, subjects)
plt.ylabel('Percentage')
plt.title('Not taking exam or not registering on subject')

rects = axis.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha = 'center', va = 'bottom')
plt.show()


