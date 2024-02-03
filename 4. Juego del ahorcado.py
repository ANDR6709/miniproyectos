
# a . Implementa el clásico juego del ahorcado en el que los jugadores intentan 
#     adivinar una palabra oculta.
# b.  Incluye funciones para manejar la lógica del juego, como verificar letras 
#     correctas o incorrectas.



import random




palabras=["mesa","tomate","pajaro","quebrada","sol","montaña","esperanza"]
secreta=random.choice(palabras)
cadena="-" *len(secreta)
print("Bienvenidos al juego del ahorcado")
intentos=0



while True:
    print(cadena)
    letra=input("ingresa una letra:")
    if letra in secreta:
        for i in range(len(secreta)):
            if secreta[i]==letra:
                cadena=cadena[:i]+letra+cadena[i+1:]
            else:
                intentos +=1
                if intentos==1:
                    print("O")
                elif intentos==2:
                    print(" O")
                    print("/")
                elif intentos==3:
                    print("/|")
                elif intentos==4:
                    print("/|\\")
                elif intentos==5:
                    print(" O")
                    print("/|\\")
                    print("/")
                elif intentos==6:
                    print(" O")
                    print("/|\\") 
                    print("/\\")
                    print(f"has perdido el juego.la palabra secreta era{secreta}")
                    break

            if cadena==secreta:
                print("Felicidades has ganado el juego.la palabra secreta era{secreta}")
                break



                    

                
                    


    