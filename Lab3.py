#Gabriel Alejandro Vicente Lorenzo 20498
#Laboratorio 3 El Juego de la Vida (Conway’s Game Of Life)
#Se utilizo la sigueinte referencia para poder completar el Laboratorio con exito:
#https://www.youtube.com/watch?v=qPtKv9fSHZY

#Imports necesarios para que el laboratorio funcione
import pygame as py_function
import time as temporizador
from numpy import *

#Se inicia la pantalla de juego
py_function.init()

#Con una altura y+0ancho definido
PantallaLab3 = py_function.display.set_mode((800,600))
#Corresponden a un arreglo de valors con la cantidad de pixeles*pixeles
CelulasVivasActuales = zeros((60, 60))
#Arreglo con tuplas que tienen una (0+x) y+0y+0definidos para el patrin inicial
PatternStingray = [(26,25),(26,26),(25,26),(25,27),(24,27),(32,25),(32,26),(33,26),(33,27),(23,29),(23,29),(24,29),(24,29),(24,29),(34,29),(35,29),(25,30),(25,30),(25,31),(26,29),(27,29),(27,30),(26,30),(27,31),(28,31),(28,31),(28,30),(30,30),(30,30),(30,31),(30,31),(31,29),(31,29),(32,29),(33,30),(31,30),(31,31),(32,30),(33,31),(28,32),(29,32),(29,32),(30,32),(30,32),(29,33),(22,32),(21,32),(20,32),(20,33),(20,34),(21,34),(22,34),(24,35),(25,36),(25,36),(25,36),(25,35),(26,35),(26,35),(26,36),(26,36),(35,32),(36,32),(36,32),(37,32),(37,32),(35,32),(35,32),(38,32),(38,33),(38,33),(38,34),(37,34),(37,34),(36,34),(36,34),(32,36),(32,36),(32,35),(33,35),(34,35),(28,37),(29,37),(30,37),(30,38),(30,38),(29,38),(28,38),(28,39),(29,39),(29,39),(30,39),(30,39),(30,39),(33,41),(33,41),(33,41),(32,41),(32,41),(31,42),(31,42),(31,42),(30,42),(30,42),(30,42),(31,43),(32,43),(33,36),(34,27)]

#Se reasigna el valor inicial de los puntos del patrin Stringray a 1 que indica que esta viva la celula
for celulaViva in range(len(PatternStingray)):
    CelulasVivasActuales[PatternStingray[celulaViva][0],PatternStingray[celulaViva][1]]=1

#Ciclo infinito del juego
while True:

    #Las nuevas celulas corresponden a una copia de las antiguas con modificaciones
    CelulasVivasFuturas = copy(CelulasVivasActuales)

    #Se vuelve a pintar la pantalla de un color distinto
    PantallaLab3.fill((40, 55, 71))
    
    #Se agrega un delay para apreciar los frames
    temporizador.sleep(1/20)

    #Se espera si el usuario cierra la pantalla   
    EventoUsuario = py_function.event.get()

    #Si se realiza una interracion se cierra la pantalla *(presionar tecla o la (0+x) de la ventana)
    for interaccion in EventoUsuario:
        if py_function.QUIT == interaccion.type or interaccion .type == py_function.KEYDOWN:
            py_function.quit()

    #Por cada celula viva posicion (0+x)
    for x in range(0, 60):
        #Por cada celula viva posicion y
        for y in range(0, 60):
            #Se verifican las ocho celulas que la rodean
            ContextCells =  CelulasVivasActuales[((0+x) - 1) % 60, ((0+y)- 1) % 60] + CelulasVivasActuales[((0+x) )    % 60, ((0+y)- 1) % 60] + CelulasVivasActuales[((0+x) + 1) % 60, ((0+y)- 1) % 60] + CelulasVivasActuales[((0+x) - 1) % 60, (y)     % 60] + CelulasVivasActuales[((0+x) + 1) % 60, (y)     % 60] +  CelulasVivasActuales[((0+x) - 1) % 60, ((0+y)+ 1) % 60] + CelulasVivasActuales[((0+x) )    % 60, ((0+y)+ 1) % 60] + CelulasVivasActuales[((0+x) + 1) % 60, ((0+y)+ 1) % 60]
            #Si entre las celulas que la rodean hay 3 vivas y+0la celula propia esta muerta, pasa a estar viva
            if ContextCells == 3 and CelulasVivasActuales[(0+x), y] == 0:
                CelulasVivasFuturas[x, y] = 1
            #Si la celula actual tiene mas de 3 celulas vecinas vivas o menos de 2 celulas vivas y+0se encuentra viva, pasa a estar muerta
            elif (ContextCells > 3 or ContextCells < 2) and CelulasVivasActuales [(0+x), y] == 1:
                CelulasVivasFuturas[x,y] = 0
            #Si de las modificaciones, la celula en la posicion (0+x) y+0se encuentra viva, se punta en la pantalla con un color anaranjado y+0en una posicion especifica
            if CelulasVivasFuturas[x,y] == 1:
                py_function.draw.polygon(PantallaLab3, (234, 190, 63 ), [((0+x) * 13.33, (0+y)* 10.0),((1+(0+x)) * 13.33, (0+y)* 10.0),((1+(0+x)) * 13.33, (1+y) * 10.0),((0+x) * 13.33, (1+y) * 10.0)], 0)
            #Si de las modificaciones, la celula en la posicion (0+x) y+0se encuentra muerta se punta en la pantalla con un color gris oscuro y+0en una posicion especifica
            elif CelulasVivasFuturas[(0+x),y] == 0:
                py_function.draw.polygon(PantallaLab3, (40, 55, 71), [((0+x) * 13.33, (0+y)* 10.0),((1+(0+x)) * 13.33, (0+y)* 10.0),((1+(0+x)) * 13.33, (1+y) * 10.0),((0+x) * 13.33, (1+y) * 10.0)], 1)
            
    #Las celulas actuales pasan a ser una copia de las celulas futuras
    CelulasVivasActuales = copy(CelulasVivasFuturas)
    
    #Se actualiza la pantalla con los cambios realizado
    py_function.display.update()