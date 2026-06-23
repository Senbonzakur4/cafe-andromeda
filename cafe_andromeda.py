# Programa Cafe Andromeda v1.1

# Descripcion: Este programa simula el proceso de compra de una cafeteria, le muestra al usuario el menu de bebidas y alimentos
# de los cuales el puede elegir uno de cada uno o ninguno, luego le pregunta cuantas unidades del producto llevara, asi como su
# precio unitario, por ultimo, le pide al cliente su nombre para generar un ticket de compra con el detalle de sus productos,
# cuantos llevo, a que precio, subtotal, iva y total a pagar.

# Declaracion de variables
menu = [['Expresso', 'Americano', 'Capuccino', 'Latte', 'Refresco'],    # Menu de Bebidas
        ['Sandwich', 'Galleta', 'Dona', 'Pan', 'Rebanada de Pastel']]   # Meenu de Alimentos
precios = [[42.00, 51.00, 64.00, 71.00, 33.00],
           [68.00, 24.00, 16.00, 12.00, 48.00]]
clientes, cliente, subtotal, unidades, precio_unitario = [], [], [], [], []
opcion, decision, unidad, nombre = 0, "si", 0, ""

# Funciones


# Ejecucion del programa

#while decision == 'si':
print(f"\n=== Bienvenido a Cafe Andromeda ===")

while decision == 'si':
    print(f"\n======= Menu de Bebidas =======")
    for i in range (len(menu[0])):
        print(f"{i+1}- {menu[0][i]:<24}$ {precios[0][i]:2.2f}")

    while True:
        opcion = input(f"\nSeleccione su Bebida escribiendo el numero junto a ella o ENTER para no seleccionar ninguna: ")

        if opcion == "":
            print(f"\nDecidio no llevar bebida.")
            break

        if opcion.isdigit():
            opcion = int(opcion)

            if 1 <= opcion <= 5:
                print(f"\nLa bebida que selecciono es: {menu[0][opcion - 1]}")

                while True:
                    unidad = input(f"\nCuantas unidades de {menu[0][opcion - 1]} llevara: ")

                    if unidad.isdigit():
                        unidad = int(unidad)

                        if unidad >= 1:
                            print(f"\nDecidio llevar {unidad} unidades de {menu[0][opcion - 1]}.")
                            cliente.append(menu[0][opcion - 1])
                            subtotal.append(unidad * precios[0][opcion - 1])
                            unidades.append(unidad)
                            precio_unitario.append(precios[0][opcion - 1])
                            break

                        else:
                            print(f"Dato no valido.")

                    else:
                        print("Dato no valido.")
                break

            else:
                print(f"\nDato no valido, por favor ingresa el numero junto a la bebida o presiona ENTER para no seleccionar ninguna: ")

        else:
            print(f"\nDato no valido, por favor ingresa el numero junto a la bebida o presiona ENTER para no seleccionar ninguna: ")

    while True:
        decision = input(f"\nDeseas agregar otra bebida?\nEscribe 'si' o 'no' para continuar: ").strip().lower()

        if decision == 'no':
                print(f"\nDecidio no llevar mas bebidas.")
                break

        elif decision == 'si':
                break

        else:
            print(f"\nDato no valido. ")

decision = 'si'

while decision == 'si':
    print(f"\n======= Menu de Alimntos =======")
    for i in range (len(menu[1])):
        print(f"{i+1}- {menu[1][i]:<24}$ {precios[1][i]:2.2f}")

    while True:
        opcion = input(f"\nSeleccione su Alimento escribiendo el numero junto a el o ENTER para no seleccionar ninguno: ")

        if opcion == "":
            print(f"\nDecidio no llevar Alimento.")
            break

        if opcion.isdigit():
            opcion = int(opcion)

            if 1 <= opcion <= 5:
                print(f"\nEl Alimento que selecciono es: {menu[1][opcion - 1]}")

                while True:
                    unidad = input(f"\nCuantas unidades de {menu[1][opcion - 1]} llevara: ")

                    if unidad.isdigit():
                        unidad = int(unidad)

                        if unidad >= 1:
                            print(f"\nDecidio llevar {unidad} unidades de {menu[1][opcion - 1]}.")
                            cliente.append(menu[1][opcion - 1])
                            subtotal.append(unidad * precios[1][opcion - 1])
                            unidades.append(unidad)
                            precio_unitario.append(precios[1][opcion - 1])
                            break

                        else:
                            print(f"Dato no valido.")

                    else:
                        print("Dato no valido.")
                break

            else:
                print(f"\nDato no valido, por favor ingresa el numero junto al alimento o presiona ENTER para no seleccionar ninguno: ")

        else:
            print(f"\nDato no valido, por favor ingresa el numero junto al alimento o presiona ENTER para no seleccionar ninguno: ")

    while True:
        decision = input(f"\nDeseas agregar otro alimento?\nEscribe 'si' o 'no' para continuar: ").strip().lower()

        if decision == 'no':
            print(f"\nDecidio no llevar mas alimentos.")
            break
        
        elif decision == 'si':
                break

        else:
                print(f"\nDato no valido. ")

nombre = input(f"\nIngrese su nombre para generar el Ticket:\n")
print(f"\n\n\n=================================== Su Ticket =========================================")
print(f"Nombre: {nombre}\n=======================================================================================")
print(f"Cantidad\tProducto\t\t\tPrecio Unitario\t\tImporte\n=======================================================================================")
for producto in range(len(cliente)):
    print(f"   {unidades[producto]:<12} {cliente[producto]:<35} $ {precio_unitario[producto]:<18.2f}$ {subtotal[producto]:2.2f}")

clientes.append([nombre, unidades, cliente, precio_unitario, subtotal])
nombre, unidades, cliente, precio_unitario, subtotal = "", [], [], [], []

while True:
    decision = input(f"\nDeseas registrar un nuevo pedido?\nEscribe 'si o 'no': ").strip().lower()

    if decision == 'no':
        print(f"\nSu decision fue no registrar mas pedidos.\nSe mostrara el total de venta del dia de hoy:")
        break

    elif decision == 'si':
        print(f"\nRegistrando un nuevo pedido . . .\n\n\n")
        break

    else:
        print(f"\nDato no valido.")


print(f"\n========== Ventas del Dia - Cafe Andromeda ==========")
print(f"\nClientes de hoy: {len(clientes)}.")
print(clientes)