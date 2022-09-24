# Podemos crear o definir nuestras propias funciones
# Lo hacemos con la palabra especial "def" y el cuerpo
# la funcion debe ir correctamente indentado

def chuchuwa(inst):
    print("chuchuwa chuchuwa chuchuwa wa wa!")
    print("Chuchuwa chuchuwa chuchuwa wa wa!")
    print("Atencion, Compañia")
    print(inst)

print(chuchuwa)
print(type(chuchuwa))

# El llamado de la funcion
chuchuwa("Mano hacia el frente")
chuchuwa(" Hombro hacia atras")

# Las funciones deben llamarse o ejecutarse con los mismos parametros
result = chuchuwa("lengua afuera")

# Si la funcion no tiene un valor de retorno, nos entregara "none", que es para representar: "nada"
print(result)