print("Project Title: Student Result Management System")

#Objective
#Build a simple Python console application using the topics you have learned this week.
#Project Requirements
# Create a Python program that performs the following tasks:

print("1. Student Information")

student_name = input("Please Enter Student Name: ")
student_id = input("Please Enter Student ID: ")
department = input("Please Enter Department: ")


print("2. Subject Marks")


#List of subject 

subjects = ["Python", "Math", "English", "Physics", "ICT"]

# Empty dictionary to store marks
marks = {}


for subject in subjects:
    marks[subject] = int(input(f"Enter Marks for {subject}: "))
    print(f"{subject}: {marks[subject]}")
    


# Display the dictionary
print("Subject Marks:")
print(marks)
   
 
print("3. Calculate Result")

#Use Python's built-in math functions where possible

total_marks = sum(marks.values())
average_marks = total_marks / len(subjects)
highest_marks = max(marks.values())
lowest_marks = min(marks.values())

print(f"Total Marks: {int(total_marks)}")
print(f"Average Marks: {average_marks}")
print(f"Highest Marks: {int(highest_marks)}")
print(f"Lowest Marks: {int(lowest_marks)}")


print("4. Grade Calculation")

#Using if-elif-else, assign grades.



if any(mark < 35 for mark in marks.values()):
    Grade = "F"
    
elif(average_marks >= 80):
   Grade = "A+"
elif(average_marks >=70):
    Grade = "A"
elif(average_marks >=60):
    Grade = "A-"
elif(average_marks >=50):  
    Grade = "B" 
elif(average_marks >=40):
    Grade = "C" 
else:
    Grade = "F"
    

# if marks[subjects[0]] < 35 or marks[subjects[1]] < 35 or marks[subjects[2]] < 35 or marks[subjects[3]] < 35 or marks[subjects[4]] < 35:
#     Grade = "F"
# else:
#     average_marks = total_marks / len(subjects)
    
print(f"Grade: {Grade}")

status = "Pass" 

for mark in marks.values():
    if mark < 35:
        status = "Fail"
        break
    
print(f"Status: {status}")



#Password


correct_password = "python123"

while True:
    password = input("Enter Password: ")

    if password == correct_password:
        print("Correct Password")
        break
    else:
        print("Wrong Password. Try Again.")
        

#String Manipulation

print(student_name.upper())
print(student_name.lower())
print(len(student_name))
print(student_name[:3])
print(student_name[-3:])


# Create two sets.
# sports = {"Football", "Cricket", "Badminton"}
# clubs = {"Programming", "Cricket", "Photography"}
# Display
# ● Common items
# ● All unique items

Sports = {"Football", "Cricket", "Badminton"}
Clubs = {"Programming", "Cricket", "Photography"}

# Display common items
print("Common Items:")
print(Sports.intersection(Clubs))


# Display all unique items
print("All Unique Items:")
print(Sports.union(Clubs))


# Tuple Example
# Create a tuple containing weekdays.
# Display
# ● First day
# ● Last day
# ● Total number of days

tuple_weekdays = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(f"First day: {tuple_weekdays[0]}")
print(f"Last day: {tuple_weekdays[6]}")
print(f"Total number of days: {len(tuple_weekdays)}")

#REPORT DISPLAY

print("========================================")
print("           STUDENT REPORT               ")
print("========================================")

print(f"Student Name: {student_name}")
print(f"Student ID: {student_id}")
print(f"Department: {department}")

print("---------------------------------------------------")

print("Subject Marks:")

for subject in subjects:
    print(f"{subject}: {marks[subject]}")



print("---------------------------------------------------")


print(f"Total Marks: {int(total_marks)}")

print(f"Grade: {Grade}")
print(f"Status: {status}")


print("====================================================")