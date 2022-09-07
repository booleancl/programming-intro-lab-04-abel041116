# Tenemos expresiones que se pueden evaluar en terminos booleans
# o dicotomicos
# Ejemplo:

print(10 > 9)

# Esto nos permite hacer ejecuciones condicionales, por ejemplo:

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

Gaby_age = 4
Paola_age = 30

# Estas siguientes instrucciones las prodriamos leer como:
# "Si el resultado de is_adult ejecutada con la variable gaby_age
# es verdadero, entonces el programa imprime '¿Quieres una Cerveza?'
# De otro modo (else), imprime 'Cantemos Chuchuwa?'"

if is_adult(Paola_age):
    print("¿Quieres una Cerveza?")
else:
    print("Cantemos Chuchuwa?")

# elif es una abreviacion "else if", nos permite seguir evaluando espreciones. Podemos tener tantos como necesitemos

if Paola_age > Gaby_age:
    print("Paola es mayor que gaby")
elif paola_age < gaby_age:
    print("Paola es menor que Gaby")
else:
    print("Tiene la misma edad Gaby y Paola")