class Cine:
    precio_boleto = 12 
    archivo_ventas = "VENTAS.txt"
    ventas = []

    def __init__(self):
        self.precio_boleto
        self.archivo_ventas
        self.ventas  # Almacena las ventas
        self.limpiar_archivo()

    def limpiar_archivo(self):
        with open(self.archivo_ventas, "w") as archivo:
            archivo.write("")  # Vacía el archivo al iniciar el programa

    def calcular_descuento(self, total, boletos):
        if boletos > 5:
            return total * 0.85
        elif 3 <= boletos <= 5:
            return total * 0.90
        else:
            return total

    def validar_boletos(self, personas, boletos):
        return boletos <= personas * 7

    def guardar_venta(self, nombre, total):
        self.ventas.append((nombre, total))  # Guarda los datos como tupla
        with open(self.archivo_ventas, "a") as archivo:
            archivo.write(f"{nombre}: ${total:.2f}\n")  # Escribe cada venta al archivo

    def mostrar_resumen_ventas(self):
        if not self.ventas:
            print("No se realizaron ventas.")
        else:
            print("\n--- Resumen de Ventas ---")
            print(f"{'Nombre':<20}{'Total a Pagar'}")
            print("-" * 30)

            total_general = 0
            for nombre, total in self.ventas:
                print(f"{nombre:<20}${total:.2f}")
                total_general += total

            print("-" * 30)
            print(f"{'Total General':<20}${total_general:.2f}")

    def entrada_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Entrada no válida. Ingrese un número entero.")

    def procesar_compra(self):
        while True:
            print("\n--- Boletos ---")
            nombre = input("Nombre del comprador: ")
            personas = self.entrada_entero("Cantidad de personas: ")
            boletos = self.entrada_entero("Cantidad de boletos: ")

            while not self.validar_boletos(personas, boletos):
                print("Cantidad de boletos no válida (máximo 7 por persona).")
                ajuste = input("¿Desea ajustar la cantidad de personas o boletos? (p/b): ").strip().lower()
                if ajuste == "p":
                    personas = self.entrada_entero("Ingrese la nueva cantidad de personas: ")
                elif ajuste == "b":
                    boletos = self.entrada_entero("Ingrese la nueva cantidad de boletos: ")
                else:
                    print("Opción no válida. Intente otra vez.")

            total = self.precio_boleto * boletos
            total_con_descuento = self.calcular_descuento(total, boletos)

            print(f"Total con descuento aplicado: ${total_con_descuento:.2f}")
            metodo_pago = input("¿Método de pago? (efectivo/tarjeta CINECO): ").strip().lower()

            if metodo_pago == "t":
                total_con_descuento *= 0.90

            print(f"Total a pagar: ${total_con_descuento:.2f}")
            self.guardar_venta(nombre, total_con_descuento)

            continuar = input("¿Desea realizar otra compra? (s/n): ").strip().lower()
            if continuar != 's':
                break

        self.mostrar_resumen_ventas()

    def menu_principal(self):
        opcion = input("¿Desea realizar compras o salir? (c/s): ").strip().lower()
        if opcion == "c":
            self.procesar_compra()
        elif opcion == "s":
            print("Saliendo...")
        else:
            print("Opción no válida. Intente nuevamente.")
            self.menu_principal()

if __name__ == "__main__":
    cine = Cine()
    cine.menu_principal()
