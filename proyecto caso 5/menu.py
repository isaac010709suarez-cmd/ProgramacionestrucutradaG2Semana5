def display_menu():

    print("\n==========================================")
    print("      ESTIMADOR DE CONSUMO ELÉCTRICO")
    print("==========================================")
    print("1. Registrar consumo")
    print("2. Calcular costo")
    print("3. Consultar rango y tarifa")
    print("4. Ver recomendación de ahorro")
    print("5. Mostrar resumen")
    print("6. Salir")
    print("==========================================")

    option = input("Seleccione una opción: ")

    return option


def pause_program():

    input("\nPresione ENTER para continuar...")