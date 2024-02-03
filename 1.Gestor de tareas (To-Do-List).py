# a.Crea un programa que permita a los usuarios agregar, editar y eliminar tareas 
# en una lista.

# b. Pueden expandir el proyecto agregando funciones como la fecha de 
# vencimiento y la prioridad de las tareas.



lista_de_tareas={}


def agregar_tarea():
    tarea=input("ingrese la nueva tarea")
    nuevo_id=len(lista_de_tareas)+1
    nueva_tarea={"tarea":tarea,"completada":False}
    lista_de_tareas[nuevo_id]=nueva_tarea
    print("tarea agregada a la lista")


def  marcar_completada():
    tarea_id=int(input("ingrese el numero de tarea que desea marcar como completada"))
    if tarea_id in lista_de_tareas:
        lista_de_tareas[tarea_id]["completada"]=True
        print("tarea marcada como completada.")
    else:
        print("tarea no encontrada.")





