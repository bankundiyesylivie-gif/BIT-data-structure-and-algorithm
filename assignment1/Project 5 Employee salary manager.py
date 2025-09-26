
# Employee Salary Man

import array

# === Integers ===
salaries = [42000, 51000, 60000, 39000, 47000]  # integer values for employee salaries
total_salary = sum(salaries)
average_salary = total_salary / len(salaries)
min_salary = min(salaries)
max_salary = max(salaries)

print("=== Integer Calculations ===")
print(f"Total: {total_salary}, Average: {average_salary}, Min: {min_salary}, Max: {max_salary}\n")

# === Strings (f-strings) ===
report = (
    f"Employee Salary Report\n"
    f"Total salary payout = {total_salary}\n"
    f"Average salary = {average_salary:.2f}\n"
)
print("=== String Report ===")
print(report)

# === Booleans ===
threshold = 45000
if average_salary > threshold and max_salary > 50000:  # compound condition
    status = "Above Standard"
else:
    status = "Below Standard"

print("=== Boolean Status ===")
print(f"Status: {status}\n")

# === Lists ===
print("=== List Operations ===")
print("Original salaries:", salaries)

salaries.append(53000)  # add new element
print("After adding 53000:", salaries)

# remove one salary based on condition (remove salaries below 40000)
salaries = [s for s in salaries if s >= 40000]
print("After removing <40000:", salaries)

salaries.sort()
print("After sorting:", salaries, "\n")

# === Arrays ===
print("=== Array Operations ===")
salary_array = array('i', [42000, 51000, 60000])  # fixed-size subset
array_sum = sum(salary_array)

print("Array elements:", salary_array.tolist())
print("Sum of array:", array_sum)
print("Compare with salaries list sum:", sum(salaries), "\n")

# === Dictionaries ===
print("=== Dictionary Records ===")
employee_records = [
    {"id": 1, "name": "Alice", "value": 42000},
    {"id": 2, "name": "Bob", "value": 51000},
    {"id": 3, "name": "Charlie", "value": 60000},
]

# update one record
employee_records[1]["value"] = 55000  # Bob got a raise

# delete one record (Charlie leaves)
employee_records = [emp for emp in employee_records if emp["id"] != 3]

# compute total of 'value'
dict_total = sum(emp["value"] for emp in employee_records)

print("Updated records:", employee_records)
print("Total value from records:", dict_total)


