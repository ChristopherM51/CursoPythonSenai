dolares = float(input("DIgite o valor em dólares: "))
taxa_conversao = float(input("Digite a cotação do dia: "))

euros = dolares * taxa_conversao
libras = dolares * 0.75

print (f"Em euros: {euros: 2f}")
print (f"Em libras: {libras: 2f}")