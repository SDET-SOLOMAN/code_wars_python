# The police have placed radars that will detect those vehicles that exceed the speed limit on that road.
# If the driver's speed is 10km/h to 19km/h above the speed limit, the fine will be 100 dollars,
# if it is exceeded by 20km/h to 29km/h the fine will be 250 dollars and if it is exceeded by more
# than 30km/h the fine will be 500 dollars.
#
# You will be provided with the speed limits of those roads with radar as a collection of speedlimits
# [90,100,110,120,....] and the speed of the driver will be the same on all roads and can never be negative
# and the amount of the fine will be accumulated example 95km/h.
#
# Example (Speed=100, Signals=[110,100,80]-> 250)

def speed_limit(speed, *speed_limits):
    fine = 0

    for signs in speed_limits:
        for limit in signs:
            excess_speed = speed - limit

            match excess_speed:
                case _ if 10 <= excess_speed <= 19:
                    fine += 100
                case _ if 20 <= excess_speed <= 29:
                    fine += 250
                case _ if excess_speed >= 30:
                    fine += 500

    return fine


def speed_limit2(speed, signals):
    m = 0
    for char in signals:
        if speed - char >= 30:
            m += 500
        elif speed - char >= 20:
            m += 250
        elif speed - char >= 10:
            m += 100
    return m


def cost(s, limit):
    total = limit - s
    match total:
        case total if total < 10:
            return 0
        case total if total < 20:
            return 100
        case total if total < 30:
            return 250
        case _:
            return 500
speed_limit3 = lambda speed, signals: sum(cost(x, speed) for x in signals)