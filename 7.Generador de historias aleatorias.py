# a.Crea un programa que combine elementos aleatorios, como personajes
# lugares y eventos, para generar historias únicas.
# b. Pueden incluir opciones para que los usuarios personalicen el tipo de historia que desean crear.

import random


sentence_starter=['Hace unos 100 años','En el 20 a.c','Erase una vez',]
character=['vivia un rey en españa','habia un hombre llamado jack','vivia un granjero en Francia']
time=['un dia','una noche de luna llena']
story_pilot=['el estaba pasando por','el estaba paseando su perro en',]
place=['las montañas','el jardin']
second_character=['cuandio vio a un hombre','cuando vio a una mujer']
age=['que parecia tener unos 30 años','que pareciaa una persona mas vieja']
work=['buscando algo','cavando un pozo en la carretera']
saludo=['-hola...','-perdona,creo nos hemos visto antes...','-hey que estas haciendo?']
respuesta=['-no puedo conversar,''acabo de participar en un asesinato','largate de aqui',
           '-hola,que tal','¿me puedes ayudar?']
final=['Se trataba de un familiar suyo que estaba desaparecido hace 3 años']


print(random.choice(sentence_starter)+random.choice(character)+
      random.choice(time)+random.choice(story_pilot)+
     random.choice(place)+random.choice(second_character)+
     random.choice(age)+random.choice(work))
print((random.choice(saludo)))
print(random.choice(respuesta))



