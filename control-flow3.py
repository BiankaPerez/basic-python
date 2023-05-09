#https://www.pythontutorial.net/python-basics/python-if/
 #statement
points = int(input("Ingresa tus puntos:"))
if points >= 500:
    discount = 20 # discount in food
elif points >= 250:
    discount = 10 #discount in food
else:
    discount = 0
if discount > 0:
    print (f"Recibiste un descuento de {discount}% !")

color = input("Ingresa tu color favorito: ")
if color == "rojo":
    print("El color rojo me recuerda a las rosas!")
elif color == "azul":
    print("El azul es un color brillante.")
else:
    print("Ese un color muy bonito!")

combo = input("Ingresa tu combo: ")
if combo == "coca-cola + hamburguesa":
    print("El combo tiene un precio de 30$")
elif combo == "palomitas y coca-cola":
    print("El combo cuesta 150$")
else:
    print("Lo siento, no tenemos ese combo disponible.")

    # ternary operator
#1 
numero = int(input("Ingresa un número: "))
mensaje = "El número es par" if numero % 2 == 0 else "El número es impar"
print(mensaje)

#2
color = "rojo"
is_red = True if color == "rojo" else False

if is_red:
    print("Esta flor es roja")
else:
    print("Esta flor no es roja")
#3
answer = input("¿Quieres continuar? (s/n): ")
can_continue = True if answer.lower() == "s" else False

if can_continue:
    print("Continuando...")
else:
    print("Saliendo del programa...")
    # for loop with range 
#1
for i in range(18, 0, -1):
    print(i)
 #2 numeros pares
for i in range(2, 8, 2):
    print(i)
#3 Colores diferentes al azar
import random
for i in range(4):
    color = random.choice(['rosa', 'azul', 'gris', 'amarillo', 'rojo'])
    tono = random.choice(['claro', 'oscuro'])
    print(f"Color # {i+1}: {color},{tono}")
#While statment 
#1
x=1
while (x<=5):
    x=x**2
    print (x)
    x=x+1 
#2
i=1
t=0
while i<=5:
    print (i)
    i=i+1
#3
n = int(input("Ingresa un número entero positivo: "))
suma = 0
i = 2
while i <= n:
    suma += i
    i += 2
    print("La suma de todos los números pares entre 1 y", n, "es", suma)    

    
