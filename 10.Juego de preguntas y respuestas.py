# a.Diseña un juego de preguntas y respuestas con diferentes categorías.
# b.Pueden almacenar preguntas en una estructura de datos y permitir que los 
#  jugadores seleccionen categorías y respondan preguntas.


from io import open
import random
def aleatorio():
    num=random.randint(0,22)
    return num


def preg():
    archivo=open('preguntas.txt','r')
    preg=archivo.readlines()
    archivo.close
    return preg


def pcorrecta(preg1):
    resp={0:"a",1:"a",2:"c",3:"d",4:"d",5:"b",6:
          "d",12:"b",13:"c",14:"a",15:"b",16:"c"}
    afir=resp[preg1]
    return afir
preg=preg()
num=aleatorio()
acierto=0
cantidad=0
for i in range(5):
    num=aleatorio()
    print("conteste correctamente")
    print(preg[num])
    op=input()
    acierto=acierto+1
    cantidad=cantidad+25
    if op==pcorrecta(num):
        print("pregunta correcta,ha ganado $",cantidad)
        print("el numero de aciertos es",acierto)
        if acierto==5:
            print("felicidades gano el juego")
            print("su premio total es $",cantidad)
        else:
            print("respuesta incorrecta,fin del juego")
            print("su numero de acierto es:",acierto-1)
            print("ha ganado $",cantidad-25)
            break


