def validate_consumption(consumption):

    try:
        consumption = float(consumption)

        if consumption > 0:
            return True
        else:
            return False

    except ValueError:
        return False