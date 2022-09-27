def count_photos(road):
    photos = 0
    left = 0
    dot_founds = 0
    for item in road:
        if item == ">":
            left += 1
        elif item == ".":
            photos += left
            dot_founds += 1
        elif item == "<":
            photos += dot_founds

    return photos