# Las funciones pueden hacer cosas y tambien pueden retornar valores

def circle_area(radius):
    area = 3.1415*radius**2
    return area

# En este caso la funcion me entrega o devuelve el valor

result = circle_area(4)
print(result)
def circle_volumen(radius,height):
    volumen = 3.1415*radius**2*height
    return volumen

result_two = circle_volumen(4,10)
print(result_two)