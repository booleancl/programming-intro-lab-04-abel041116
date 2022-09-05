# Una funcion es un grupo de sentencias con un nombre que realizan una computacion.
# Primero uno define una funcion y luego de "llama" o "ejecuta" esa funcion.

# Python viene con muchas funciones listas para usar.
# Solo hay que llamarla o ejecutarlas
print("Hola Pao")

# La mayoria de las funciones entregan un valor, es decir, nos devuelven el resultado. Ejemplo:

str_num = '32' # Esto es un string que parece numero
real_num = int(str_num) # Esta funcion trasforma a entero
print(type(real_num))

float_num = 3.9999
int_num = int(float_num) # No aproxima, corta la parte decimal
print(int_num)

# La siguiente linea es un errror
# int("Hola inmundo")

print(float('32')) # Esta funcion entrega un float
print(str(3.1415)) # Esta funcion entrega un str

# Composicion de funciones: Anidar funciones

print(str(3.14.15))