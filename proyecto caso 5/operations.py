def is_high_consumption(consumption):

    if consumption > 500:
        return True
    else:
        return False


def generate_recommendation(consumption):

    if consumption <= 100:
        return "Mantenga sus hábitos actuales de ahorro."

    elif consumption <= 300:
        return "Apague los equipos eléctricos que no estén en uso."

    elif consumption <= 500:
        return "Reduzca el uso de equipos de alto consumo."

    else:
        return "Se recomienda reducir el uso de equipos de alto consumo y revisar las instalaciones."


def display_summary(consumption, consumption_range, rate, cost, high_consumption, recommendation):

    print("\n========== RESUMEN DEL CONSUMO ==========")
    print(f"Consumo registrado: {consumption:.2f} kWh")
    print(f"Rango de consumo: {consumption_range}")
    print(f"Tarifa aplicada: C$ {rate:.2f} por kWh")
    print(f"Costo estimado: C$ {cost:.2f}")

    if high_consumption:
        print("Estado: CONSUMO ELEVADO")
    else:
        print("Estado: Consumo dentro del rango esperado")

    print(f"Recomendación: {recommendation}")
    print("==========================================")


def display_rates():

    print("\n========== RANGOS Y TARIFAS ==========")
    print("Rango          Consumo          Tarifa por kWh")
    print("-----------------------------------------------")
    print("Bajo           0 - 100 kWh      C$ 3.00")
    print("Medio          101 - 300 kWh    C$ 4.00")
    print("Alto           301 - 500 kWh    C$ 5.00")
    print("Muy alto       Más de 500 kWh   C$ 6.00")
    print("===============================================")


def display_recommendations():

    print("\n========== RECOMENDACIONES DE AHORRO ==========")
    print("1. Para consumos bajos:")
    print("   Mantenga sus hábitos actuales de ahorro.")

    print("\n2. Para consumos medios:")
    print("   Apague los equipos eléctricos que no estén en uso.")

    print("\n3. Para consumos altos:")
    print("   Reduzca el uso de equipos de alto consumo.")

    print("\n4. Para consumos muy altos:")
    print("   Reduzca el uso de equipos de alto consumo")
    print("   y revise las instalaciones eléctricas.")

    print("===============================================")