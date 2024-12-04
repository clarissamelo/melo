def main():
    x = float(input("Escolha o primeiro número:"))
    y = float(input("Escolha o segundo número:"))
    verificacao(x,y)
def verificacao(x,y):
    if x > y:
        print(f"{x} é maior que {y}:")
    elif x < y:
        print(f"{x} é menor que {y}:")
    else:
        print(f"{x} é igual a {y}:")
main()