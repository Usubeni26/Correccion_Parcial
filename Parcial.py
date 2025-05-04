import array
import machine
from uctypes import addressof

def bezier(P0, P1, P2, P3, n):
    mem32 = machine.mem32
    LR = []
    
    # direcciones de memoria
    dir_P0 = addressof(memoryview(P0))
    dir_P1 = addressof(memoryview(P1))
    dir_P2 = addressof(memoryview(P2))
    dir_P3 = addressof(memoryview(P3))
    
    # Leer coordenadas (x, y) de cada punto
    p0_x = mem32[dir_P0]        # x de P0
    p0_y = mem32[dir_P0 + 4]    # y de P0
    p1_x = mem32[dir_P1]        # x de P1
    p1_y = mem32[dir_P1 + 4]    # y de P1
    p2_x = mem32[dir_P2]        # x de P2
    p2_y = mem32[dir_P2 + 4]    # y de P2
    p3_x = mem32[dir_P3]        # x de P3
    p3_y = mem32[dir_P3 + 4]    # y de P3

    for i in range(n + 1):
        t = i / n
        # Coeficientes de Bézier n=4
        c0 = (1.0 - t)**3
        c1 = 3.0 * (1.0 - t)**2 * t
        c2 = 3.0 * (1.0 - t) * t**2
        c3 = t**3
        
        # Calcular coordenadas interpoladas
        x = int(c0 * p0_x + c1 * p1_x + c2 * p2_x + c3 * p3_x)
        y = int(c0 * p0_y + c1 * p1_y + c2 * p2_y + c3 * p3_y)
        
        LR.append(array.array('l', [x, y]))
    
    return LR
#Puesta a prueba del algoritmo
P0 = array.array('l', [0, 0])    
P1 = array.array('l', [50, 100])  
P2 = array.array('l', [100, 50])  
P3 = array.array('l', [150, 0])   

# Generar la curva con n=4 
LR = bezier(P0, P1, P2, P3, 4)

# Mostrar resultados
for i in LR:
    print(f"({i[0]}, {i[1]})")