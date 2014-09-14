def recorrer_arbol(elem, nodo, atr):
    if (type(nodo.valor) == str):
        return nodo.valor
    else:
        nuevo_atr = (atr+1) % (len(elem))

        if (elem[atr] > nodo.valor):
            return recorrer_arbol(elem, nodo.hijos[1], nuevo_atr)
        else:
            return recorrer_arbol(elem, nodo.hijos[0], nuevo_atr)

def determinar_clase(elem, arbol):
    return recorrer_arbol(elem, arbol.raiz, 0)
