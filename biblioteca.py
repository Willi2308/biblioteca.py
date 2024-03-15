from livro import Livro

def adicionar_livro(biblioteca, titulo, autor, ano_publicacao):
    livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(livro)

def emprestar_livro(biblioteca, titulo):
    for livro in biblioteca:
        if livro.titulo == titulo and livro.disponibilidade():
            livro.alterar_status("emprestado")
            print("Livro emprestado com sucesso.")
            return
    print("Livro não encontrado ou indisponível.")

def devolver_livro(biblioteca, titulo):
    for livro in biblioteca:
        if livro.titulo == titulo and not livro.disponibilidade():
            livro.alterar_status("disponível")
            print("Livro devolvido com sucesso.")
            return
    print("Livro não encontrado ou disponível.")

def exibir_livros_disponiveis(biblioteca):
    print("Livros disponíveis:")
    for livro in biblioteca:
        if livro.disponibilidade():
            print(f"{livro.titulo} - {livro.autor} - {livro.ano_publicacao}")