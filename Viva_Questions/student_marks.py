# Python Program to Calculate Total Marks Percentage and Grade of a Student

print("Enter the marks of five subjects::")

subject_1 = float (input ())
subject_2 = float (input ())
subject_3 = float (input ())
subject_4 = float (input ())
subject_5 = float (input ())

total, average, percentage, grade = None, None, None, None

# It will calculate the Total, Average and Percentage
total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average = total / 5.0
percentage = (total / 500.0) * 100

# It will produce the final output
print ("\nThe Total marks is:   \t", total, "/ 500.00")
print ("\nThe Percentage is:    \t", percentage, "%")
