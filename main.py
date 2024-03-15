from biblioteca import adicionar_livro, emprestar_livro, devolver_livro, exibir_livros_disponiveis

def main():
    biblioteca = []

    while True:
        print("\nMenu de opções:")
        print("1. Adicionar livro")
        print("2. Emprestar livro")
        print("3. Devolver livro")
        print("4. Exibir livros disponíveis")
        print("5. Sair do programa")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            ano_publicacao = int(input("Digite o ano de publicação: "))
            adicionar_livro(biblioteca, titulo, autor, ano_publicacao)
        elif opcao == 2:
            titulo = input("Digite o título do livro que deseja emprestar: ")
            emprestar_livro(biblioteca, titulo)
        elif opcao == 3:
            titulo = input("Digite o título do livro que deseja devolver: ")
            devolver_livro(biblioteca, titulo)
        elif opcao == 4:
            exibir_livros_disponiveis(biblioteca)
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()