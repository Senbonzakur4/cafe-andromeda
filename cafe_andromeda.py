# Programa Cafe Andromeda v1.1

## Descripcion: Este programa simula el proceso de compra de una cafeteria, le muestra al usuario el menu de bebidas y alimentos
## de los cuales el puede elegir cuantas bebidas y alimentos llevar (o no llevar), asi como cuantas unidades de cada uno.
## Al terminar la seleccion de Bebidas y Alimentos, se le pide el nombre para mostrarle el ticket de compra.
## Despues el programa pregunta si un usuario nuevo ingresara otro pedido para repetir el ciclo.
## Si ya no habran mas pedidos, se muestra un resumen de la venta del dia asi como los ingresos totales.

### Declaracion de variables
menu = [['Expresso', 'Americano', 'Capuccino', 'Latte', 'Refresco'],    # Menu de Bebidas
        ['Sandwich', 'Galleta', 'Dona', 'Pan', 'Rebanada de Pastel']]   # Meenu de Alimentos
precios = [[42.00, 51.00, 64.00, 71.00, 33.00],
           [68.00, 24.00, 16.00, 12.00, 48.00]]
clientes, cliente, subtotal, unidades, precio_unitario = [], [], [], [], []  # Cliente = Seleccion del menu del usuario actual
opcion, unidad, sub_ticket = 0, 0, 0                                         # Clientes = Lista donde se guardara toda la info. del usuario actual para resetear las listas para el proximo usuario
decision, nombre = "si", " "
total = 0

### Funciones


### Ejecucion del programa

while decision == 'si':                                # Mientras la decision sea 'si' el programa seguira funcionando para agregar mas ventas.
    print(f"\n=== Bienvenido a Cafe Andromeda ===")

    while decision == 'si':
        print(f"\n======= Menu de Bebidas =======")
        for i in range (len(menu[0])):
            print(f"{i+1}- {menu[0][i]:<24}$ {precios[0][i]:2.2f}")

        while True:       # Validacion para evitar datos equivocados como ingresar letras o numeros que no estan en el menu.
            opcion = input(f"\nSeleccione su Bebida escribiendo el numero junto a ella o ENTER para no seleccionar ninguna: ")

            if opcion == "":
                print(f"\nDecidio no llevar bebida.")
                break

            if opcion.isdigit():
                opcion = int(opcion)

                if 1 <= opcion <= 5:
                    print(f"\nLa bebida que selecciono es: {menu[0][opcion - 1]}")

                    while True:        # Validacion para comprobar que las unidades requeridas por el cliente no sean cero o numero negativo.
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

        while True:          # Se le pregunta al usuario si desea agregar mas bebidas
            decision = input(f"\nDeseas agregar otra bebida?\nEscribe 'si' o 'no' para continuar: ").strip().lower()

            if decision == 'no':
                print(f"\nDecidio no llevar mas bebidas.")
                break

            elif decision == 'si':
                break

            else:
                print(f"\nDato no valido. ")

    decision = 'si'   # Si decidio no llevar mas bebidas, se cambia decision = 'si' para que el while de menu de alimentos arranque.

    while decision == 'si':
        print(f"\n======= Menu de Alimntos =======")
        for i in range (len(menu[1])):
            print(f"{i+1}- {menu[1][i]:<24}$ {precios[1][i]:2.2f}")

        while True:         # Validacion para evitar datos equivocados como ingresar letras o numeros que no estan en el menu.
            opcion = input(f"\nSeleccione su Alimento escribiendo el numero junto a el o ENTER para no seleccionar ninguno: ")

            if opcion == "":
                print(f"\nDecidio no llevar Alimento.")
                break

            if opcion.isdigit():
                opcion = int(opcion)

                if 1 <= opcion <= 5:
                    print(f"\nEl Alimento que selecciono es: {menu[1][opcion - 1]}")

                    while True:            # Validacion para comprobar que las unidades requeridas por el cliente no sean cero o numero negativo.
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

        while True:     # Se le pregunta al usuario si desea agregar otro alimento.
            decision = input(f"\nDeseas agregar otro alimento?\nEscribe 'si' o 'no' para continuar: ").strip().lower()

            if decision == 'no':
                print(f"\nDecidio no llevar mas alimentos.")
                break
        
            elif decision == 'si':
                    break

            else:
                    print(f"\nDato no valido. ")

    # Si decidio ya no llevar nada mas, se le pide su nombre para mostrarle el ticket detallado.
    nombre = input(f"\nIngrese su nombre para generar el Ticket:\n")
    print(f"\n\n\n=================================== Su Ticket =========================================")
    print(f"Nombre: {nombre}\n=======================================================================================")
    print(f"Cantidad\tProducto\t\t\tPrecio Unitario\t\tImporte\n=======================================================================================")
    for producto in range(len(cliente)):
        sub_ticket += subtotal[producto]
        print(f"   {unidades[producto]:<12} {cliente[producto]:<35} $ {precio_unitario[producto]:<18.2f}$ {subtotal[producto]:2.2f}")
    print(f"=======================================================================================")
    print(f"{"Subtotal:":>71} $ {sub_ticket:<2.2f}\n{"I.V.A.:":>71} $ {sub_ticket * .16:<2.2f}\n{"Total:":>71} $ {sub_ticket * 1.16:2.2f}")
    print(f"=======================================================================================")

    # Se agrega toda la informacion del cliente actual a la matriz 'clientes' y se resetean todas las listas para poder ser usadas por el siguiente usuario.
    clientes.append([nombre, unidades, cliente, precio_unitario, subtotal])
    nombre, unidades, cliente, precio_unitario, subtotal, sub_ticket = "", [], [], [], [], 0

    while True:   # El programa pregunta si un nuevo cliente hara uso de el, si no es asi, se pasa a mostrar el corte de venta de la cafeteria.
        decision = input(f"\nDeseas registrar un nuevo pedido?\nEscribe 'si o 'no': ").strip().lower()

        if decision == 'no':
            print(f"\nSu decision fue no registrar mas pedidos.\nSe mostrara el corte del punto de venta:\n")
            break

        elif decision == 'si':
            print(f"\nRegistrando un nuevo pedido . . .\n\n\n")
            break

        else:
            print(f"\nDato no valido.")


    # Este es el corte del dia, donde se muestra un resumen de los clientes y al final las ganancias totales del dia.
print(f"\n=========================== Ventas del Dia - Cafe Andromeda ===========================\n\n\n")
print(f"Clientes de hoy: {len(clientes)}\n=======================================================================================")

for i in range(len(clientes)):
    sub_ticket = 0
    print(f"\n\n\nNombre: {clientes[i][0]}\n=======================================================================================")
    print(f"{"Cantidad":<20} {"Producto":<21} {"Precio Unitario":<28} {"Importe":<23}\n=======================================================================================")


    for j in range(len(clientes[i][2])):
        sub_ticket += clientes[i][4][j]
        print(f"    {clientes[i][1][j]:<16} {clientes[i][2][j]:<25} $ {clientes[i][3][j]:<22.2f} $ {clientes[i][4][j]:<20.2f}")
    print(f"=======================================================================================")
    print(f"{"Subtotal:":>71} $ {sub_ticket:<2.2f}\n{"I.V.A.:":>71} $ {sub_ticket * .16:<2.2f}\n{"Total:":>71} $ {sub_ticket * 1.16:2.2f}")
    print(f"=======================================================================================")
    total += sub_ticket * 1.16

print(f"\nGanancias totales del dia de hoy:  $ {total:2.2f}\n\n")

### Fin del Programa 