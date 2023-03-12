def my_error(ch1="Name", num1=[1, 2]):
    if not isinstance(ch1, str):
        raise TypeError("ch1 must be a string")
    if type(num1) != list:
        raise TypeError("num1 must be a list")
    if len(num1) > 2:
        raise IndexError("num1 must be 2 items only")
    if num1[1] > 89:
        raise ValueError("value 2 in num1 must be less than 89")


print(my_error("231", [987, 998]))
