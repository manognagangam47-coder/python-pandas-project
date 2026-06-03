import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# Display first 5 rows
print("===== FIRST 5 ROWS =====")
print(df.head())

# Display last 5 rows
print("\n===== LAST 5 ROWS =====")
print(df.tail())

# Display data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

# Summary Statistics
print("\n===== SUMMARY STATISTICS =====")
print("Mean Marks:", df["Marks"].mean())
print("Median Marks:", df["Marks"].median())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())
print("Count:", df["Marks"].count())

# Filter students with Marks > 80
high_marks = df[df["Marks"] > 80]

print("\n===== STUDENTS WITH MARKS > 80 =====")
print(high_marks)

# Select specific columns
selected_columns = df[["Name", "Department", "Marks"]]

print("\n===== SELECTED COLUMNS =====")
print(selected_columns)

# Slice first 10 rows
print("\n===== FIRST 10 STUDENTS =====")
print(df.iloc[:10])

# Save filtered data to CSV
high_marks.to_csv("high_marks_students.csv", index=False)

# Save filtered data to Excel
high_marks.to_excel("high_marks_students.xlsx", index=False)

print("\nFiltered data saved successfully!")

