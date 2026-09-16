def determine_range(consumption):

    if consumption <= 100:
        return "Bajo"
    elif consumption <= 300:
        return "Medio"
    elif consumption <= 500:
        return "Alto"
    else:
        return "Muy alto"


def get_rate(consumption):

    if consumption <= 100:
        return 3.00
    elif consumption <= 300:
        return 4.00
    elif consumption <= 500:
        return 5.00
    else:
        return 6.00


def calculate_cost(consumption, rate):

    cost = consumption * rate

    return cost