"""
Sistema de Farmacia
Este programa implementa un sistema para gestionar medicamentos, clientes y recetas médicas.

Clases principales:
- Medicamento: Representa un medicamento en la farmacia
- Receta: Representa una receta médica
- Cliente: Representa un cliente de la farmacia
- Farmacia: Clase principal que coordina todas las operaciones
"""

from datetime import datetime
from typing import List, Dict

class Medicamento:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def actualizar_stock(self, cantidad: int) -> bool:
        if self._stock + cantidad >= 0:
            self._stock += cantidad
            return True
        return False

    def hay_stock(self, cantidad: int) -> bool:
        return self._stock >= cantidad

    def __str__(self) -> str:
        return f"{self._nombre} - ${self._precio:.2f} (Stock: {self._stock})"

class Receta:
    def __init__(self, cliente: 'Cliente', medicamentos: List[Medicamento], fecha: datetime):
        self._cliente = cliente
        self._medicamentos = medicamentos
        self._fecha = fecha
        self._estado = "Pendiente"

    def procesar(self) -> bool:
        # Verificar stock de los medicamentos
        for medicamento in self._medicamentos:
            if not medicamento.hay_stock(1):
                return False  # No hay stock suficiente

        # Actualizar stock de los medicamentos
        for medicamento in self._medicamentos:
            medicamento.actualizar_stock(-1)

        self._estado = "Procesada"
        return True

    def __str__(self) -> str:
        resultado = f"Receta de {self._cliente._nombre} - Fecha: {self._fecha.strftime('%Y-%m-%d')}\n"
        resultado += "Medicamentos:\n"
        for medicamento in self._medicamentos:
            resultado += f"- {medicamento._nombre}\n"
        resultado += f"Estado: {self._estado}"
        return resultado

class Cliente:
    def __init__(self, nombre: str, email: str, direccion: str):
        self._nombre = nombre
        self._email = email
        self._direccion = direccion
        self._recetas: List[Receta] = []

    def realizar_receta(self, medicamentos: List[Medicamento]) -> bool:
        receta = Receta(self, medicamentos, datetime.now())
        if receta.procesar():
            self._recetas.append(receta)
            return True
        return False

    def __str__(self) -> str:
        return f"{self._nombre} ({self._email})"

class Farmacia:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._medicamentos: Dict[str, Medicamento] = {}
        self._clientes: List[Cliente] = []

    def agregar_medicamento(self, medicamento: Medicamento) -> None:
        self._medicamentos[medicamento._codigo] = medicamento

    def registrar_cliente(self, cliente: Cliente) -> None:
        self._clientes.append(cliente)

    def mostrar_catalogo(self) -> None:
        print(f"\nCatálogo de {self._nombre}")
        for medicamento in self._medicamentos.values():
            print(medicamento)

def main():
    # Crear farmacia
    farmacia = Farmacia("Farmacia Saludable")

    # Agregar medicamentos
    medicamentos = [
        Medicamento("M001", "Paracetamol", 2.50, 100),
        Medicamento("M002", "Ibuprofeno", 3.00, 50),
        Medicamento("M003", "Amoxicilina", 5.00, 30)
    ]
    for medicamento in medicamentos:
        farmacia.agregar_medicamento(medicamento)

    # Crear cliente
    cliente = Cliente("Carlos López", "carlos.lopez@email.com", "Av. Las Américas")
    farmacia.registrar_cliente(cliente)

    # Mostrar catálogo inicial
    print("Catálogo inicial:")
    farmacia.mostrar_catalogo()

    # Cliente realiza una receta con medicamentos
    if cliente.realizar_receta([medicamentos[0], medicamentos[1]]):  # Paracetamol e Ibuprofeno
        print("\nReceta realizada con éxito.")
    else:
        print("\nNo hay stock suficiente para realizar la receta.")

    # Mostrar catálogo después de la receta
    print("\nCatálogo después de la receta:")
    farmacia.mostrar_catalogo()

    # Verificar las recetas del cliente
    print("\nRecetas del cliente:")
    for receta in cliente._recetas:
        print(receta)

if __name__ == "__main__":
    main()
