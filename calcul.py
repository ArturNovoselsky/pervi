def get_operator():
    while True:
        operator = input("Введите оператор (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Неверный оператор! Введите один из: +, -, *, /")

def get_numbers():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            return num1, num2
        except ValueError:
            print("Неверный ввод! Попробуйте еще раз.")

def calculate(operator, num1, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Деление на ноль невозможно"
        else:
            result = num1 / num2
    return result

while True:
    operator = get_operator()
    num1, num2 = get_numbers()
    result = calculate(operator, num1, num2)
    print("Результат:", result)

    again = input("Хотите продолжить? (да/нет): ")
    if again.lower() != 'да':
        break