resposta = input("qual operação voce deseja realizar?")
if resposta =="soma":
    x = int (input("digite o primeiro numero:"))
    y = int (input("digite o segundo numero:"))
    resultadoSOM = x + y
    print(f"{x} + {y} = {resultadoSOM}")
elif resposta == "subtração":
    x = int (input("digite o primeiro numero:"))
    y = int (input("digite o segundo numero:"))
    resultadoSUB = x - y
    print(f"{x} - {y} = {resultadoSUB}")
elif resposta == "multiplicação":
    x = int (input("digite o primeiro numero:"))
    y = int (input("digite o segundo numero:"))
    resultadoMUL = x * y
    print(f"{x} * {y} = {resultadoMUL}")
elif resposta == "divisão":
    x = int (input("digite o primeiro numero:"))
    y = int (input("digite o segundo numero:"))
    resultadoDIV = x / y
    print(f"{x} / {y} = {resultadoDIV}")
    
    