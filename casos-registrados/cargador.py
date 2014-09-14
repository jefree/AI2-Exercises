def cargar_archivo(nombre_archivo):

    contenido = None

    with open(nombre_archivo) as archivo:
        contenido = archivo.read()

    return contenido

def analizar_contenido(contenido):
    contenido = contenido.split('\n')
    datos = []

    for linea in contenido[1:-1]:
        elem = linea.split(',')

        for i in range(len(elem)-1):
            elem[i] = float(elem[i])

        datos.append(elem)

    cab = contenido[0].split(',')

    return cab, datos

def cargar_datos(nombre_archivo):
    c = cargar_archivo(nombre_archivo)
    return analizar_contenido(c)
