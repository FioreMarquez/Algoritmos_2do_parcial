### Ejercicio 1
def f(n:int):
    assert type(n)==int and n>=0, ' debe ingresar un entero positivo'
    if n == 0:
        res = 1
    else:
        res = f(n-1)+ n * f(n-1)
    return res

def g(n:int):
    assert type(n)==int and n >= 0, ' debe ingresar un entero positivo'
    if n ==1:
        res = 2
    else:
        res = 2 * g(n-1) + 3* n
    return res

# -------------------------------
# Tests para f(n)
# -------------------------------

assert f(0) == 1
assert f(1) == 2      # 1 + 1*1 = 2
assert f(2) == 6      # 2 + 2*2 = 6
assert f(3) == 24     # 6 + 3*6 = 24
assert f(4) == 120

# -------------------------------
# Tests para g(n)
# -------------------------------

assert g(1) == 2
assert g(2) == 10     # 2*2 + 3*2 = 10
assert g(3) == 29     # 2*10 + 3*3 = 29
assert g(4) == 70     # 2*29 + 3*4 = 70

print("Todos los tests pasaron correctamente")

### Ejercicio 2
""""
Definir una función `potencia(a, n)` que:

- reciba un número `a` y un entero no negativo `n`
- devuelva $ a^n $ usando recursión

Ejemplo de uso: `potencia(2, 3) #8`

Requisitos:
- Definir correctamente el caso base
- No usar el operador `**`
"""

#codigo
def potencia(a,n:int):
    assert type(a) == type(n) == int and n>=0, 'debe ingresar un numero a y un numero no negativo n'
#caso base
    if n== 0:
        pot = 1
    else:
        pot = a * potencia(a, n-1)
    return pot

#test
print(potencia(2,3))#devuelve 8


#Ejercicio 3:
#Se pide implementar de forma recursiva las siguientes funciones.
"""
1. Definir una función f(n) que:
   - reciba un entero n
   - cumpla la siguiente definición:
     f(n) = 0                          si n = 0
     f(n) = 1                          si n = 1
     f(n) = 3f(n-1) - f(n-2) + 1       si n > 1

Requisitos:
   - Usar únicamente recursión
   - No usar ciclos (for, while)
   - Validar que n sea un entero mayor o igual a 0
"""
#codigo
def f(n:int):
    assert type(n)==int, 'debe ingresar un numero entero no negativo'
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = 3 * f(n-1) - f(n-2) +1
    return res

""""
definir una funcion g(n) que:
- reciba un entero n
- cumpla la siguiente definicion:
g(n)=0                                     si n = 1
g(n)= 1                                    si n = 2  
g(n)=3                                     si n = 3
g(n)= g(n-1) + g(n-2) + n* g(n-3)          si n > 3
"""
#codigo
def g(n:int):
    assert type(n)== int and n>=0, ' debe ingrear un numero entero no negativo'
    if n== 1:
        res = 0
    elif n == 2:
        res = 1
    elif n ==3:
        res = 3
    else:
        res = g(n-1) + g(n-2) + n * g(n-3)
    return res
    # -------------------------------
# Tests para f(n)
# -------------------------------

assert f(0) == 0
assert f(1) == 1
assert f(2) == 4     # 3*1 - 0 + 1 = 4
assert f(3) == 12    # 3*4 - 1 + 1 = 12
assert f(4) == 33
assert f(5) == 88

# Resultado pedido
#assert f(8) == 1531

# -------------------------------
# Tests para g(n)
# -------------------------------

assert g(1) == 0
assert g(2) == 1
assert g(3) == 3
assert g(4) == 4     # 3 + 1 + 4*0 = 4
assert g(5) == 12    # 4 + 3 + 5*1 = 12
assert g(6) == 30

# Resultado pedido
assert g(8) == 228

print("Todos los tests pasaron correctamente")

### Ejercicio 4
""""
Se pide implementar una función que calcule la suma de los dígitos de un número utilizando recursión. Definir una función `suma_digitos(n)` que:

- reciba un entero positivo `n`
- devuelva la suma de todos sus dígitos

Ejemplo de uso: `suma_digitos(1234)  # 1 + 2 + 3 + 4 = 10`
"""

# codigo
def suma_digitos(n:int):
    assert isinstance (n, int) and n >= 0, ' debe ingresar un entero no negativo'
#caso base
    if n < 10:
        return n
#caso recursivo:
    else:

        ultimo_digito = n % 10
        return ultimo_digito + suma_digitos(n//10)

#test
print(suma_digitos(1234))

#falta ej 5

#Ejericio 6
# codigo
def fib(n):
    assert type(n)== int and n>= 0, ' debe ingresar un numero entero'
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib (n-1) + fib(n-2)
    return res

#tests
assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
assert fib(7) == 13

print("Todos los tests pasaron correctamente")

#ejericio 7
#ver

#ejercicio 8
 #codigo
def cantidad_divisores(n, i = 1):
    if i > n:
        return 0
    if n % i ==0 :
        return 1 + cantidad_divisores(n, i+1)
    return cantidad_divisores(n, i+1)

#test

#ejercicio 11
# codigo
def contiene(elem, lista):
    assert type(lista)== list, ' debe ingresar una lista'
   
    if lista == []:
        return False
    if lista[0]== elem:
        return True
    else: 
         return contiene(elem, lista[1:])

#test
assert contiene(1, [1, 2, 3]) == True
assert contiene(3, [1, 2, 3]) == True
assert contiene(4, [1, 2, 3]) == False
assert contiene(5, []) == False
print("Todos los tests pasaron correctamente")