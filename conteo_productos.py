'''Crea un scrip en python el cual le permita al usuario crear una lista de objetos
a inventariar, en esta debera poder almacenar nombre,codigo y precio de productos para
poder y una ves echo esto debera poder relizar un conteo fisico de sus productos,
una ves termine el conteo debera desplegarse el total de piezas contadas y valor monetario
de su inventario'''

productos={}


nombre=str(input('Escribe el nombre de producto: '))
codigo=int(input('Codigo de producto: '))
costo=float(input('Costo por unidad: $'))
cantidad=int(input('Cantidad encontrada: '))
