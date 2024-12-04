def main():
    resposta = input("voce concorda? "). lower()

def concordo(resposta):
    if resposta == "sim" or resposta == "s":
        print("eu concordo")
    elif resposta == "n" or resposta == "n":
        print("eu nao concordo")



main()