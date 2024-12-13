def decimal_to_ternary(num):
    if num == 0:
        return "0"
    tern = ""
    is_negative = num < 0
    num = abs(num)
    while num > 0:
        tern = str(num % 3) + tern
        num //= 3
    return "-" + tern if is_negative else tern

def main():
    try:
        dec = int(input("Введите десятичное число: "))

        tern = decimal_to_ternary(dec)

        print(f"Троичное представление: {tern}")
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()




