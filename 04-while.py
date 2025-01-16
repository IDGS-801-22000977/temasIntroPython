'''x =0
while x<10:
    print(x)
    x=x+1 
'''
'''operacion de multiplicacion de a x b utilizando sumas 
    a=3
    b=4
    salida : 3+3+3+3=12
'''
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

salida = 0 
contador = 0  
suma_detalle = ""  

while contador < b:
    salida += a
    suma_detalle += f"{a} + " if contador < b - 1 else f"{a}"  
    contador += 1

print(f"La suma de {suma_detalle} es {salida}")


    
    