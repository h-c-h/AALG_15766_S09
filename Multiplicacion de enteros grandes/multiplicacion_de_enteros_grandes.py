def pedir_entero_grande(prompt):
    while True:
        entrada = input(prompt)
        if entrada.isdigit():
            return entrada
        else:
            print("Error: Dato ingresado no valido, Intente de nuevo: ")


def karatsuba(x: str, y: str) -> int:
    if len(x) == 1 or len(y) == 1:
        return int(x) * int(y)

    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    n = max_len
    m = n // 2

    x1, x0 = x[:-m], x[-m:]
    y1, y0 = y[:-m], y[-m:]

    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(str(int(x1) + int(x0)), str(int(y1) + int(y0))) - z2 - z0

    resul = (z2 * 10**(2 * m)) + (z1 * 10**m) + z0
    return resul


num1 = pedir_entero_grande("Ingrese el primer numero entero grande: ")
num2 = pedir_entero_grande("Ingrese el segundo numero entero grande: ")

resul = karatsuba(num1, num2)

print("\nResultado de la multiplicacion:")
print(resul)