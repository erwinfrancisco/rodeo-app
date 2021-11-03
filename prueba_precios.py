import numpy as np
import pandas as pd

lista_articulos = ['budlight bote 355 ml', 'corona extra familiar 940 ml', 'michelo ultra media 355 ml']
lista_precio_1x = [12, 33, 17]
lista_precio_2x = [np.nan, 57, np.nan]
lista_precio_4x = [np.nan, np.nan, np.nan]
lista_precio_5x = [np.nan, np.nan, np.nan]
lista_precio_6x = [60, 342, 98]
lista_precio_7x = [np.nan, np.nan, np.nan]
lista_precio_8x = [np.nan, np.nan, np.nan]
lista_precio_9x = [np.nan, np.nan, np.nan]
lista_precio_10x = [np.nan, np.nan, np.nan]
lista_precio_11x = [np.nan, np.nan, np.nan]
lista_precio_12x = [110, np.nan, np.nan]

entrada = input('Ingresa el artículo: ')
cantidad = int(input('Cantidad: '))



if entrada == 'budlight bote 355 ml' and cantidad > 1 and cantidad <= 5:
    operacion = lista_precio_1x[0]*cantidad
    print(f'{entrada} x {cantidad} = ${float(operacion)}')

elif entrada == 'budlight bote 355 ml' and cantidad == 6:
    operacion = lista_precio_6x[0]*1
    print(f'{entrada} x {cantidad} = ${float(operacion)}')

elif entrada == 'budlight bote 355 ml' and cantidad >6 and cantidad < 12:
    piezas_unitarias = (cantidad - 6)
    calculo = lista_precio_6x[0] + piezas_unitarias*lista_precio_1x[0]
    print(f'Budlight 355 ml six pack = 1 x ${float(lista_precio_6x[0])}')
    print(f'Budlight bote 355 ml: {piezas_unitarias} x {lista_precio_1x[0]} = ', '$',float(piezas_unitarias*lista_precio_1x[0]))
    print('El precio a pagar es: ', '$',float(calculo))

elif entrada == 'budlight bote 355 ml' and cantidad % 12 == 0:
    cantidad = cantidad // 12
    operacion = lista_precio_12x[0]*cantidad
    print(f'{entrada} 12 pack x {cantidad} = ${float(operacion)}')
