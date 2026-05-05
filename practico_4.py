#ejericios  del practico 4 de algoritmos

#ejercicio 1
#Definir una función `contar_letras(texto)` que:

#- reciba una cadena de caracteres
#- ignore los espacios
#- devuelva un diccionario donde:
# - cada clave sea una letra
# - cada valor sea la cantidad de veces que aparece en el texto
  
#Ejemplo:
#```python
#contar_letras("hola hola") 
# {'h': 2, 'o': 2, 'l': 2, 'a': 2}
#```

#codigo
def contar_letras(texto:str):
    resultado = {}

    for letra in texto:
        if letra!= " ":
            if letra in resultado:
               resultado[letra] += 1
            else: 
                resultado[letra] = 1
    return resultado



#tests
assert contar_letras("hola hola") == {'h': 2, 'o':2, 'l':2, 'a':2}
assert contar_letras("") == {}

