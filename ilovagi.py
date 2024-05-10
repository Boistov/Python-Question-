def calculator(num1, num2, operator):
    match operator:
        case '+':
            result = num1 + num2
            print(result)
        case '-':
            result = num1 - num2
            print(result)
        case '*':
            result = num1 * num2
            print(result)
        case '/':
            result = num1 / num2
            print(result)
        case _:
            result = 0

    return result

num1 = int(input())
num2 = int(input())
operator = input()

result = calculator(num1, num2, operator)
if result is not None:
    print(f"Result: {result}")
else:
    print("error")
