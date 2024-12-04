def main():
    nome = input("qual seu nome?")
    diga_ola(nome)

    def diga_ola(para="mundo"):
        print(f"ola, {para}!")
    main()