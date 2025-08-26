#crie uma lista com cadastro de usuario 
#cadastrar
#alterar                                    > usar (função, lista, try/except, laços)
#excluir
#listar 

usuarios = []

def menu():
    print("\n--- MENU ---")
    print("1 - Cadastrar usuário")
    print("2 - Alterar usuário")
    print("3 - Excluir usuário")
    print("4 - Listar usuários")
    print("5 - Sair")

def cadastrar_usuario():
    try:
        nome = input("Digite o nome: ")
        email = input("Digite o e-mail: ")
        idade = int(input("Digite a idade: "))
        usuario = {"nome": nome, "email": email, "idade": idade}
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
    except ValueError:
        print("Erro: idade deve ser um número inteiro.")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\n--- Lista de Usuários ---")
    for idx, usuario in enumerate(usuarios):
        print(f"{idx} - Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")

def alterar_usuario():
    listar_usuarios()
    try:
        indice = int(input("Digite o índice do usuário que deseja alterar: "))
        if 0 <= indice < len(usuarios):
            nome = input("Novo nom
