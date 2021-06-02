print("[INFO] Vyberte pocetni operaci:")
print("[INFO] 1 - Scitani   +")
print("[INFO] 2 - Odcitani  -")
print("[INFO] 3 - Nasobeni  *")
print("[INFO] 4 - Deleni    /")

while True:
    vyber = input("[INPUT] Zadejte pocetni operaci: ")
    if vyber in ('1', '2', '3', '4'):
        number1 = float(input("[INPUT] Zadejte prvni cislo: "))
        number2 = float(input("[INPUT] Zadejte druhe cislo: "))
        if vyber == '1':
            print(number1, " + ", number2, " = ", (number1+number2))
        elif vyber == '2':
            print(number1, " - ", number2, " = ", (number1-number2))
        elif vyber == '3':
            print(number1, " * ", number2, " = ", (number1*number2))
        elif vyber == '4':
            print(number1, " / ", number2, " = ", (number1/number2))
    else:
        print("[SHUTDOWN] Zadali jste nepovolene znaky, doslo k selhani aplikace.")
