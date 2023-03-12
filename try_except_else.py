def return_day(num):
    my_dict = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    try:
        return my_dict[num]
    except (KeyError, ValueError, ZeroDivisionError) as err:# or can be left empty:
        print(err)
        return f"This item is not here {err}"


# try

# except

# else

# finally - run no matter what


print(return_day(93))
