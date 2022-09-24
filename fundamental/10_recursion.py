import time

# Es perfectamente posible llamar una funcion dentro de otra
# Lo hicimos cuando calculamos el volumen de un cilindro.

# Pero tambien es perfectamente posible que una funcion se llame a si misma
# Esto es una tecnica muy poderosa para ciertos problemas

# funcion conteo regresivo
# Es una funcion que se llama a si misma
def countdown(number):
    if number <= 0:
      print("KABUUMM")
    else:
      print(number)
      time.sleep(0.5)
      countdown(number - 1)

countdown(5)

def super_sum(number):
    if number <= 0:
        return number
    else:
        return number + super_sum(number - 1)

print(super_sum(3))

# Recursion infinita, sin condiciones de salida
# para nada util, pero entretenido
def infinite():
  infinite()

infinite()