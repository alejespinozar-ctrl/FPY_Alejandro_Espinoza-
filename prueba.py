def mostrar_menu():
    print("*** MENU PRINCIAL ***")
    print("1.Stock marca")
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







"""productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],"""

        