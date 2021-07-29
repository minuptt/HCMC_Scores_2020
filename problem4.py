import matplotlib.pyplot as plt
import numpy as np
# read file
with open("/Users/thiphan/Desktop/HCMC_scores/HCMC_scores_2020/clean_data.csv", encoding="utf8") as file:
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

# number of students who took 0,1,2,3,... subjects
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	count = 0
	for i in range(11):
		if s[i+5] != "-1":
			count += 1

	num_of_exam_taken[count] += 1

num_of_exam_taken_percentage = [0,0,0,0,0,0,0,0,0,0,0,0]

# convert to percentage
for i in range (0,11):
    num_of_exam_taken_percentage[i] = round(num_of_exam_taken[i]*100/total_student, 2)

# Draw pie chart

sizes = num_of_exam_taken
labels = ['0 sbj - ', '1 sbj - ', '2 sbj - ', '3 sbj - ', '4 sbj - ', '5 sbj - ', '6 sbj - ', '7 sbj - ', '8 sbj - ', '9 sbj - ', '10 sbj - ', '11 sbj - ']

mylabels = [str(labels[i]) + str(num_of_exam_taken_percentage[i]) for i in range (len(labels))]


mycolor = np.random.rand(len(sizes), 3)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors = mycolor, pctdistance = 1.2, startangle=90)
plt.title("Number of subjects that students took exam")
plt.legend(labels = mylabels, loc = "center right", bbox_to_anchor = (1,0.5), bbox_transform = plt.gcf().transFigure)
plt.tight_layout()
plt.show()
