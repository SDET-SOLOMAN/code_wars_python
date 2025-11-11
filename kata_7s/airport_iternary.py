# Travel itinerary

# When you travel around the world you pass though different airports.

# TRN -> FCO -> JFK
# And then return back to home

# JFK - TRN
# In order to propose the unique list of airports that your trip uses we have to create an itinerary feature that can compress the list of airports including only the list of unique in/out combination.

# For example, a trip with:

# [TRN-FCO] [FCO-JFK] [JFK-TRN]
# Should be represented as:

# TRN-FCO-JFK-TRN
# That is the unique list of airport steps.

# Now in our database we save the travel as a list of objects with in/out properties and you will receive that list always sorted in the right way.

# [
#   {'in': "TRN", 'out': "FCO"},
#   {'in': "FCO", 'out': "JFK"},
#   {'in': "JFK", 'out': "FCO"}
# ]
# Now we have to create a helper function itinerary for JS that extract the unique airport list:

# travel = itinerary([
#   {'in': "TRN", 'out': "FCO"},
#   {'in': "FCO", 'out': "JFK"},
#   {'in': "JFK", 'out': "FCO"}
# ]); # TRN-FCO-JFK-FCO

def itinerary(t: list[dict[str, str]]) -> str:
    
    res: list[str] = []
    
    for flight in t:
        if not res or flight["in"] != res[-1]:
            res.append(flight["in"])
        if flight["out"] != res[-1]:
            res.append(flight["out"])
    
    return "-".join(res)

# Alternative solution:
# def itinerary(t: list[dict[str, str]]) -> str:
#     airports = []
#     for flight in t:
#         if not airports or flight['in'] != airports[-1]:
#             airports.append(flight['in'])
#         if flight['out'] != airports[-1]:
#             airports.append(flight['out'])
#     return '-'.join(airports)