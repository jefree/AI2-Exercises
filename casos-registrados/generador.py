from arbol import Arbol

def buscar_promedio(lista, atributo=0):

    lista = sorted(lista, key= lambda e: e[atributo])

    indice_medio = len(lista)/2
    indice_medio = indice_medio-1 if(indice_medio % 1 == 0) else indice_medio
    indice_medio = int(indice_medio)

    medio = lista [indice_medio][atributo]
    siguiente = 0
    
    if (indice_medio < len(lista) -1):
        siguiente = lista[indice_medio+1][atributo]

        while(medio == siguiente and indice_medio+1 < len(lista) -1):
            indice_medio += 1
            medio = siguiente

            siguiente = lista[indice_medio+1][atributo]

    return (medio+siguiente)/2.0, lista, indice_medio+1

def comparar_clases(lista):

    if (len(lista) == 0):
        return True, 'None'

    clases = [ e[len(lista[0])-1] for e in lista ]

    iguales = True
    clase_actual = clases[0]

    for clase in clases[1:]:
        if (clase != clase_actual):
            iguales = False
            break

    return iguales, clase_actual

def construir_arbol(lista, atributo, nodo):
    clase_unica, clase = comparar_clases(lista)

    if (clase_unica):
        nodo.valor = clase
        return nodo

    promedio, lista, indice_medio = buscar_promedio(lista, atributo)

    if (atributo == len(lista[0])-2):
        atributo = 0
    else:
        atributo += 1

    nodo.valor = promedio

    nodo_izq = construir_arbol(lista[:indice_medio], atributo, Arbol.Nodo())
    nodo_der = construir_arbol(lista[indice_medio:], atributo, Arbol.Nodo())

    nodo.hijos.append(nodo_izq)
    nodo.hijos.append(nodo_der)

    return nodo

def crear_arbol(lista):

    arbol = Arbol()
    construir_arbol(lista, 0, arbol.raiz)

    return arbol
