Student Performance Report System Using Python

Overview
This project is a simple student performance analysis system built using Python with the Pandas and NumPy libraries. The program stores marks of students in multiple subjects, calculates their average score, determines pass or fail status, assigns grades, and generates different reports based on the data.

This project demonstrates how Python can be used for basic data analysis tasks which are common in data science workflows.

Technologies Used
Python
Pandas
NumPy

Dataset
The dataset contains student names and their marks in three subjects.

Subjects included in the analysis
Maths
Science
English

Features
Creation of a structured dataset using a Pandas DataFrame
Calculation of student average marks across subjects
Automatic rounding of averages for cleaner output
Pass or fail detection based on the average score
Grade assignment based on defined score ranges
Identification of failed students
Display of students with high average scores
Filtering students who scored below 40 in Science
Display of Grade A students

Grading System
Grades are assigned based on the average marks of each student.

Average greater than or equal to 85 results in Grade A
Average greater than or equal to 70 and less than 85 results in Grade B
Average greater than or equal to 60 and less than 70 results in Grade C
Average below 60 results in Grade D

Project Workflow
Student data is stored in Python lists
The lists are combined into a dictionary structure
A Pandas DataFrame is created from the dictionary
The average score of each student is calculated
The result column identifies whether a student passed or failed
Grades are assigned using conditional logic with NumPy
Different filtered reports are printed from the dataset

Learning Outcome
This project helps in understanding important data analysis concepts such as DataFrame creation, column operations, conditional filtering, and simple reporting systems. These concepts are widely used in real data science tasks when analyzing datasets.

Author
Uday Bhaskar
Aspiring Data Science learner working with Python, NumPy, and Pandas.
