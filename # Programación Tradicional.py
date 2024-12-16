# Programación Tradicional
def ingresar_temperaturas_tradicional():
    """Función para ingresar temperaturas diarias en programación tradicional."""
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1} (Tradicional): "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio_tradicional(temperaturas):
    """Función para calcular el promedio semanal en programación tradicional."""
    return sum(temperaturas) / len(temperaturas)

def promedio_clima_tradicional():
    """Gestión del promedio semanal del clima utilizando programación tradicional."""
    print("\n--- Promedio Semanal del Clima (Tradicional) ---")
    temperaturas = ingresar_temperaturas_tradicional()
    promedio = calcular_promedio_tradicional(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Programación Orientada a Objetos (POO)
class ClimaSemanal:
    """Clase para gestionar el promedio semanal del clima."""
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Método para ingresar temperaturas diarias."""
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1} (POO): "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """Método para calcular el promedio semanal."""
        return sum(self.temperaturas) / len(self.temperaturas)

def promedio_clima_poo():
    """Gestión del promedio semanal del clima utilizando programación orientada a objetos."""
    print("\n--- Promedio Semanal del Clima (POO) ---")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Menú Principal
def menu_principal():
    """Menú principal para seleccionar el paradigma a utilizar."""
    while True:
        print("\nSeleccione el enfoque para calcular el promedio semanal del clima:")
        print("1. Programación Tradicional")
        print("2. Programación Orientada a Objetos (POO)")
        print("3. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            promedio_clima_tradicional()
        elif opcion == "2":
            promedio_clima_poo()
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu_principal()
