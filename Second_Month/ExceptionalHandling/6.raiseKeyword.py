try:
    data = int(input("Pleaae enter a number: "))
    if data == 10:
        raise ZeroDivisionError
    else:
        raise TypeError
except ZeroDivisionError:
    print("From ZeroDivision Error")
except TypeError:
    print("This is a Type Error")