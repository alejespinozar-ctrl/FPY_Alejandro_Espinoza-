def mostrar_menu():
    print("*** MENU PRINCIAL ***")
    print("1. Stock marca")
    print("2. Buscar por precio")
    print("3. Actualizar precio")
    print("4. Salir")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 1 and opcion <= 4:
                return opcion
            else:
                print("Debe seleccionar una opción válida (1 al 4)")
        except ValueError:
            print("Debe seleccionar una opción válida (ingrese solo números)")

def buscar_codigo(codigo, diccionario_inventario):
    codigo = codigo.strip().upper()
    for llave in diccionario_inventario.keys():
        if codigo == llave:
            return True
    return False

def stock_por_marca(marca_buscada, diccionario_productos, diccionario_inventario):
    marca_buscada = marca_buscada.strip().lower()
    acumulador_stock = 0

    for cod_prod, lista_atributos in diccionario_productos.items():
        if lista_atributos[0].strip().lower() == marca_buscada:
            for cod_inv, lista_inventario in diccionario_inventario.items():
                if cod_prod == cod_inv:
                    acumulador_stock += lista_inventario[1]
                    break
    
    print(f"Existen {acumulador_stock} unidades totales en stock para la marca {marca_buscada.upper()}")

def busqueda_por_precio(p_min, p_max, diccionario_productos, diccionario_inventario):
    lista_resultados = []

    for cod_inv, lista_inventario in diccionario_inventario.items():
        if lista_inventario[0] >= p_min and lista_inventario[0] <= p_max and lista_inventario[1] > 0:
            for cod_prod, lista_atributos in diccionario_productos.items():
                if cod_inv == cod_prod:
                    lista_resultados.append(f"{lista_atributos[0]} -- {cod_prod}")
                    break



    if len(lista_resultados) == 0:
        print("No se encotraron productos en ese rango de precios con stock disponible")
    else:
        lista_resultados.sort()
        print("Los productos encontrados son:")
        for item in lista_resultados:
            print(item)

def actualizar_precio(codigo, nuevo_preio, diccionario_inventario):
    if buscar_codigo(codigo, diccionario_inventario):
        diccionario_inventario[codigo.upper()][0] = nuevo_preio
        return True
    return False

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
                 }
    
inventario = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
             'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
             'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
             }

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        marca_ingresada = input("Ingrese la marca a consultar (HP, Lenovo, Asus, Dell)")
        stock_por_marca(marca_ingresada, productos, inventario)

    elif opcion == 2:
        while True:
            try:
                precio_minimo = int(input("Ingrese el precio minimo del rango: "))
                precio_maximo = int(input("Ingrese el precio maximo del rango"))

                if precio_minimo < 0 or precio_minimo > precio_maximo:
                    print("Error: el rango minimo debe ser mayor a 0 y menor al rango max")
                else:
                    busqueda_por_precio(precio_minimo, precio_maximo, productos, inventario)
                    break
            except ValueError:
                print("debes ingresar valores enteros validos")

    elif opcion == 3:
        while True:
            cod_buscar = input("Ingrese el codigo del producto a actualizar")
            while True:
                try:
                    precio_nuevo = int(input("Ingrese el nuevo precio del producto"))
                    if precio_nuevo <= 0:
                        print("debes ingresar un valor mayor a 0")
                    else: 
                        break
                except ValueError:
                    print("debe ser un numero entero positivo")

            if actualizar_precio(cod_buscar, precio_nuevo, inventario):
                print("Precio actualizado correctamente!")
            else:
                print("El codigo ingresado no existe en el sistema. ")

            otro = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower
            if otro != "s":
                break
    
    elif opcion == 4:
        print("programa finalizado")
        break