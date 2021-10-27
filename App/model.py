﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'avistamientos': None,
                'cityIndex': None
                }

    analyzer['avistamientos'] = lt.newList('ARRAY_LIST', compareDates)
    analyzer['cityIndex'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareCities)
    return analyzer

# Funciones para agregar informacion al catalogo

def addUFO(analyzer, UFO):
    """
    """
    lt.addLast(analyzer['avistamientos'], UFO)
    updateCityIndex(analyzer['cityIndex'], UFO)
    return analyzer


def updateCityIndex(map, UFO):
    """
    Se toma la ciudad del avistamiento y se busca si ya existe en el arbol
    dicha ciudad.  Si es asi, se adiciona a su lista de avistamientos
    y se actualiza ...

    Si no se encuentra creado un nodo para esa ciudad en el arbol
    se crea y se actualiza ...
    """
    city = UFO['city']
    entry = om.get(map, city)
    if entry is None:
        cityentry = newDataEntry(UFO)
        om.put(map, city, cityentry)
    else:
        cityentry = me.getValue(entry)
        addCityIndex(cityentry, UFO)
    return map

def newDataEntry(UFO):
    """
    Crea una entrada en el indice por ciudades, es decir en el arbol
    binario.
    """
    entry = {'lstUFOs': None}
    entry['lstUFOs'] = lt.newList('ARRAY_LIST', compareDates)
    lst = entry['lstUFOs']
    lt.addLast(lst, UFO)
    return entry

def addCityIndex(cityentry, UFO):
    
    lst = cityentry['lstUFOs']
    lt.addLast(lst, UFO)
    return cityentry


# Funciones para creacion de datos

# Funciones de consulta

def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['cityIndex'])


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['cityIndex'])


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer['cityIndex'])


def maxKey(analyzer):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer['cityIndex'])

# Funciones utilizadas para comparar elementos dentro de una lista

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareCities(city1, city2):
    """
    Compara dos ciudades
    """
    if (city1 == city2):
        return 0
    elif city1 > city2:
        return 1
    else:
        return -1

# Funciones de ordenamiento
