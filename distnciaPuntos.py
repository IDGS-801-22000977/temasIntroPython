import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, x2, y2):
        return math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)

class CalculadoraDeDistancia:
    
    def calcular_distancia(punto1, punto2):
        return punto1.distancia(punto2.x, punto2.y)

    
    def obtener_coordenadas():
        x = float(input("Ingrese la coordenada x: "))
        y = float(input("Ingrese la coordenada y: "))
        return Punto(x, y)

# Ejemplo de uso
if __name__ == "__main__":
    print("Ingrese las coordenadas del primer punto:")
    punto_a = CalculadoraDeDistancia.obtener_coordenadas()

    print("Ingrese las coordenadas del segundo punto:")
    punto_b = CalculadoraDeDistancia.obtener_coordenadas()
    
    distancia = CalculadoraDeDistancia.calcular_distancia(punto_a, punto_b)
    print(f"La distancia entre los puntos es: {distancia}")
