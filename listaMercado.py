linea='__'
linea2='--'
print(linea*15)
print('| Programa Compra de Mercado |')
print(linea2*15)
bolsa=[]
articulo=0
cantidad=int(input('ingresa la cantidad de articulos que piensas comprar:\n'))
while articulo<cantidad:
    bolsa.append(input('\r\nIngresa que articulo vas a comprar:\n'))
    articulo+=1
print(linea*20)    
print('\r\nEsta es la Lista de los articulos:\r\n')

for articulo in bolsa:
    print(articulo)
print('\r\nEsta es la representacion bolsa del mercado\r\n',bolsa)