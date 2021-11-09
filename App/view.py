"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

UFOfile = 'UFOS-utf8-small.csv'
cont = None

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de avistamientos")
    print("3- Consultar avisatamientos en una ciudad")
    print("4- Consultar avistamientos por duracion")
    print("5- Consultar avistamientos por hora/min")
    print("6- Consultar avistamientos en un rango de fechas")
    print("7- Contar avistamientos en una zona geografica")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de avistamientos ....")
        controller.loadData(cont, UFOfile)
        print('UFOs cargados: ' + str(controller.UFOsSize(cont)))
        print("\nPrimeros 5 avistamientos: ") 
        controller.printFirstTotals(cont)
        print("\nUltimos 5 avistamientos: ") 
        controller.printLastTotals(cont)

    elif int(inputs[0]) == 3:
        print('Se econtraron ' + str(controller.indexSize(cont['cityIndex'])) + ' ciudades con avistamientos')
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))

    elif int(inputs[0]) == 4:
        print('Elementos en el arbol: ' + str(controller.indexSize(cont['durationIndex'])))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))


    else:
        sys.exit(0)
sys.exit(0)
