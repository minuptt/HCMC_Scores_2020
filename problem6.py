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

name = [] # first name list 
name_count = [] # total of each first name list

for s in students:
	s_stdname = s[1].split(" ")
	s_name = s_stdname[-1]
	if s_name not in name:
		name.append(s_name)
		name_count.append(0)
		name_count[name.index(s_name)] += 1
	else:
		name_count[name.index(s_name)] += 1

counted_max_num = [] # list of the number of first name reprtition by descending order
sort_index = [] # list of index 

# create counted_max_num, ist of the number of first name reprtition by descending order
for i in range(len(name)):
	max_number = 0
	for j in range(len(name)):
		if name_count[j] > max_number and name_count[j] not in counted_max_num:
			max_number = name_count[j]
	counted_max_num.append(max_number)

# create sort_index to sort by descending order
for max_num in counted_max_num:
	for i in range(len(name)):
		if name_count[i] == max_num and i not in sort_index:
			sort_index.append(i)

name_sorted = [] # sorted list of first name
name_count_sorted = [] # sorted list of the number of first name reprtition by descending order

# re-sort list of first name and the number of first name reprtition by descending order
for index in sort_index:
	name_sorted.append(name[index])
	name_count_sorted.append(name_count[index])

# draw chart

num = 10 # the 10 most common first names 

x = np.arange(num)
y = np.arange(num)

fig, axis = plt.subplots()
plt.bar(x, name_count_sorted[0:num])

# label for column x
plt.xticks(x, name_sorted[0:num])

axis.set_ylabel('Number of Students')
axis.set_xlabel('First names')

rects = axis.patches

#  chart labels.
labels = name_count_sorted[0:num]
for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')

plt.title(str(num) + ' most common first names in the exam')
plt.show()
