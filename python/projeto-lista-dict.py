def informações(doramas):
    doramas = [
        {"nome":"alquimia das alma", "temporadas":"2", "ano":"2022", "gênero":"fantasia", "diretor":"park joon hwa"},
        {"nome":"caçadores de demônios", "temporadas":"2", "ano":"2020", "gênero":"ação", "diretor":"yoo seon dong"},
        {"nome":"pretendente suspresa", "temporadas":"1", "ano":"2022", "gênero":"romance", "diretor":"park seon ho"},
        {"nome":"all of us are dead", "temperadas":"1", "ano":"2022", "gênero":"terror", "diretor":"lee jae kyoo"},
        {"nome":"hidden love", "temporadas":"1", "ano":"2023", "gênero":"romance", "diretor":"lee ching jung"},
        {"nome":"o rei de porcelana", "temporadas":"1", "ano":"2021", "gênero":"romance", "diretor":"song hyun wook"},
        {"nome":"my name", "temporadas":"1", "ano":"2021", "gênero":"ação", "diretor":"kim jin min"},
        {"nome":"my demon", "temporadas":"1", "ano":"2019", "gênero":"comédia romântica", "diretor":"hangul"},
        {"nome":"sorriso real", "temporadas":"1", "ano":"2023", "gênero":"romance", "diretor":"hyun wook im"},
        {"nome":"desgraça ao seu dispor", "temporadas":"1", "ano":"2021", "gênero":"romance", "diretor":"kwon young il"},
        ]
    
    def buscar_doramas(nome, doramas):
    for doramas in doramas:
        if dorama["nome"].lower() == nome.lower():
            return dorama
    return None

# Função principal
def main():
    while True:
        nome_dorama = input("Digite o nome do dorama: ")
        nome_dorama_encontrado = buscar_dorama(nome_dorama, doramas)
    
        if filme_encontrado:
            print(f"\nInformações do dorama:")
            print(f"Nome: {dorama_encontrado['nome']}")
            print(f"Ano: {dorama_encontrado['ano']}")
            print(f"Diretor: {dorama_encontrado['diretor']}")
            print(f"Nota: {dorama_encontrado['nota']}")
        else:
            print("Filme não encontrado.")

        continuar = input("Deseja pesquisar outro filme?(Sim/Não)").lower()
        if continuar =="não" or continuar =="nao":
            print("Encerrando o programa...")
            break
        
        else:
            continue



main()

