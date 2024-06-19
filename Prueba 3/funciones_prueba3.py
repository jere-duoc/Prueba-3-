sectores=["CENTRO", "NORTE", "SUR"]

def registrar(pedidos):
    while True:
        nombre=input("\nIngrese su nombre: ")
        if len(nombre)!=0:
            break
        else:
            print("Porfavor, Debe ingresar un nombre!")

    while True:
        direccion=input("\nIngrese su Dirección: ")
        if len(direccion)!=0:
            break
        else:
            print("Porfavor, Debe ingresar una dirección!")

    while True:
        sector=input("\nIngrese el Sector (Centro, Norte, Sur): ").upper()
        if sector not in sectores:
            print("Porfavor, Debe ingresar un sector valido!")
        else:
            break


    pequeno=0
    mediano=0
    grande=0
    maspaquetes=0
    while maspaquetes!=2:
        try:
            print("\nSeleccione el tamaño del paquete que desea registrar: ")
            print("(Para seleccionar escriba 1, 2 o 3)")
            print("1. Pequeño")
            print("2. Mediano")
            print("3. Grande")
            opcion_pedido=int(input("---> "))

            if opcion_pedido==1:
                while True:
                    try:
                        print("\nIngrese la cantidad de paquetes que desea registrar")
                        cantidad=int(input("---> "))
                        if cantidad>=1:
                            pequeno=pequeno+cantidad
                            break
                        else:
                            print("Porfavor una cantidad valida! (1, 3, 1000)")
                    except:
                        print("Porfavor una cantidad valida! (1, 3, 1000)")
                while True:
                    try:
                        print("\n¿Desea registrar otro paquete? (1.si/2.no)")
                        maspaquetes=int(input("---> "))
                        if maspaquetes==1:
                            break
                        elif maspaquetes==2:
                            break
                        else:
                            print("Porfavor Ingrese una opción valida! (1, 2)")
                    except:
                        print("Porfavor Ingrese una opción valida! (1, 2)")

            elif opcion_pedido==2:
                while True:
                    try:
                        print("\nIngrese la cantidad de paquetes que desea registrar")
                        cantidad=int(input("---> "))
                        if cantidad>=1:
                            mediano=mediano+cantidad
                            break
                        else:
                            print("Porfavor una cantidad valida! (1, 3, 1000)")
                    except:
                        print("Porfavor una cantidad valida! (1, 3, 1000)")
                while True:
                    try:
                        print("\n¿Desea registrar otro paquete? (1.si/2.no)")
                        maspaquetes=int(input("---> "))
                        if maspaquetes==1:
                            break
                        elif maspaquetes==2:
                            break
                        else:
                            print("Porfavor Ingrese una opción valida! (1, 2)")
                    except:
                        print("Porfavor Ingrese una opción valida! (1, 2)")
        
            elif opcion_pedido==3:
                while True:
                    try:
                        print("\nIngrese la cantidad de paquetes que desea registrar")
                        cantidad=int(input("---> "))
                        if cantidad>=1:
                            grande=grande+cantidad
                            break
                        else:
                            print("Porfavor una cantidad valida! (1, 3, 1000)")
                    except:
                        print("Porfavor una cantidad valida! (1, 3, 1000)")
                while True:
                    try:
                        print("\n¿Desea registrar otro paquete? (1.si/2.no)")
                        maspaquetes=int(input("---> "))
                        if maspaquetes==1:
                            break
                        elif maspaquetes==2:
                            break
                        else:
                            print("Porfavor Ingrese una opción valida! (1, 2")
                    except:
                        print("Porfavor Ingrese una opción valida! (1, 2")

            else:
                print("Porfavor Ingrese una opción valida! (1, 2, 3...)")
        except:
            print("Porfavor Ingrese una opción valida! (1, 2, 3...)")

    pedido={
        "nombre" : nombre,
        "direccion" : direccion,
        "sector" : sector,
        "Paquetes pequeños" : pequeno,
        "Paquetes medianos" : mediano,
        "Paquetes grandes" : grande
    }
    #pedido=[("nombre",nombre),("direccion", direccion),("sector", sector),("Paquetes pequeños", pequeno),("Paquetes medianos", mediano),("Paquetes grandes", grande)]
    pedidos.append(pedido)
            
def listar_pedidos(pedidos):
    if pedidos==[]:
        print("\nDeben haber pedidos registrados para listar los pedidos!")
        print("volviendo al menú...\n")
    else:
        print("\n",pedidos,"\n")


def imprimir_ruta(pedidos):
    while True:
        if pedidos==[]:
            print("\nDeben haber pedidos registrados para imprimir la hoja de ruta")
            print("volviendo al menú...\n")
            break
        else:
            with open("archivo.txt","w") as archivo:
                
                archivo.write(f"nombre: {pedidos["nombre"]}"), 
                archivo.write(f"\ndireccion: {pedidos["direccion"]}"),
                archivo.write(f"\nPaquetes pequeños: {pedidos["Paquetes pequeños"]}"),
                archivo.write(f"\nPaquetes medianos: {pedidos["Paquetes medianos"]}"),
                archivo.write(f"\nPaquetes grandes: {pedidos["Paquetes grandes"]}")
                archivo.close()
                break 
                         
                
                    

    # - Permitir al usuario seleccionar uno de los sectores 
    #     predefinidos (Centro, Norte, Sur).
    # - Generar un archivo de texto (.txt) con el detalle 
    #     de los pedidos para el sector seleccionado.
    # - El archivo de texto debe seguir el formato del 
    #     registro completo de pedidos.
