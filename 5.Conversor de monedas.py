# a. Crea un programa que realice conversiones entre diferentes monedas.
# b. Pueden utilizar tasas de cambio actuales o permitir que los usuarios ingresen tazas personalizadas.

print("1 de dolares a pesos chilenos")
print("2 de pesos chilenos a dolares")
print("3 de dolares a euros")
print("4 de euros a dolares")
print("5 de pesos mexicanos a dolares")
print ("")
hl=int(input("coloque aqui opcion"))
print ("")
if hl==1:
    dol1=int(input("introdusca cantidad de dolares"))
    pesc=dol1*756.70
    print ("")
    print ("pesos chilenos=", pesc)
if hl==2:
    pesc1=float(input("introdusca pesos chilenos"))
    dol2=pesc1/756.70
    print("")
    print("dolares=", dol2)
if hl==3:
    dol3=int(input("introdusca cantidad de dolares"))
    euros=dol3*1.18
    print("")
    print("dolares=", euros)
if hl==4:
    euros1=int(input("introduzca dolares"))
    dol4=euros1/1.18
    print("")
    print("euros=", dol4)
if hl==5:
    pesm=int(input("coloque pesos mexicanos"))
    dol5=pesm/22.27
    print("")
    print("dolares=", dol5)
    
 