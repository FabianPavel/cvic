def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Dělení nulou."
    return x / y

while True:
    print("Options:")
    print("Napište 'soucet' pro sčítání")
    print("Napište 'odecet' pro odečtení")
    print("Napište 'nasob' pro násobení")
    print("Napište 'del' pro delení")
    print("Napište 'konec' pro ukončení")

    user_input = input(": ")

    if user_input == "konec":
        break

    if user_input in ("soucet", "odecet", "nasob", "del"):
        num1 = float(input("Zadejte první číslo: "))
        num2 = float(input("Zadejte druhé číslo: "))

        if user_input == "soucet":
            print("Výsledek:", add(num1, num2))
        elif user_input == "odecet":
            print("Výsledek:", subtract(num1, num2))
        elif user_input == "nasob":
            print("Výsledek:", multiply(num1, num2))
        elif user_input == "del":
            print("Výsledek:", divide(num1, num2))
    else:
        print("Neplatná možnost. Prosím zadejte platnou možnost.")
