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

def probar_reglas_para(datos, arbol):

  total = 0
  correctos = 0

  for dato in datos:
    elem = dato[:-1]
    clase = dato[-1]

    total += 1

    if (determinar_clase(elem, arbol) == clase):
      correctos += 1

  return correctos*1.0 / total
