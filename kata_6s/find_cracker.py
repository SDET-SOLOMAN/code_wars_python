def find_hack(arr):
    hacked = []

    temp = 0
    scores = {
        "A": 30,
        "B": 20,
        "C": 10,
        "D": 5
    }

    for student in arr:

        s = student[2]
        temp += 20 if all(x == "B" or x == "A" for x in s) and len(s) >= 5 else 0
        temp += sum(scores.get(x, 0) for x in s)
        temp = min(200, temp)

        if temp != student[1]:
            hacked.append(student[0])
        temp = 0

    return hacked