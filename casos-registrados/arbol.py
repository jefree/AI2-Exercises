class Arbol():

    class Nodo():
        def __init__(self):
            self.hijos = []

        def imprimir(self, profundidad):

            cadena = str(self.valor)

            for hijo in self.hijos:
                cadena += '\n' +  '  '*profundidad +'|--'
                cadena += hijo.imprimir(profundidad+1);

            return cadena

        def __str__(self):
            return self.imprimir(0)
            
    def __init__(self):
        self.raiz = self.Nodo()

    def __str__(self):
        return self.raiz.__str__()
