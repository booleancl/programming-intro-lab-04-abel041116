# Los arreglos son una ESTRUCTURA DE DATOS FUNDAMENTALES
# que permite agrupar valores

first_array = ['Sacar la basura', 'peinarse', 'dormir', 'secar la ropa']

# En python el primer elementode un arreglo tiene posicion (indice) 0
print(first_array[0])
print(first_array[1])
print(first_array[2])
print(first_array[3])
# No existen el elemento con indice 4 y python da un error
# print(first_array[4])

# Podemos saber el largo de un arreglo o lista con la funcion pre definida len()

print(len(first_array))

# Ademas, podemos agregar elementos al arreglo con el metodo append
first_array.append('comer')
first_array.append('dormir')

# Podemos indicar la posicion del nuevo elemento a agregar con insert
first_array.insert(0,'levantarse')

# Podemos imprimir la lista completa
print(first_array)

