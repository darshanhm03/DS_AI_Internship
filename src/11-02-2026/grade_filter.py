import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

missing_values = grades.isnull()

filled_grades = grades.fillna(0)

passed_students = filled_grades[filled_grades >=60]

print("Original Series:")
print(grades)

print("\nMissing Values (True = Missing):")
print(missing_values)

print("\nSeries after filling missing values with 0:")
print(filled_grades)

print("\nScores greater than 60:")
print(passed_students)
