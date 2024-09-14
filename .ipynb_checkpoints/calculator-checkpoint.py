from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def main():
    user_input = input("Введите выражение: ")
    tokens = user_input.strip().split()
    
    num1_str, operator, num2_str = tokens

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("ошибка!!! Введите корректные числа.")
        return
    
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("ошибка!!! неизвестный оператор.")
        return
    
    print("Результат:", result)

if __name__ == "__main__":
    main()
