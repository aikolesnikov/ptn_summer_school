print("Input operation and two digits")
while True:
    op = raw_input()
    if op == 'q':
        break
    # else:
    else:
        if not (op == '+' or op == '-' or op == '*' or op == '/'):
            continue
        else:
            first_digit = input()
            second_digit = input()
            if op == '+':
                result = first_digit + second_digit
            elif op == '-':
                result = first_digit - second_digit
            elif op == '*':
                result = first_digit * second_digit
            elif op == '/':
                result = first_digit / second_digit
            print("result:", result)
