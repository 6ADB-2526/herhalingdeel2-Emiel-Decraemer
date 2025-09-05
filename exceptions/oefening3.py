#IndexError
lijst = [10, 20, 30]

try:
    print(lijst[5])
except IndexError:
    print("deze array is niet zo lang")