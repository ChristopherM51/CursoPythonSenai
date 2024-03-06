import math

try:
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4 * a * c

    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    else:
        print("Não existem raízes reais.")

except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
except ZeroDivisionError:
    print("Erro: Divisão por zero.")
