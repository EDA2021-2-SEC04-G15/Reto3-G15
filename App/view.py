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
        ciudad = input('Ciudad a buscar: ')
        print('\nSe encontraron ' + str(controller.indexSize(cont['cityIndex'])) + ' ciudades con avistamientos')
        min = controller.findMaxCity(cont['cityIndex'])
        print('La ciudad con mas avistamientos fue: ' + str(min[0]))
        print('Numero de avistamientos en esa ciudad: ' + str(min[1]))
        result = controller.searchByCity(cont['cityIndex'], ciudad)
        print('\nSe encontraron ' + str(result[0]) + ' avistamientos en ' + ciudad)
        print('\nPimeros 3 avistamientos:')
        controller.printFirst3(result[1])
        print('\nUltimos 3 avistamientos:')
        controller.printLast3(result[1])

    elif int(inputs[0]) == 4:
        duracion1 = input('Duracion minima (segundos) : ')
        duracion2 = input('Duracion maxima (segundos) : ')
        print('\nSe encontraron ' + str(controller.indexSize(cont['durationIndex'])) + ' avistamientos con distintas duraciones')
        min = controller.findMax(cont['durationIndex'])
        print('El avisamiento de mayor duracion duro: ' + str(min[0]))
        print('Numero de avistamientos con esta duracion : ' + str(min[1]))
        result = controller.searchByDurationRange(cont['durationIndex'], duracion1, duracion2)

        print('\nSe encontraron ' + str(result[0]) + ' avistamientos en el rango de duraciones')
        print('\n3 avistamientos mas largos:')
        controller.printFirst3(result[1])
        print('\n3 avistamientos mas cortos:')
        controller.printLast3(result[1])

    elif int(inputs[0]) == 5:
        print('Elementos en el arbol: ' + str(controller.indexSize(cont['durationIndex'])))
        print('Menor Llave: ' + str(controller.minKey(cont['durationIndex'])))
        print('Mayor Llave: ' + str(controller.maxKey(cont['durationIndex'])))

    elif int(inputs[0]) == 6:
        fecha1 = input('Fecha minima de busqueda (AAAA-MM-DD) : ')
        fecha2 = input('Fecha maxima de busqueda (AAAA-MM-DD) : ')
        print('\nSe encontraron ' + str(controller.indexSize(cont['dateIndex'])) + ' avistamientos con distintas fechas')
        min = controller.findMin(cont['dateIndex'])
        print('La fecha de avistamiento mas antiguo fue en: ' + str(min[0]))
        print('Numero de avistamientos en esa fecha : ' + str(min[1]))
        result = controller.searchByDateRange(cont['dateIndex'], fecha1, fecha2)

        print('\nSe encontraron ' + str(result[0]) + ' avistamientos en el rango')
        print('\nPimeros 3 avistamientos:')
        controller.printFirst3(result[1])
        print('\nUltimos 3 avistamientos:')
        controller.printLast3(result[1])

    else:
        sys.exit(0)
sys.exit(0)
