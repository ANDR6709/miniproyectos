# a.Crea un programa que permita a los usuarios agregar, editar y eliminar tareas 
# en una lista.

# b. Pueden expandir el proyecto agregando funciones como la fecha de 
# vencimiento y la prioridad de las tareas.


# definir una lista vacía  

tareas = []  

# definir la función para agregar tareas a la lista  


def  agregar_tarea():  
    # obteniendo la cadena del campo de entrada  
    cadena_tarea = campo_tarea.get()  
    # comprobando si la cadena está vacía o no  
    si  len(cadena_tarea) ==  0 :  
        # mostrando un cuadro de mensaje con el mensaje 'Campo vacío'  
        messagebox.showinfo( 'Error' ,  'El campo está vacío' ).


      # agregando la cadena a la lista de tareas  
        tareas.append(cadena_tarea)  
         
        the_cursor.execute ( 'insertar valores en tareas (?)' , (cadena_tarea,))  
        # llamando a la función para actualizar la lista  
        lista_actualización()  
        # eliminar la entrada en el campo de entrada  
        task_field.delete ( 0 ,  'fin' )



    # definiendo la función para actualizar la lista  
def  lista_actualización():  
    # llamando a la función para borrar la lista  
    limpiar lista()  
    # iterando a través de las cadenas en la lista  
    para  tarea  en  tareas:  
        # usando el método insert() para insertar las tareas en el cuadro de lista  
        task_listbox.insert( 'fin' , tarea)



  # definir la función para eliminar una tarea de la lista  
def  eliminar_tarea():  
    # usando el método try-except  
    intentar :  
        # obtener la entrada seleccionada del cuadro de lista  
        el_valor = task_listbox.get(task_listbox.curselection())  
        # comprobando si el valor almacenado está presente en la lista de tareas  
        si  el_valor  en  tareas:  
            # eliminar la tarea de la lista  
            tareas.remove(el_valor)  
            # llamando a la función para actualizar la lista  
            lista_actualización()  
            # usando el método ejecutar() para ejecutar una declaración SQL  
            the_cursor.execute( 'eliminar de tareas donde título =?' , (the_value,))
    

 # función para eliminar todas las tareas de la lista  
def  eliminar_todas_tareas():  
    # mostrar un cuadro de mensaje para pedir confirmación al usuario  
   message_box   = messagebox.askyesno( 'Eliminar todo' ,  '¿Estás seguro?' )  
    # si el valor resulta ser Verdadero  
     si  cuadro_mensaje ==  Verdadero :  
        # usando el bucle while para recorrer la lista de tareas hasta que esté vacía   
        mientras (len (tareas)! =  0 ):  
            # usando el método pop() para sacar los elementos de la lista  
            tareas.pop()  
        # usando el método ejecutar() para ejecutar una declaración SQL  
        the_cursor.execute( 'eliminar de tareas' )  
        # llamando a la función para actualizar la lista  
        lista_actualización()


   # función para borrar la lista  
def  lista_clara():  
    # usando el método de eliminación para eliminar todas las entradas del cuadro de lista  
    task_listbox.delete ( 0 ,  'fin' )



 # función para cerrar la aplicación  
definición  cerrar():  
    # imprimir los elementos de la lista de tareas  
    imprimir (tareas)  
    # usando el método destroy() para cerrar la aplicación  
    guiWindow.destroy()  


# función para recuperar datos de la base de datos  
def  recuperar_base de datos():  
    # usando el bucle while para recorrer los elementos en la lista de tareas  
    mientras (len (tareas)! =  0 ):  
        # usando el método pop() para sacar los elementos de la lista  
        tareas.pop()  
    # iterando a través de las filas en la tabla de la base de datos  
    para  la fila  en  the_cursor.execute ( 'seleccionar título de las tareas' ):  
        # usando el método append() para insertar los títulos de la tabla en la lista  
        tareas.append(fila[ 0 ])  
               