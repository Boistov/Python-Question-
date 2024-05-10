def said_input(input_str):
    try:
        number = float(input_str)
        result = number + 2
        print(result)
        return "Number"
    except Error:
        print(" ")
        return "Text"
4
sum  = 0


while True:
    num = input()
    if num == "close":
        print( "Goodbye")
        break
    print(said_input(num))
