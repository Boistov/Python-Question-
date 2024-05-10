def showEmployee(name, salary):
    result = "Name: {}, Salary: {}".format(name, salary)
    return result

while True:
    a = input()
    if a.lower() == "error":
        break
    salary_input = input()
    print(showEmployee(a, salary_input))
