# ZeroDivisionError
def deel(a, b):
    try:
        resultaat = (a/b)
    except ZeroDivisionError:
        resultaat = ("je kan niet delen door nul")
    
    print(f"Resultaat: {resultaat}")

deel(10, 0)