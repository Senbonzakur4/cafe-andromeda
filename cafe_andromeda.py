#  Programa Cafe Andromeda v1.0

# Descripcion: Este programa simula el proceso de compra de una cafeteria, le muestra al usuario el menu de bebidas y alimentos
# de los cuales el puede elegir uno de cada uno o ninguno, luego le pregunta cuantas unidades del producto llevara, asi como su
# precio unitario, por ultimo, le pide al cliente su nombre para generar un ticket de compra con el detalle de sus productos,
# cuantos llevo, a que precio, subtotal, iva y total a pagar.

# Declaracion de variables
cuenta, cantidad_producto, precio_unitario = [], [], []
bebidas = ['Expresso', 'Americano', 'Capuccino', 'Latte', 'Refresco']
alimentos = ['Sandwich', 'Galleta', 'Rebanada de pastel', 'Dona']
producto_elegido, subtotal, iva, total, = 0, 0, 0,0
decision, nombre = 'si', "" 
i = 1

# Funciones


# Ejecucion del programa
print(f"\n=== Bienvenido a Cafe Andromeda ===")

# Se muestra el menu de bebidas

print(f"\n=== Bebidas disponibles:\n")
for bebida in bebidas:
    print(f" {i} - {bebida}")
    i += 1

# Validacion de bebida elegida por el usuario

producto_elegido = int(input(f"\n Ingrese el numero del producto que desea comprar: \n (Ingrese 0 para no llevar ninguna Bebida). "))
while producto_elegido < 0 or producto_elegido > 5: 
    print(f"\n Opcion no valida, por favor ingrese un numero del 0 al 5.\n")
    producto_elegido = int(input(f" Ingrese el numero del producto que desea comprar: \n (Ingrese 0 para no llevar ninguna Bebida). "))
if producto_elegido != 0:
    cuenta.append(bebidas[producto_elegido - 1])

# Si el usuario no eligio ninguna bebida, el programa se saltara los pasos de preguntar cuantas unidades llevara y el precio unitario.
# Si el usuario eligio una bebida, se guardara el nombre de la bebida en la lista 'cuenta' para mostrar en el ticket de compra.

# Validacion de cantidad de bebidas que llevara el usuario, nos aseguramos que ingrese un numero entero mayor o igual a 1.

if producto_elegido != 0:
    cantidad_producto.append(int(input(f"\n Ingrese la cantidad del producto que llevara: ")))
    while cantidad_producto[-1] <= 0:
        print(f"\n Cantidad no valida, por favor ingrese un numero entero mayor a 0.")
        cantidad_producto[-1] = int(input(f"\n Ingrese la cantidad del producto que llevara: "))
    

# Validacion del precio unitario de la bebida, nos aseguramos de que el precio sea mayor a 0.     

if producto_elegido != 0:
    precio_unitario.append(float(input(f"\n Ingrese el precio del producto: ")))
    while precio_unitario[-1] <= 0:
        print(f"\n Precio no valido, por favor ingrese un numero mayor a 0.")
        precio_unitario[-1] = float(input(f"\n Ingrese el precio del producto: "))

if producto_elegido !=0:
    subtotal = cantidad_producto[-1] * precio_unitario[-1]
print(f"\n Subtotal: $ {subtotal:.2f}")

# Aqui se valida que el usuario ingrese 'si' o 'no' y nos aseguramos que no se salte la seccion de
# alimentos por un error de dedo o por ingresar un numero.

decision = input(f"\n Desea agregar algun alimento? (si/no): ").lower()
while decision != 'si' and decision != 'no':
    print(f"\n Opcion no valida, por favor ingrese 'si' o 'no'.")
    decision = input(f"\n Desea agregar algun alimento? (si/no): ").lower()

if decision == 'si':
    i = 1

# Se muestra el menu de alimentos

    print(f"\n=== Alimentos disponibles: \n")
    for alimento in alimentos:
        print(f" {i} - {alimento}")
        i += 1

# Validacion de alimento elegido por el usuario   

    producto_elegido = int(input(f"\n Ingrese el numero del producto que desea comprar: \n (Ingrese 0 para no llevar ningun Alimento). "))
    while producto_elegido < 0 or producto_elegido > 4:
        print(f"\n Opcion no valida, por favor ingrese un numero del 0 al 4.\n")
        producto_elegido = int(input(f" Ingrese el numero del producto que desea comprar: \n (Ingrese 0 para no llevar ningun Alimento). "))
    if producto_elegido != 0:
        cuenta.append(alimentos[producto_elegido - 1])

# Si el usuario no eligio ningun alimento, el programa se saltara los pasos de preguntar cuantas unidades llevara y el precio unitario.
# Si el usuario eligio un alimento, se guardara el nombre del alimento en la lista 'cuenta' para mostrar en el ticket de compra.

# Validacion de cantidad de alimentos que llevara el usuario, nos aseguramos que ingrese un numero entero mayor o igual a 1.

    if producto_elegido != 0:
        cantidad_producto.append(int(input(f"\n Ingrese la cantidad del producto que llevara: ")))
        while cantidad_producto[-1] <= 0:
            print(f"\n Cantidad no valida, por favor ingrese un numero mayor a 0.")
            cantidad_producto[-1] = int(input(f"\n Ingrese la cantidad del producto que llevara: "))

# Validacion del precio unitario del alimento, debe ser un numero mayor a 0.
    
    if producto_elegido != 0:
        precio_unitario.append(float(input(f"\n Ingrese el precio del producto: ")))
        while precio_unitario[-1] <= 0:
            print(f"\n Precio no valido, por favor ingrese un numero mayor a 0.")
            precio_unitario[-1] = float(input(f"\n Ingrese el precio del producto: "))

    if producto_elegido != 0:
        subtotal = cantidad_producto[-1] * precio_unitario[-1]
        print(f"\n Subtotal: $ {subtotal:.2f}")
    else:
        subtotal = 0
        print(f"\n Subtotal: $ {subtotal:.2f}")

# Por ultimo se le pide al usuario que ingrese su nombre para recoger el pedido, se valida que el espacio de nombre no este vacio.

nombre = input(f"\n Ingresa tu nombre para generar ticket de compra: ")
while nombre == "":
    print(f"\n El nombre debe tener al menos un caracter, por favor ingrese un nombre valido.")
    nombre = input(f"\n Ingresa tu nombre para generar ticket de compra: ")

# Se genera el ticket de compra, tambien reiniciamos la variable 'subtotal' a 0, ya que la usaremos para calcular el subtotal del ticket

subtotal = 0
i = 1
print(f"\n\n\n=============== Ticket de compra ================= \n")
print(f" Cliente: {nombre}")
print(f"===================================================\nProductos: {len(cuenta)}\n===================================================")

for i in range(len(cuenta)):
    print(f"-  {cantidad_producto[i]}  {cuenta[i]}\t\t\t\t   $ {precio_unitario[i]:.2f}")
    subtotal += cantidad_producto[i] * precio_unitario[i]
print(f"\n\t\t\t\tSubtotal:  $ {subtotal:.2f}")
print(f"\t\t\t\tI.V.A.:    $ {subtotal * 0.16:.2f}")
print(f"\t\t\t\tTotal:     $ {subtotal * 1.16:.2f}\n\n=============== Gracias por su Compra ==============\n=================== Vuelva Pronto ==================\n")