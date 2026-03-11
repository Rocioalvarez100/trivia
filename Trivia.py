'''```
# trivia
# es juego de triviaaa!
# Challenge: Mini Trivia en Python

## Debes crear:
Un archivo llamado `trivia.py`

## Tu programa debe:
- pedir el nombre del jugador
- mostrar una bienvenida
- hacer 4 preguntas
- sumar 1 punto por cada respuesta correcta
- mostrar el nombre y el puntaje final

## Resultado final
- si `puntaje == 4` → **Excelente**
- si `puntaje >= 2` → **Muy bien**
- si no → **Puedes mejorar**

## Recuerda
- trabaja paso a paso
- no hace falta terminar perfecto
- usa Git durante el proceso
- haz varios commits pequeños```'''
nombre= input("Ingresa el nombre del jugador: ")
print("Welcome!")
puntaje= 0
pregunta1= (print("Cuanto es 9x9: "))
pregunta2= (print("Cuando es navidad?: "))
pregunta3=(print("Que se celebra el 25 de diciembre: "))
pregunta4= (print("Cuanto es 90x10: "))

respuestacorrecta1= 81
respuestacorrecta2= '25 de diciembre'
respuestacorrecta3= 'Navidad'
respuestacorrecta4= '900'


respuesta1= input("Ingresa la respuesta de la pregunta 1: ")
respuesta2= input("Ingresa la respuesta de la pregunta 2: ")
respuesta3= input("Ingresa la respuesta de la pregunta 3: ")
respuesta4= input("Ingresa la respuesta de la pregunta 4: ")
if 