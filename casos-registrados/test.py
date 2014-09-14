import unittest
from generador import *
from arbol import Arbol

class Tests(unittest.TestCase):

    def setUp(self):
        self.datos = [[1, 3, 'A'],
                      [3, 4, 'A'],
                      [2, 5, 'B'],
                      [0.5, 7, 'B']]

    def test_buscar_promedio(self):

        lista_esperada = [[0.5, 7, 'B'],
                          [1, 3, 'A'],
                          [2, 5, 'B'],
                          [3, 4, 'A']]

        self.assertEqual((1.5, lista_esperada, 2), buscar_promedio(self.datos, 0))

    def test_buscar_promedio_especifico(self):

        datos = [[1, 3, 'A'],
                 [2, 5, 'B']]

        datos_esperados =  [[1, 3, 'A'],
                            [2, 5, 'B']]

        self.assertEqual((1.5, datos_esperados, 1), buscar_promedio(datos, 0))
        self.assertEqual((4, datos_esperados, 1), buscar_promedio(datos, 1))

    def test_comparar_clases(self):
        datos_falso = [[1, 3, 'A'],
                        [2, 5, 'B']]

        datos_verdad = [[1, 3, 'B'],
                        [2, 5, 'B']]

        self.assertEqual((False, 'A'), comparar_clases(datos_falso))
        self.assertEqual((True, 'B'), comparar_clases(datos_verdad))
        self.assertEqual((True, 'None'), comparar_clases([]))


    def test_construir_arbol(self):
        arbol = Arbol()
        datos = [[1, 3, 'A'],
                 [2, 5, 'B']]

        resultado = construir_arbol(datos, 0, arbol.raiz)

        self.assertEqual(1.5, arbol.raiz.valor)
        self.assertEqual('A', arbol.raiz.hijos[0].valor)
        self.assertEqual('B', arbol.raiz.hijos[1].valor)


    def test_crear_arbol(self):

        arbol = crear_arbol(self.datos)

        self.assertEqual(1.5, arbol.raiz.valor)

        self.assertEqual(5.0, arbol.raiz.hijos[0].valor)
        self.assertEqual(4.5, arbol.raiz.hijos[1].valor)

        self.assertEqual('A', arbol.raiz.hijos[0].hijos[0].valor)
        self.assertEqual('B', arbol.raiz.hijos[0].hijos[1].valor)

        self.assertEqual('A', arbol.raiz.hijos[1].hijos[0].valor)
        self.assertEqual('B', arbol.raiz.hijos[1].hijos[1].valor)

if __name__ == '__main__':
    unittest.main()
