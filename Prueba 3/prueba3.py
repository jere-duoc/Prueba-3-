import funciones_prueba3 as fn

pedidos=[]
opcion_menu=0
sectores=["CENTRO", "NORTE", "SUR"]
#pedidos=[("nombre","jere"),("direccion", "direccion"),("sector", "SUR"),("Paquetes pequeños", 1),("Paquetes medianos", 2),("Paquetes grandes", 3)]
pedidos={
    "nombre": "jere",
    "direccion": "1 poniente",
    "sector": "SUR",
    "Paquetes pequeños": 1,
    "Paquetes medianos": 2,
    "Paquetes grandes": 3
}

while opcion_menu!=4:
    try:
        print(" ------------------------------------------ ")
        print("|               PaquExpress               |")
        print(" ------------------------------------------ ")
        print("Bienvenido a la aplicación de PaquExpress!")
        print("Seleccione una de las opciones a continuacion \n(Escriba 1, 2, 3 o 4 para seleccionar la opción)\n")
        print("1. Registrar pedido")
        print("2. Listar los todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        opcion_menu=int(input("---> "))

        #Registrar pedido
        if opcion_menu==1:
            fn.registrar(pedidos)

        #Listar los todos los pedidos
        elif opcion_menu==2:
            fn.listar_pedidos(pedidos)

        #Imprimir hoja de ruta
        elif opcion_menu==3:
            fn.imprimir_ruta(pedidos)
            print("Hoja de ruta impresa!\n")

        elif opcion_menu==4:
            print("")
    
    except ValueError:
        print("Porfavor Ingrese una opción valida! (1, 2, 3 o 4)")