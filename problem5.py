import matplotlib.pyplot as plt
import numpy as np

# read file
with open("clean_data.csv", encoding="utf8") as file:
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

lastname = [] # last name list 
lastname_count = [] # total of each last name list

for s in students:
	s_name = s[1].split(" ")
	s_lastname = s_name[0]
	if s_lastname not in lastname:
		lastname.append(s_lastname)
		lastname_count.append(0)
		lastname_count[lastname.index(s_lastname)] += 1
	else:
		lastname_count[lastname.index(s_lastname)] += 1

counted_max_num = [] # list of the number of last name reprtition by descending order
sort_index = [] # list of index 

# create counted_max_num, ist of the number of last name reprtition by descending order
for i in range(len(lastname)):
	max_number = 0
	for j in range(len(lastname)):
		if lastname_count[j] > max_number and lastname_count[j] not in counted_max_num:
			max_number = lastname_count[j]
	counted_max_num.append(max_number)

# create sort_index to sort by descending order
for max_num in counted_max_num:
	for i in range(len(lastname)):
		if lastname_count[i] == max_num and i not in sort_index:
			sort_index.append(i)

lastname_sorted = [] # sorted list of last name
lastname_count_sorted = [] # sorted list of the number of last name reprtition by descending order

# re-sort list of last name and the number of last name reprtition by descending order
for index in sort_index:
	lastname_sorted.append(lastname[index])
	lastname_count_sorted.append(lastname_count[index])

# draw chart

num = 10 # the 10 most common last names 

x = np.arange(num)
y = np.arange(num)

fig, axis = plt.subplots()
rects = axis.patches

# for 10 common last name
plt.bar(x, lastname_count_sorted[0:num])
# label for column x
plt.xticks(x, lastname_sorted[0:num])

axis.set_ylabel('Number of Student')
axis.set_xlabel('Last names')


#  chart labels
labels_ln = lastname_count_sorted[0:num]
for rect, label in zip(rects, labels_ln):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')

plt.title(str(num) + ' most common last names in the exam at HoChiMinh City')


plt.show()
