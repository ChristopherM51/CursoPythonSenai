def palindromo(texto):
    texto = texto.lower().replace(" ","")
    return texto == texto[::-1]

frase_usuario = input("Digite uma frase ")
resultado_palindromo = palindromo(frase_usuario)
print(f"A frase é um palindromo: {resultado_palindromo}")