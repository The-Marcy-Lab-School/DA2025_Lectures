import pandas as pd

# Sample DataFrames
student_demographics = pd.DataFrame({
    'StudentID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Major': ['Computer Science', 'Mathematics', 'Physics', 'Chemistry']
})

course_enrollments = pd.DataFrame({
    'StudentID': [1, 2, 3, 5], # StudentID 5 is not in demographics
    'CourseName': ['Intro to Python', 'Calculus I', 'Quantum Mechanics', 'Organic Chemistry'],
    'Credits': [3, 4, 3, 4]
})

new_students = pd.DataFrame({
    'StudentID': [5, 6],
    'Name': ['Eve', 'Frank'],
    'Major': ['Biology', 'History']
})

student_contact = pd.DataFrame({
    'Email': ['alice@uni.edu', 'bob@uni.edu', 'charlie@uni.edu', 'david@uni.edu'],
    'Phone': ['555-1111', '555-2222', '555-3333', '555-4444']
}, index=[0, 1, 2, 3]) # Index matches StudentID for join

# Task 1: Concatenate student_demographics and new_students
combined_students = pd.concat([student_demographics,new_students], axis=0, ignore_index=True)
print(combined_students)

# Task 2: Merge student_demographics with course_enrollments (inner join)
merged_data = combined_students.merge(course_enrollments, how = "left")
#print("\n--- Merged Data (inner join) ---")
print(merged_data)


#Task 3: Join student_demographics with student_contact
joined_data = merged_data.join(student_contact)
#print("\n--- Joined Data (index join) ---")
print(joined_data)