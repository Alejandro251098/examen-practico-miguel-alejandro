
# ejercicio 3: funcion para numeros primos


def verificar_primos(numero):
    
    primo = True
    if numero > 1:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
                break

    if primo and numero > 1:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

verificar_primos(6)