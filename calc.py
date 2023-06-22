while True:
    print('Welcome to Calculator')
    oper1 = int(input('Write First Number:\n'))
    operator = input('Write operator(+, -, *, /)\n')
    oper2 = float(input('Write Second Number: \n'))
    if operator == "+":
        result = oper1 + oper2
    if operator == "-":
        result = oper1 - oper2
    if operator == "*":
        result = oper1 * oper2
    if operator == "/":
        result = oper1 / oper2
    print(result)
    choise = input('You want to quit?(y/n)')
    if choise == 'y':
        break