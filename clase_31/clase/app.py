# exceptions

def division(a,b):
    try:
        b = int(b)
        return a/b
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("No papá! no se divide por zero!")


print(division(1,"0."))
