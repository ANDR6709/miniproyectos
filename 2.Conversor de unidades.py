# a. Crea un programa que convierte entre diferentes unidades de medida, como 
#  longitud, masa o temperatura.
# b. Los estudiantes pueden implementar funciones para convertir de una unidad 
#    a otra y luego crear una interfaz de usuario simple.


def celsius_a_fahrenheit(temperatura):
    return temperatura * 1.8 + 32


temperatura_f = celsius_a_fahrenheit(17)
print(f'La temperatura en ºF es: {temperatura_f}')

temperatura_f = celsius_a_fahrenheit(25)
print(f'La temperatura en ºF es: {temperatura_f}')



def fahrenheit_a_celsius(temperatura):
    return (temperatura - 32) / 1.8


temperatura_c = fahrenheit_a_celsius(17)
print(f'La temperatura en ºC es: {temperatura_c}')

temperatura_c = fahrenheit_a_celsius(41)
print(f'La temperatura en ºC es: {temperatura_c}')




def celsius_a_kelvin(temperatura):
    return temperatura + 273.15


temperatura_k = celsius_a_kelvin(30)
print(f'La temperatura en K es: {temperatura_k}')

temperatura_k = celsius_a_kelvin(55.3)
print(f'La temperatura en K es: {temperatura_k}')




def kelvin_a_celsius(temperatura):
    return temperatura - 273.15


temperatura_c = kelvin_a_celsius(265.9)
print(f'La temperatura en ºC es: {temperatura_c}')

temperatura_c = kelvin_a_celsius(297.15)
print(f'La temperatura en ºC es: {temperatura_c}')




def fahrenheit_a_kelvin(temperatura):
    return (temperatura + 459.67) / 1.8


temperatura_k = fahrenheit_a_kelvin(50)
print(f'La temperatura en K es: {temperatura_k}')

temperatura_k = fahrenheit_a_kelvin(75)
print(f'La temperatura en K es: {temperatura_k}')



