import pandas as pd

employee_data = {
    "Employee ID": ["161E90", "161F91", "161F99", "171E20", "171G30"],
    "Name": ["Raman", "Himadri", "Jaya", "Tejas", "Ajay"],
    "Age": [41, 38, 51, 30, 45],
    "Salary (PM)": [56000, 67500, 82100, 55000, 44000]
}

df = pd.DataFrame(employee_data)

search_parameter = int(input("Enter the search parameter (1, 2, or 3): "))

search_value = input("Enter the search value: ")

if search_parameter == 1:
    df_filtered = df[df["Age"] == search_value]
elif search_parameter == 2:
    df_filtered = df[df["Name"] == search_value]
elif search_parameter == 3:
    operator = input("Enter the operator (>, <, <=, >=): ")
    df_filtered = df[df["Salary (PM)"] ,operator, search_value]
else:
    print("Invalid search parameter.")
    exit()

print(df_filtered)
