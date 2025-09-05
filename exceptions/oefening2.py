#TypeError
def tel_op(a, b):
    try:
        return a + b
    except TypeError:
        return "je hebt 2 nummers nodig om op te tellen"

print(tel_op(5, "drie"))