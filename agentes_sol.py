import numpy as np
import random

# pasos/movimientos de aspiradoras
steps = 0

# costo por limpieza
costo = 0

print("Ingresa el tamaño de la habitación a limpiar: ")
filas = input("Filas: ")
columnas = input("Columnas: ")

aspiradoras = input("Ingresa el numero de aspiradoras: ")
porcentaje = input("Ingresa el porcentaje de suciedad: ")

tam = int(filas) * int(columnas)

area = np.zeros((int(filas), int(columnas)))
visitada = np.zeros((int(filas), int(columnas)))

np.random.seed(42)
operacion = int(filas) * int(columnas)
cant = round((int(porcentaje) * int(operacion)) / 100)
contador = 0
for m in range(int(filas)):
    for n in range(int(columnas)):
        random_numbers = random.randint(0, 1)
        if(random_numbers == 1):
            area[m, n] = 1
            contador += 1
        else:
            area[m, n] = 0
        if(contador == cant+1):
            area[m, n] = 0
            continue
print("area sucia")
print(area)

# 0 = limpio
# 1 = sucio

aspiradora = np.zeros((int(filas), int(columnas)))
aspiradora[1, 1] = int(aspiradoras) #numero de agentes

print("aspiradora")
print(aspiradora)

costo = 0
steps = 0
#i = 0
#j = 0

def moverextraordinario(i, j, n):
    global steps
    while True:
        try:
            ubicacion = [random.randrange(0, 3), random.randrange(0, 3)] # [n, n] # todas las posiciones alrededor -> 8
            
            if(ubicacion[0] == 0 and ubicacion[1] == 0): # ARRIBA IZQUIERDA [0, 0]
                # esta dentro del área y no hay agente
                if(i-1 > 0 and i-1 < int(filas) and j-1 > 0 and j-1 < int(columnas) and int(aspiradora[i-1, j-1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i -= 1
                    j -= 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    continue

            elif(ubicacion[0] == 1 and ubicacion[1] == 0): # ARRIBA [1, 0]
                # esta dentro del área y no hay agente
                if(i-1 > 0 and i-1 < int(filas) and int(aspiradora[i-1, j]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i -= 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    continue
        
            elif(ubicacion[0] == 2 and ubicacion[1] == 0): # ARRIBA DERECHA [2, 0]
                # esta dentro del área y no hay agente
                if(i-1 > 0 and i-1 < int(filas) and j+1 > 0 and j+1 < int(columnas) and int(aspiradora[i-1, j+1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i -= 1
                    j += 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    continue
        
            elif(ubicacion[0] == 0 and ubicacion[1] == 1): # IZQUIERDA [0, 1]
                # esta dentro del área y no hay agente
                if(j-1 >= 0 and j-1 < int(columnas) and int(aspiradora[i, j-1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    j -= 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    continue
            elif(ubicacion[0] == 0 and ubicacion[1] == 2): # ABAJO IZQUIERDA [0, 2]
                # esta dentro del área, la posicion está sucia, no ha sido visitada, no hay agente
                if(i+1 > 0 and i+1 < int(filas) and j-1 >= 0 and j-1 < int(columnas) and int(aspiradora[i+1, j-1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i += 1
                    j -= 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    continue
        
            elif(ubicacion[0] == 1 and ubicacion[1] == 2): # ABAJO [1, 2]
                # esta dentro del área y no hay agente
                if(i+1 > 0 and i+1 < int(filas) and int(aspiradora[i+1, j]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i += 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    continue
        
            elif(ubicacion[0] == 2 and ubicacion[1] == 2): # ABAJO DERECHA [2, 2]
                # esta dentro del área y no hay agente
                if(i+1 > 0 and i+1 < int(filas) and j+1 > 0 and j+1 < int(columnas) and int(aspiradora[i+1, j+1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i += 1
                    j += 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    continue
                
            elif(ubicacion[0] == 2 and ubicacion[1] == 1): # DERECHA [2, 1]
                # esta dentro del área, la posicion está sucia, no ha sido visitada, no hay agente
                if(j+1 > 0 and j+1 < int(columnas) and int(aspiradora[i, j+1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    j += 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    continue

            elif(ubicacion[0] == 1 and ubicacion[1] == 1): # misma posición actual [1, 1]
                if(n == 0): # numero de agentes en la posición
                    continue
                else:
                    return
            
        except KeyboardInterrupt:
            print("press control-c again to quit")
        #return i, j #input(prompt) #let it raise if it happens again
        return
    
    
def mover(i, j, n):
    global steps
    cont = 1
    while True:
        try:
            ubicacion = [random.randrange(0, 3), random.randrange(0, 3)] # [n, n] # todas las posiciones alrededor -> 8
            #print("ubicacion", ubicacion)

            if(ubicacion[0] == 0 and ubicacion[1] == 0): # ARRIBA IZQUIERDA [0, 0]
                cont += 1
                # esta dentro del área, la posicion está sucia, no ha sido visitada, no hay agente
                if(i-1 > 0 and i-1 < int(filas) and j-1 > 0 and j-1 < int(columnas) and int(area[i-1, j-1]) == 1 and int(visitada[i-1, j-1]) == 0 and int(aspiradora[i-1, j-1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i -= 1
                    j -= 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    if(cont == 10): # ya checo todas las casillas posibles
                        moverextraordinario(i, j, n)
                    else:
                        continue

            elif(ubicacion[0] == 1 and ubicacion[1] == 0): # ARRIBA [1, 0]
                cont += 1
                # esta dentro del área, la posicion está sucia, no ha sido visitada, no hay agente
                if(i-1 > 0 and i-1 < int(filas) and int(area[i-1, j]) == 1 and int(visitada[i-1, j]) and int(aspiradora[i-1, j]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i -= 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    if(cont == 10): # ya checo todas las casillas posibles
                        moverextraordinario(i, j, n)
                    else:
                        continue
        
            elif(ubicacion[0] == 2 and ubicacion[1] == 0): # ARRIBA DERECHA [2, 0]
                cont += 1
                # esta dentro del área, la posicion está sucia, no ha sido visitada, no hay agente
                if(i-1 > 0 and i-1 < int(filas) and j+1 > 0 and j+1 < int(columnas) and int(area[i-1, j+1]) == 1 and int(visitada[i-1, j+1]) == 0 and int(aspiradora[i-1, j+1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i -= 1
                    j += 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    if(cont == 10): # ya checo todas las casillas posibles
                        moverextraordinario(i, j, n)
                    else:
                        continue
        
            elif(ubicacion[0] == 0 and ubicacion[1] == 1): # IZQUIERDA [0, 1]
                cont += 1
                # esta dentro del área, la posicion está sucia, no ha sido visitada, no hay agente
                if(j-1 >= 0 and j-1 < int(columnas) and int(area[i, j-1]) == 1 and int(visitada[i, j-1]) == 0 and int(aspiradora[i, j-1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    j -= 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    if(cont == 10): # ya checo todas las casillas posibles
                        moverextraordinario(i, j, n)
                    else:
                        continue
                    
            elif(ubicacion[0] == 0 and ubicacion[1] == 2): # ABAJO IZQUIERDA [0, 2]
                cont += 1
                # esta dentro del área, la posicion está sucia, no ha sido visitada, no hay agente
                if(i+1 > 0 and i+1 < int(filas) and j-1 >= 0 and j-1 < int(columnas) and int(area[i+1, j-1]) == 1 and int(visitada[i+1, j-1]) == 0 and int(aspiradora[i+1, j-1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i += 1
                    j -= 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    if(cont == 10): # ya checo todas las casillas posibles
                        moverextraordinario(i, j, n)
                    else:
                        continue
        
            elif(ubicacion[0] == 1 and ubicacion[1] == 2): # ABAJO [1, 2]
                cont += 1
                # esta dentro del área, la posicion está sucia, no ha sido visitada, no hay agente
                if(i+1 > 0 and i+1 < int(filas) and int(area[i+1, j]) == 1 and int(visitada[i+1, j]) == 0 and int(aspiradora[i+1, j]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i += 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    if(cont == 10): # ya checo todas las casillas posibles
                        moverextraordinario(i, j, n)
                    else:
                        continue
        
            elif(ubicacion[0] == 2 and ubicacion[1] == 2): # ABAJO DERECHA [2, 2]
                cont += 1
                # esta dentro del área, la posicion está sucia, no ha sido visitada, no hay agente
                if(i+1 > 0 and i+1 < int(filas) and j+1 > 0 and j+1 < int(columnas) and int(area[i+1, j+1]) == 1 and int(visitada[i+1, j+1]) == 0 and int(aspiradora[i+1, j+1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    i += 1
                    j += 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    if(cont == 10): # ya checo todas las casillas posibles
                        moverextraordinario(i, j, n)
                    else:
                        continue
                
            elif(ubicacion[0] == 2 and ubicacion[1] == 1): # DERECHA [2, 1]
                cont += 1
                # esta dentro del área, la posicion está sucia, no ha sido visitada, no hay agente
                if(j+1 > 0 and j+1 < int(columnas) and int(area[i, j+1]) == 1 and int(visitada[i, j+1]) == 0 and int(aspiradora[i, j+1]) == 0):
                    if(n-1 < 0):
                        aspiradora[i, j] = 0
                    else:
                        aspiradora[i, j] = n-1
                    j += 1
                    aspiradora[i, j] = 1
                    #print("Aspiradora se movió a: cuadro [",i,",",j,"]")
                    steps += 1
                    return # tengo una posicion
                else:
                    if(cont == 10): # ya checo todas las casillas posibles
                        moverextraordinario(i, j, n)
                    else:
                        if(cont == 10): # ya checo todas las casillas posibles
                            moverextraordinario(i, j, n)
                        else:
                            continue

            elif(ubicacion[0] == 1 and ubicacion[1] == 1): # misma posición actual [1, 1]
                cont += 1
                if(n == 0):
                    continue
                else:
                    return
            else:
                moverextraordinario(i, j, n)
                
        except KeyboardInterrupt:
            print("press control-c again to quit")
        #return i, j #input(prompt) #let it raise if it happens again
        return

            
def limpiar():
    
    global sucio
    global steps
    global costo
    n = 0
    for i in range(int(filas)):
        for j in range(int(columnas)):
            #print("aspiradora[i, j]", int(aspiradora[i, j]))
            #print("i", i)
            #print("j", j)
            
            if(int(aspiradora[i, j]) > 1): # Hay más de 1 en el mismo lugar
                n = int(aspiradora[i, j]) # numero de aspiradoras en una misma posición
                mover(i, j, n)
                print("aspiradora")
                print(aspiradora)
                print("area")
                print(area)
                continue
                
            if(int(aspiradora[i, j]) == 1): # hay 1 aspiradora en la posición
                if(int(area[i, j]) == 1): # esta sucio
                    #print("Hay que limpiar cuadro [",i,",",j,"]")
                    #print("Limpiando cuadro [",i,",",j,"]")
                    sucio -= 1
                    area[i, j] = 0
                    visitada[i, j] = 1
                    costo += 1
                    mover(i, j, n)
                    print("aspiradora")
                    print(aspiradora)
                    print("area")
                    print(area)
                    
                    continue
                else: # esta limpio
                    #print("Está limpio cuadro [",i,",",j,"]")
                    mover(i, j, n)
                    continue
            else: # no hay 1 aspiradora en la posición
                continue
                    
                
sucio = 0

for a in range(int(filas)): # recorre toda la habitación
    for b in range(int(columnas)):
        if(area[a, b] == 1): #esta sucia
            sucio += 1
#print(sucio)

while sucio > 0 and int(aspiradoras) >= 1: # mientras haya algo que limpiar y haya una aspiradora
    #print("sucio while", sucio)
    limpiar()
    
print("El costo de la limpieza fue de: ",costo)
print("Los movimientos de las aspiradoras fueron de: ",steps)