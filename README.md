# HCMC_Scores_2020

## Introduction

The dataset in this project was collected by Dung Lai (https://github.com/DungLai) on http://diemthi.hcm.edu.vn website. This dataset talks about the scores of all high school students in the National High School Exam at HoChiMinh City in 2020. 
The dataset includes 74,445 students and 16 columns (Std_ID, Name, dd, mm, yy, Math, Literature, Social Sciences, Natural Sciences, History, Geography, Humanities, Biography, Physic, Chemisty, English).
With 11 subjects, each student has to choose any 6 subjects to take an exam. 
    For example: 
      - Student A: Math, Physic, Chemistry, Natural Sciences, Literature and English
      - Student B: Math, Literature, English, History, Geography, Humanities
The subjects which the students didn't pick will have "-1".

The raw data is the text file (raw_data.txt) with html character codes. We have to process and ingest the raw data to the clean data and save it to clean_data.csv. After we have the clean data file, we use it to analyze the data.

## Tasks

# Problem 1: 
Plot bar chart for the subjects that student was not take exam or register
# Problem 2: 
Every student can choose the number of different subjects to take the exam. For 11 subjects, we have 11 categories and the minimum of subject is 0 and the maximum of subjects is 11. For example: student A chooses 4 subjects (Math, Physic, Chemistry and English), student B chooses 6 subjects (English, Literature, History, Geography, Math, Humanities). Find number of students who took 0, 1, 2 ... subjects and the average scores they made for each category. Plot bar chart that shows the relationship of them.
# Problem 3: 
Let seperate the age by 10 categories (18, 19, 20, ..., 26 and over 26). Find total of students for each category and average score by age. Draw 2 charts at the same diagram.
# Problem 4: 
Draw pie chart that shows total number of subjects that each student took exam.
# Problem 5: 
Draw the bar chart to show the 10 most common last names in the exam at HoChiMinh City
# Problem 6: 
Find the 10 most common first names and show them on chart
# Problem 7: 
Find the longest full name 

### P.S.: We can not upload the raw data file to github because it is huge. 
Here is the link: 
    https://drive.google.com/file/d/1X9VCJGmt5PY7Z8dOO39PeAS6G3xCyKut/view?usp=sharing
