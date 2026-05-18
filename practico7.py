#ejercicio 1
# codigo
def crear_archivo(nombre:str):
    archivo = open(nombre, 'w')
    archivo.write("hola\n")
    archivo.write("Bienvenidos a Algoritmos y programación\n")
    archivo.write("python es divertido\n")
    archivo.close()

    
#ejercicio 2
def leer_archivo(nombre:str):
    try:
        archivo = open(nombre, 'r')
        contenido = archivo.read()
        print(contenido)
        archivo.close()
        return contenido
    except:
        return "ERROR"

#ejercicio 3
def contar_lineas(nombre:str):
       
    try:
        with open(nombre, 'r') as archivo:
            lineas = archivo.readlines()

        return len(lineas)

    except:
        return -1



