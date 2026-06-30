# Cafe Andromeda

### Declaracion de Variables

menu = [['Expresso', 'Americano', 'Capuccino', 'Latte', 'Refresco'],    # Menu de Bebidas
        ['Sandwich', 'Galleta', 'Dona', 'Pan', 'Rebanada de Pastel']]   # Meenu de Alimentos
precios = [[42.00, 51.00, 64.00, 71.00, 33.00],
           [68.00, 24.00, 16.00, 12.00, 48.00]]
clientes, cliente, subtotal, unidades, precio_unitario = [], [], [], [], []  # Cliente = Seleccion del menu del usuario actual
opcion, unidad, sub_ticket = 0, 0, 0                                         # Clientes = Lista donde se guardara toda la info. del usuario actual para resetear las listas para el proximo usuario
decision, nombre = "si", " "
total = 0

### Definicion de Funciones

def menu_de_bebidas(menu, precios): # Muestra el menu de bebidas y sus precios.
    print(f"\n========== Menu de Bebidas ==========")
    for i in range (len(menu[0])):
        print(f"{i + 1}- {menu[0][i]:<24} $ {precios[0][i]:2.2f}")

def menu_de_alimentos(menu, precios): # Muestra el menu de alimentos y sus precios.
    print(f"\n========= Menu de Alimentos =========")
    for i in range (len(menu[1])):
        print(f"{i + 1}- {menu[1][i]:<24} $ {precios[1][i]:2.2f}")
      
def eleccion_de_bebida(): # Permite al usuario seleccionar una bebida del menu.
    while True:
        opcion = input(f"\nSeleccione su Bebida escribiendo el numero junto a ella o ENTER para no seleccionar ninguna: ")

        if opcion == "":
            print(f"\nDecidio no llevar bebida.")
            break

        if opcion.isdigit():
            opcion = int(opcion)

            if 1 <= opcion <= 5:
                print(f"\nLa bebida que selecciono es: {menu[0][opcion - 1]}")
                return opcion
            else:
                    print(f"\nDato no Valido.")
        else:
                print(f"\nDato no Valido.")

def eleccion_de_alimento(): # Permite al usuario seleccionar un alimento del menu.
    while True:
        opcion = input(f"\nSeleccione su Alimento escribiendo el numero junto a el o ENTER para no seleccionar ninguno: ")

        if opcion == "":
            print(f"\nDecidio no llevar alimento.")
            break

        if opcion.isdigit():
            opcion = int(opcion)

            if 1 <= opcion <= 5:
                print(f"\nEl alimento que selecciono es: {menu[1][opcion - 1]}")
                return opcion
            
            else:
                    print(f"\nDato no Valido.")
        else:
                print(f"\nDato no Valido.")

def cantidad_de_bebidas(): # Permite al usuario ingresas la cantidad de unidades de la bebida seleccionada.
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
                return

            else:
                print(f"Dato no valido.")

        else:
            print("Dato no valido.")

def cantidad_de_alimentos(): # Permite al usuario ingresas la cantidad de unidades del alimento seleccionado.
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
                return

            else:
                print(f"Dato no valido.")

        else:
            print("Dato no valido.")

def seguir_comprando(): # Validacion de si el usuario quiere otra bebida o alimento.
     while True:
        decision = input().strip().lower()

        if decision == 'si' or decision == 'no':
            return decision
        
        else:
            print(f"\nDato no valido.\nDesea llevar otro Producto?\n(Si/No): ")

def nuevo_cliente(): # Validacion de si el usuario quiere registrar un nuevo pedido.
    while True:
        decision = input(f"\nDeseas registrar un nuevo pedido?\n(Si/No): ").strip().lower()

        if decision == 'no':
            print(f"\nDecidio no registrar mas pedidos.\nSe mostrara el corte del punto de venta:\n")
            return decision

        elif decision == 'si':
            print(f"\nRegistrando un nuevo pedido . . .\n\n\n")
            return decision

        else:
            print(f"\nDato no valido.")

def formato_ticket(sub_ticket=0): # Muestra el ticket del pedido del cliente actual.
    print(f"\n\n\n=================================== Su Ticket =========================================")
    print(f"Nombre: {nombre}\n=======================================================================================")
    print(f"Cantidad\tProducto\t\t\tPrecio Unitario\t\tImporte\n=======================================================================================")
    for producto in range(len(cliente)):
        sub_ticket += subtotal[producto]
        print(f"   {unidades[producto]:<12} {cliente[producto]:<35} $ {precio_unitario[producto]:<18.2f}$ {subtotal[producto]:2.2f}")
    print(f"=======================================================================================")
    print(f"{"Subtotal:":>71} $ {sub_ticket:<2.2f}\n{"I.V.A.:":>71} $ {sub_ticket * .16:<2.2f}\n{"Total:":>71} $ {sub_ticket * 1.16:2.2f}")
    print(f"=======================================================================================")

def formato_ticket_final(): # Muestra el ticket final del dia con todos los clientes y sus pedidos.
    print(f"\n=========================== Ventas del Dia - Cafe Andromeda ===========================\n\n\n")
    print(f"Clientes de hoy: {len(clientes)}\n=======================================================================================")
    total = 0
    
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
    return total


### Inicio del Programa

while decision == 'si': # decision = "si" para iniciar el programa y permitir al usuario registrar un pedido.
    print(f"\n==== Bienvenido a Cafe Andromeda ====")

    while decision == 'si':
        menu_de_bebidas(menu, precios)  # Muestra el menu de bebidas y sus precios.
        opcion = eleccion_de_bebida()
        if opcion is not None:  # Si el usuario dio ENTER para no seleccionar ninguna bebida, no se le pedira la cantidad de unidades.
            cantidad_de_bebidas()
        print(f"\nDesea llevar otra Bebida?\n(Si/No): ")
        decision = seguir_comprando()   # Si el usuario eligio 'si' se reinicia el ciclo para permitirle agregar otra bebida.

    decision = 'si'

    while decision == 'si':
        menu_de_alimentos(menu, precios) # Muestra el menu de alimentos y sus precios.
        opcion = eleccion_de_alimento()
        if opcion is not None:  # Si el usuario dio ENTER para no seleccionar ningun alimento, no se le pedira la cantidad de unidades.
            cantidad_de_alimentos()
        print(f"\nDesea llevar otro Alimento?\n(Si/No): ")
        decision = seguir_comprando()   # Si el usuario eligio 'si' se reinicia el ciclo para permitirle agregar otro alimento.

    nombre = input(f"\nIngrese su nombre para generar el ticket:\n")

    formato_ticket(sub_ticket)  # Muestra el ticket del pedido del cliente actual.

    clientes.append([nombre, unidades, cliente, precio_unitario, subtotal])     # Agrega la informacion del cliente actual a la lista de clientes para poder mostrarla en el ticket final.
    nombre, unidades, cliente, precio_unitario, subtotal, sub_ticket = "", [], [], [], [], 0 # Resetea las listas para el proximo cliente.

    decision = nuevo_cliente() # Pregunta al usuario si desea registrar un nuevo pedido, si elige 'si' se reinicia el ciclo para permitirle registrar otro pedido.

total = formato_ticket_final() # Muestra el ticket final del dia con todos los clientes y sus pedidos, tambien asignando el total de ganancias del dia a la variable total.
print(f"\n\n- Ganancias totales del dia de hoy:  $ {total:2.2f}\n\n") # Muestra el total de ganancias del dia.

### Fin del Programa