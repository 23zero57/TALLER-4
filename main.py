def mostrar_tablas_1_10():
    """esta funcion muestra de manera organizada las tablas del 1 al 10 que es generalmente lo basico"""
    print("\n" + "=" * 40)
    print("         TABLAS DE MULTIPLICAR DEL 1 AL 1O       ")
    print("=" * 40)
    for i in range (1, 11):
        print(f"\n--- Tabla del {i} ---")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
    print("\n" + "=" * 40)
def crear_tabla_personalizada(lista_especial):
    """esta funcion crea una nueva tabla de multiplicar con limites personalizados y la agrega a una"lista especial"""
    print("\n" + "=" * 40)
    print("         CREAR NUEVA TABLA DE MULTIPLICAR       ")
    print("=" * 40)
    try:
        numero = int(input("ingresa el numero a multiplicar en la tabla: "))

        print("\nSelecciona el limite de la tabla:")
        print("1. Del 1 al 10")
        print("1. Del 1 al 20")
        print("1. Del 1 al 30")
        opcion_limite = input("Elige  una opcion (1-3): ")

        if opcion_limite == '1' :
            limite = 10
        if opcion_limite == '2' :
            limite = 20  
        if opcion_limite == '3' :
            limite = 30 
        else:
            print("Opcion no valida. Se asignara por defecto hasta el 10. ")

        #Generar la tabla usando un bucle for
        elementos_tabla = []
        print(f"\nGenerando tabla del {numero} (del 1 al {limite}):")
        print("-" * 30)
        for j in range(1, limite + 1):
            resultado = numero * j
            elementos_tabla.append((j, resultado))
            print(f"{numero} x {j} = {resultado}")

        # Guardar automaticamente en la lista especial como un diccionario
        tabla_info = {
            "numero": numero,
            "limite": limite,
            "datos" : elementos_tabla
        }
        lista_especial.append(tabla_info)
        print(f"\nExito, la tabla del {numero} con limite de {limite} se ha guardado en la lista")

    except ValueError:
        print("Error: por favor ingresa un valor numerico entero valido")
    
    def mostrar_lista_especial(lista_especial):
        """Muestra todas las tablas almacenadas previamente en la lista especial"""
        print("\n" + "=" * 40)
        print(" LISTA ESPECIAL DE TABLAS ")
        print("=" * 40)

        if not lista_especial:
            print("La lista especial está vacía. Crea una tabla en la opción 2 primero.")
            return

        for idx, tabla in enumerate(lista_especial, 1):
            num = tabla["numero"]
            limite = tabla["limite"]
            print(f"\n{idx}. Tabla del {num} (Rango: 1 al {limite})")
            print("-" * 30)
            for multiplicador, resultado in tabla["datos"]:
                print(f"{num} x {multiplicador} = {resultado}")
        print("\n" + "=" * 40)

    def main():
        # Estructura de datos principal para almacenar las tablas personalizadas
        lista_especial = []

        while True:
            print("\n*** MENÚ PRINCIPAL - TABLAS DE MULTIPLICAR ***")
            print("1. Mostrar las tablas del 1 al 10")
            print("2. Crear nueva tabla de multiplicar (Rango 10, 20 o 30) y guardar")
            print("3. Mostrar la lista especial")
            print("4. Salir")

            opcion = input("\nSelecciona una opción (1-4): ")

            if opcion == '1':
                mostrar_tablas_1_10()
            elif opcion == '2':
                crear_tabla_personalizada(lista_especial)
            elif opcion == '3':
                mostrar_lista_especial(lista_especial)
            elif opcion == '4':
                print("\n¡Saliendo del programa. Éxitos con la presentación!")
                break
            else:
                print("\nOpción inválida. Por favor, selecciona un número entre 1 y 4.")


    if __name__ =="__main__":
        main()