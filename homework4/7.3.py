def main():
    try:
        a = float(input("Введите значение a: "))
        b = float(input("Введите значение b: "))
        c = float(input("Введите значение c: "))

        x = a * b + 4 * c

        print(f"Результат уравнения (x): {x}")
    except ValueError:
        print("Ошибка: Пожалуйста, введите числовые значения.")

if __name__ == "__main__":
    main()




