import os

def funcion1():
    os.system("cls")
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    res = num1 + num2
    print(f"La suma es: {res}")

def funcion2():
    os.system("cls")
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    res = num1 - num2
    print(f"La resta es: {res}")

def funcion3():
    os.system("cls")
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    res = num1 * num2
    print(f"La multiplicación es: {res}")

def funcion4():
    os.system("cls")
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    
    res = num1 / num2
    print(f"La división es: {res}")

def run():
    op = 0
    while op != 5:
        os.system("cls")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        op = int(input("Opción: "))
        
        if op == 1:
            funcion1()
        if op == 2:
            funcion2()
        if op == 3:
            funcion3()
        if op == 4:
            funcion4()
        if op == 5:
            print("Saliendo...")
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    run()
