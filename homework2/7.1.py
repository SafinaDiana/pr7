def main():
    try:
        dec = int(input("Введите десятичное число: "))

        dva = bin(dec)[2:]

        vos = oct(dec)[2:]  

        print(f"Двоичное представление: {dva}")
        print(f"Восьмеричное представление: {vos}")
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    