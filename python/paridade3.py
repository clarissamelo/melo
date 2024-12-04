def main ():
    num = int(input("digite um número:"))
    if eh_par(num):
        print("é par")
    else:
        print("é impar")

def eh_par(num):
    if num % 2 ==0:
        return True
    else:
        return False
main()