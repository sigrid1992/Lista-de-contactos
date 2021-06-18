# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:19:17 2021

@author: sigri
"""

# estos son los datos que vamos a solicitar para cada contacto
campos = ('nombre', 'apellidos', 'email', 'teléfono')

# esta lista contendrá todos los contactos
contactos = []

# inicialimos la variable 'seguir'
seguir = 's'

# mientras el valor de seguir sea 's' o 'S' introducimos contactos
while seguir in ('s', 'S'):
    
    # este diccionario almacena los valores de un contacto
    contacto = {}    
    
    # con este bucle preguntamos campo a campo
    for campo in campos:
        valor = input(campo + ': ')
        
        # si el usuario introduce algo, se almacena
        if len(valor) > 0:
            contacto[campo] = valor
    
    # añadimos el contacto a la lista
    contactos.append(contacto)
    
    # preguntamos si seguimos añadiendo contactos
    seguir = input('¿Introducir otro contacto? s/n:')
    
# mostramos todos los contactos
for contacto in contactos:
    
    for k, v in contacto.items():
        print(k + ': ' + v)
        
    # mostramos esto para facilitar la lectura
    print('------')

# pedimos al programa que nos de el total de contactos introducidos
print("Total contactos: ",

   len(contactos));

# pedimos al programa que nos de el total de contactos introducidoscon email
print("Total contactos con email: ",

# usamos c que es una lista de contactos que hay que cada c(diccionarios) a lo
# que llamamos lista de conversion
   len([c for c in contactos if 'email' in c.keys()]));

# 3. Escribe el código para mostrar los datos del usuario cuyo correo electrónico 
# haya sido introducido por teclado.
# Si no existe contacto alguno con ese correo electrónico,
# se mostrara el mensaje “No encontrado”.

nombre = str(input("nombre contacto con email: "))
nombre
if nombre in contacto.items():
   print (contacto['email'])
    
else:
    print(" No encontrado")



    
    