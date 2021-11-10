"""
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
 """

from DISClib.ADT import list as lt
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer, UFOfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    UFOfile = cf.data_dir + UFOfile
    input_file = csv.DictReader(open(UFOfile, encoding="utf-8"),
                                delimiter=",")
    for ufo in input_file:
        model.addUFO(analyzer, ufo)
    return analyzer

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def UFOsSize(analyzer):
    """
    Número de UFOs
    """
    return lt.size(analyzer['avistamientos'])

def printFirstTotals(analyzer):
    avistamientos = analyzer['avistamientos']
    i=1
    while i in range (1,6):
        avistamiento = lt.getElement(avistamientos,i)
        print('\n###########\nFecha: ' + avistamiento['datetime'] +
            ", Ciudad: " + avistamiento['city'] +
            ', Pais: ' + avistamiento['country']+
            ', Forma: '+ avistamiento['shape']+
            ', Duracion(segundos): '+avistamiento['duration (seconds)'])
        i+=1
    pass


def printLastTotals(analyzer):
    avistamientos = analyzer['avistamientos']
    totals = int(lt.size(analyzer['avistamientos']))
    k = totals
    while k in range (totals-4, totals+1):
        avistamiento = lt.getElement(avistamientos,k)
        print('\n###########\nFecha: ' + avistamiento['datetime'] +
            ", Ciudad: " + avistamiento['city'] +
            ', Pais: ' + avistamiento['country']+
            ', Forma: '+ avistamiento['shape']+
            ', Duracion(segundos): '+avistamiento['duration (seconds)'])
        k-=1
    pass

def printFirst3(list):
    i=1
    while i in range (1,4):
        try:
            avistamiento = lt.getElement(list,i)
            print('\n###########\nFecha: ' + avistamiento['datetime'] +
                ", Ciudad: " + avistamiento['city'] +
                ', Pais: ' + avistamiento['country']+
                ', Forma: '+ avistamiento['shape']+
                ', Duracion(segundos): '+avistamiento['duration (seconds)'])
            i+=1
        except: 
            i+=1

def printLast3(list):
    totals = int(lt.size(list))
    k = totals-2
    while k in range (totals-2, totals+1):
        try:
            avistamiento = lt.getElement(list,k)
            print('\n###########\nFecha: ' + avistamiento['datetime'] +
                ", Ciudad: " + avistamiento['city'] +
                ', Pais: ' + avistamiento['country']+
                ', Forma: '+ avistamiento['shape']+
                ', Duracion(segundos): '+avistamiento['duration (seconds)'])
            k+=1
        except:
            break

def printFirst5(list):
    i=1
    while i in range (1,6):
        try:
            avistamiento = lt.getElement(list,i)
            print('\n###########\nFecha: ' + avistamiento['datetime'] +
                ", Ciudad: " + avistamiento['city'] +
                ', Pais: ' + avistamiento['country']+
                ', Forma: '+ avistamiento['shape']+
                ', Duracion(segundos): '+avistamiento['duration (seconds)']+
                ', longitud: '+ avistamiento['longitude']+
                ', latitud: '+ avistamiento['latitude'])
            i+=1
        except: 
            i+=1

def printLast5(list):
    totals = int(lt.size(list))
    k = totals-4
    while k in range (totals-4, totals+1):
        try:
            avistamiento = lt.getElement(list,k)
            print('\n###########\nFecha: ' + avistamiento['datetime'] +
                ", Ciudad: " + avistamiento['city'] +
                ', Pais: ' + avistamiento['country']+
                ', Forma: '+ avistamiento['shape']+
                ', Duracion(segundos): '+avistamiento['duration (seconds)']+
                ', longitud: '+ avistamiento['longitude']+
                ', latitud: '+ avistamiento['latitude'])
            k+=1
        except:
            break

def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)


def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def findMin(analyzer):

    return model.findMin(analyzer)

def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)

def findMax(analyzer):

    return model.findMax(analyzer)

def findMaxCity(analyzer):

    return model.findMaxCity(analyzer)

def searchByDateRange(cont, fecha1, fecha2):

    result = model.searchByDateRange(cont, fecha1, fecha2)

    return result

def searchByDurationRange(cont, duration1, duration2):

    result = model.searchByDurationRange(cont, duration1, duration2)

    return result

def searchByCity(cont, city):

    result = model.searchByCity(cont,city)

    return result

def searchByLocation(cont, longitud_min, longitud_max, latitud_min, latitud_max):

    result = model.searchByLocation(cont, longitud_min, longitud_max, latitud_min, latitud_max)

    return result