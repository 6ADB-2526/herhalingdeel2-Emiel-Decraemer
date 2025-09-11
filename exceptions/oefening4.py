persoon = {"naam": "Ali", "leeftijd": 30}

try:
    print(persoon["adres"])
except KeyError:
    print("deze variabele bestaat niet")