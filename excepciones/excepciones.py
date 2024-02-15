def sumar_dos():
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado = int(a) + int(b)
        except Exception as e:
            print(f"ERROR: {e}")
            print("Pone un numero imbecil")
        else:
            break
    return f"Resultado: {resultado}"


print(sumar_dos())