from menu import display_menu, pause_program
from validations import validate_consumption
from calculations import determine_range, get_rate, calculate_cost
from operations import (
    is_high_consumption,
    generate_recommendation,
    display_summary,
    display_rates,
    display_recommendations
)


def main():

    consumption = 0
    consumption_registered = False

    while True:

        try:

            option = display_menu()

            if option == "1":

                input_value = input("\nIngrese el consumo mensual en kWh: ")

                if validate_consumption(input_value):

                    consumption = float(input_value)
                    consumption_registered = True

                    print("\nConsumo registrado correctamente.")
                    print(f"Consumo: {consumption:.2f} kWh")

                else:

                    print("\nError: debe ingresar un valor numérico positivo.")

                pause_program()

            elif option == "2":

                if consumption_registered:

                    rate = get_rate(consumption)
                    cost = calculate_cost(consumption, rate)

                    print("\n========== CÁLCULO DEL COSTO ==========")
                    print(f"Consumo: {consumption:.2f} kWh")
                    print(f"Tarifa: C$ {rate:.2f} por kWh")
                    print(f"Costo estimado: C$ {cost:.2f}")
                    print("=======================================")

                else:

                    print("\nPrimero debe registrar un consumo.")

                pause_program()

            elif option == "3":

                display_rates()
                pause_program()

            elif option == "4":

                display_recommendations()
                pause_program()

            elif option == "5":

                if consumption_registered:

                    consumption_range = determine_range(consumption)
                    rate = get_rate(consumption)
                    cost = calculate_cost(consumption, rate)
                    high_consumption = is_high_consumption(consumption)
                    recommendation = generate_recommendation(consumption)

                    display_summary(
                        consumption,
                        consumption_range,
                        rate,
                        cost,
                        high_consumption,
                        recommendation
                    )

                else:

                    print("\nPrimero debe registrar un consumo.")

                pause_program()

            elif option == "6":

                print("\nGracias por utilizar el estimador de consumo eléctrico.")
                break

            else:

                print("\nError: opción no válida. Seleccione una opción del 1 al 6.")
                pause_program()

        except Exception as error:

            print(f"\nSe produjo un error: {error}")
            pause_program()

        finally:
            pass


if __name__ == "__main__":
    main()