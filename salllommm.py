def showEmployee(name, salary):
    result = "Name: {}, Salary: {}".format(name, salary)
    return result

while True:
    a = input()
    if a.lower() == "error":
        break
    salary = 9000
    print(showEmployee(a, salary))
