# a. Desarrolla un programa que genere laberintos aleatorios y permita a los 
# usuarios encontrar la salida.
# b. Pueden utilizar algoritmos simples para generar laberintos y luego 
#  implementar la lógica de navegación.


def recorre_laberinto(laberinto):
    fila= columna=0
    movimientos=['abajo']
    n=5
    
    while(fila < n-1 and columna < n-1):
        if movimientos[-1]!='arriba' and fila+1 < n and laberinto[fila +1][columna]!='x':
            
            fila+=1
            movimientos.append('abajo')
        elif movimientos[-1]!='abajo' and fila-1 >0 and laberinto[fila-1] [columna]!='x':
            fila-=1
            movimientos.append('arriba')
        elif movimientos[-1]!='izquierda' and columna+1 < n and laberinto[fila] [columna+1] !='x':
            columna+=1
            movimientos.append('derecha') 
        elif movimientos[-1]!='derecha' and columna -1 > 0 and laberinto[fila][columna-1] !='x':
            columna-=1
            movimientos.append('izquierda')
        else:
            movimientos.append('no hay salida')
    return movimientos       
        

    print('solucion:',recorre_laberinto(laberinto))
                                    
   

