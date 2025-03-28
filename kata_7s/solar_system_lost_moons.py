# Oh no! The planets are jumbled up and they have lost their moons!
#
# TASK
# Given two lists, the planets and the moons, you have to return a two-dimensional list with the planets and'
# their respective moons.
#
# The dictionary with the planets' names (in the correct order) as the keys and their iconic moons' names
# as the values is given preloaded with the name planet_moons:
#
# {
#     'Mercury': [],
#     'Venus': [],
#     'Earth': ['Moon'],
#     'Mars': ['Deimos', 'Phobos'],
#     'Jupiter': ['Callisto', 'Europa', 'Ganymede', 'Io'],
#     'Saturn': ['Dione', 'Iapetus', 'Rhea', 'Tethys', 'Titan'],
#     'Uranus': ['Ariel', 'Miranda', 'Oberon', 'Titania', 'Umbriel'],
#     'Neptune': ['Nereid', 'Proteus', 'Triton']
# }
# The names of all the moons are sorted.
#
# Mercury and Venus have no moons at all.
#
# Thankfully, this time there are no "Asteroid"s, but you need to relocate the lost moons.
#
# The moons list will have random assorted moons. The planets list will have some (or all) planets, in any order.
#
# What you return should have a list for each planet with the moons you found for it. The planets should be ordered
# as per the order in the planet_moons dictionary, which is
# ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"].
#
# If a moon is present but its planet is not. Then the moon is simply not part of the Solar System you return.
#
# Start with putting the first moon (the first moon found after sorting) on the right of the planet
# and alternatively after that.
#
# EXAMPLE
# If the planets are ["Venus", "Neptune", "Jupiter", "Earth", "Mars"] and the moons are ["Proteus", "Rhea", "Io",
# "Moon", "Nereid", "Triton", "Phobos"], the Solar System you return should be:
#
# [["Venus"], ["Earth", "Moon"], ["Mars", "Phobos"], ["Jupiter", "Io"], ["Proteus", "Neptune", "Nereid", "Triton"]]
#
# # "Venus" is alone in its orbit
# # "Earth" has its (our) "Moon" given, so its found and put to the right
# # "Mars" finds "Phobos" and puts it to the right, but "Deimos", its other moon is not given, and remains lost
# # "Jupiter" only finds "Io" from its moons
# # "Neptune" first takes "Nereid", even though "Proteus" comes first in the list of moons, "Nereid" comes
# first after sorting.
# # Next it puts "Proteus" to the left, and finally "Triton" again to the right.
# # "Saturn" is not present in the list of planets, and so "Rhea" remains lost
# NOTES
# The planets list won't contain anything outside of the given planets and same applies for the moons list
# All the names in both the lists will be title-cased

d = {
    'Mercury': [],
    'Venus': [],
    'Earth': ['Moon'],
    'Mars': ['Deimos', 'Phobos'],
    'Jupiter': ['Callisto', 'Europa', 'Ganymede', 'Io'],
    'Saturn': ['Dione', 'Iapetus', 'Rhea', 'Tethys', 'Titan'],
    'Uranus': ['Ariel', 'Miranda', 'Oberon', 'Titania', 'Umbriel'],
    'Neptune': ['Nereid', 'Proteus', 'Triton']
}


def lost_moons(planets, moons):

    planets = set(planets)
    moons = set(moons)
    res = []

    for k, v in d.items():

        if not k in planets:
            continue

        temp = []

        for moon in v:
            if moon in moons:
                temp.append(moon)
        temp = temp[1::2][::-1] + [k] + temp[::2]
        res.append(temp)

    return res