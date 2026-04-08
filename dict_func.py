# Write your code here!
def employee_print(employee_info):
    if "Name" in employee_info:
        print("Name:", employee_info["Name"])
    else:
        print("Name: N/A")

    if "Salary" in employee_info:
        print("Salary:", employee_info["Salary"])
    else:
        print("Salary: N/A")

    if "Role" in employee_info:
        print("Role:", employee_info["Role"])
    else:
        print("Role: N/A")

    other = False

    for key in employee_info:
        if key != "Name" and key != "Salary" and key != "Role":
            print(key + ":", employee_info[key])
            other = True

    if not other:
        print("No other info!")

