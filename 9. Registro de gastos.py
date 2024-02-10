# a.Crear un sistema de registro de gastos que permita a los usuarios ingresar y 
#  categorizar sus gastos diarios.
#  b. Implementa funciones para calcular totales, generar informes y establecer 
#  presupuestos.


import os



def registrar_gasto(gastos,fecha,descripcion, cantidad):
     gastos.append({
         'fecha':fecha,
         'descripcion':descripcion,
         'cantidad':   cantidad

     })
         
     
        
        



def calcular_gasto_total(gastos):
    total=sum(gasto['cantidad']for gasto in gastos)
    return total



def mostrar_gastos(gastos):
    print('\nlista de gastos:')
    for gasto in gastos:
        print (f"fecha:{gasto['fecha']},descripcion:{gasto['descripcion']}, cantidad:${gasto['cantidad']:.2f}")
              
              

def guardar_gastos(gastos,archivo):
    with open(archivo,"w") as file:
        for gasto in gastos:
            file.write(f"{gasto['fecha']},{gasto['descripcion']},{gasto['cantidad'] }\n")

           

def cargar_gastos(archivo):
    gastos=[]
    if os. path.exists(archivo):
        with open(archivo,'r')as file:
            for line in file:
                fecha,descripcion,cantidad,=line.strip().slit(',')
                gastos.append({
                    'fecha':fecha,
                    'descripcion':descripcion,
                    'cantidad': float (cantidad)
                })
                return gastos


def main():
    archivo_gastos='gastos txt'
    gastos=cargar_gastos(archivo_gastos)  


    while True:
        print("\ncalculadora de gastos") 
        print("1.registrar gasto")
        print("2.mostrar gastos")  
        print("3.calcular gasto total")  
        print("4.salir")


        opcion=input("seleccione una opcion")

        if opcion=="1":
           fecha=input("ingrese la fecha(DD-MM-YYYY)") 
           descripcion=input("ingrese la descripccion del gasto:")
           cantidad=float(input("ingrese la cantidad gastada"))
           registrar_gasto(gastos,fecha,descripcion , cantidad)
           guardar_gastos(gastos,archivo_gastos)
           print("gasto registrado con exito")


        elif opcion=="2":
            mostrar_gastos(gastos)   


        elif opcion=="3":
            total=calcular_gasto_total(gastos) 
            print(f"gasto total:${total:.2f}")   


        elif opcion=="4":
            break


        else:
            print("opcion no valida.intente de nuevo.")


if __name__=="__main__":
    main()           


           

                    

              
            
              
              
              

              


