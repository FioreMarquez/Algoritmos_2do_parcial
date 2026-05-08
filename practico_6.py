## Ejercicio 1

#En este ejercicio vas a implementar una clase que represente un personaje de un videojuego.

#1. Definir una clase `Personaje` con los siguientes atributos:

#- Atributos (públicos)
"""
    - `nombre`: nombre del personaje (`str`)
    - `salud`: cantidad de vida del personaje (`int`)
    - `nivel`: nivel del personaje (`int`)

- Constructor: Implementar el método `__init__` que:

    - reciba `nombre`, `salud` y `nivel`
    - inicialice los atributos correspondientes
    - valide:
        - que `nombre` sea un `str`
        - que `salud` sea un entero mayor o igual a 0
        - que `nivel` sea un entero mayor o igual a 1

- Implementar los siguientes métodos:

    - `subir_nivel() -> None`  Incrementa el nivel del personaje en 1.

    - `recibir_danio(danio: int) -> None` Reduce la salud del personaje en la cantidad indicada.

    - Requisitos:
        - validar que `danio` sea un entero positivo
        - si la salud resultante es menor o igual a 0:
            - establecer la salud en 0
            - imprimir: `"El personaje ha sido derrotado"`

- Método especial

    - `__str__() -> str`  
  Debe devolver un string con el estado del personaje en el siguiente formato:

```python
"Nombre: Link | Salud: 80 | Nivel: 5"
``` 
Restricciones
- Usar assert para validar entradas
- No permitir valores inválidos (salud negativa, nivel menor a 1, etc.)
- Escribir código claro y legible
"""
#Codigo
Class
#hola esto se sube

