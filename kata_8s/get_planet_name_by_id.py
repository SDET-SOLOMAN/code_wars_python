# The function is not returning the correct values. Can you figure out why?
#
# Example (Input --> Output ):
#
# 3 --> "Earth"

def get_planet_name(id):
    # This doesn't work; Fix it!
    name = ""
    match id:
        case 1:
            name = "Mercury"
        case 2:
            name = "Venus"
        case 3:
            name = "Earth"
        case 4:
            name = "Mars"
        case 5:
            name = "Jupiter"
        case 6:
            name = "Saturn"
        case 7:
            name = "Uranus"
        case 8:
            name = "Neptune"
    return name


def get_planet_name2(id):
    return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]