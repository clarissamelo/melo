while True:
    try:
        entrada = input("digite a espressão aritimétoca(número operador número):")
        resultado = eval(entrada)
        print(resultado)
    except Exception as e:
        print("não foi possível achar. certifique-se que usou os símbolos certos.")