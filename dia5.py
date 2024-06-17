claves = ['nombre', 'apellido', 'correo']  
valores = ["Maria", "Lopez", "marialopez@gmail.com"]       

diccionario = {}

for indice in range(len(claves)):
    diccionario[claves[indice]] = valores[indice]
print(diccionario)