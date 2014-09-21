from generador import crear_arbol, generar_reglas
from aprendiz import determinar_clase, probar_reglas_para
from cargador import cargar_datos

def main():

    cab = ['A', 'B', 'C']

    datos = [[3, 5, 1, 'A'],
             [5, 4, 2, 'B'],
             [2, 2, 2, 'C'],
             [1, 2, 3, 'C'],
             [5, 3, 4, 'A'],
             [6, 7, 5, 'B'],
             [3, 8, 6, 'A'],
             [2, 9, 8, 'B'],]

    cab, datos = cargar_datos('data.cvs')
    
    arbol = crear_arbol(datos)

    reglas = []
    generar_reglas(arbol.raiz, cab, 0, '', reglas)

    correctos = probar_reglas_para(datos, arbol)

    print ('porcentaje de datos correctos: ' + str(correctos*100) + '%') 

if __name__ == '__main__':
    main()