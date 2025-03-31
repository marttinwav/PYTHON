contatos = []

def adicionar_contato():
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    email = input('Email: ')
    favorito = input('Marcar como favorito? (S/N): ').strip().lower() == 's'

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    contatos.append(contato)
    print(f'\nContato {nome} adicionado com sucesso!\n')

def listar_contatos():
    if not contatos:
        print("\nNenhum contato cadastrado.\n")
        return
    print("\nLista de Contatos:")
    for i, contato in enumerate(contatos, start=1):
        favorito = "⭐" if contato["favorito"] else ""
        print(f'{i}. {contato["nome"]} - {contato["telefone"]} - {contato["email"]} {favorito}')
    print()

def editar_contato():
    listar_contatos()
    nome = input('Nome do contato que deseja editar: ')
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            print("\nPressione Enter para manter o valor atual.")
            contato["nome"] = input(f'Novo nome ({contato["nome"]}): ') or contato["nome"]
            contato["telefone"] = input(f'Novo telefone ({contato["telefone"]}): ') or contato["telefone"]
            contato["email"] = input(f'Novo email ({contato["email"]}): ') or contato["email"]
            print(f'\nContato {nome} atualizado com sucesso!\n')
            return
    print("\nContato não encontrado.\n")

def alternar_favorito():
    listar_contatos()
    nome = input('Nome do contato para marcar/desmarcar como favorito: ')
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            contato["favorito"] = not contato["favorito"]
            status = "adicionado aos favoritos" if contato["favorito"] else "removido dos favoritos"
            print(f'\n{nome} agora está {status}.\n')
            return
    print("\nContato não encontrado.\n")

def listar_favoritos():
    favoritos = [contato for contato in contatos if contato["favorito"]]
    if not favoritos:
        print("\nNenhum contato favorito encontrado.\n")
        return
    print("\nContatos Favoritos:")
    for contato in favoritos:
        print(f'{contato["nome"]} - {contato["telefone"]} - {contato["email"]} ⭐')
    print()

def excluir_contato():
    listar_contatos()
    nome = input('Nome do contato que deseja excluir: ')
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            contatos.remove(contato)
            print(f'\n{nome} removido com sucesso!\n')
            return
    print("\nContato não encontrado.\n")

while True:
    try:
        opcao = int(input("Agenda de Contatos\n"
                          "[1] Adicionar contato\n"
                          "[2] Listar contatos\n"
                          "[3] Editar contato\n"
                          "[4] Marcar/Desmarcar favorito\n"
                          "[5] Listar favoritos\n"
                          "[6] Remover contato\n"
                          "[7] Sair\n"
                          "Escolha uma opção: "))

        if opcao == 1:
            adicionar_contato()
        elif opcao == 2:
            listar_contatos()
        elif opcao == 3:
            editar_contato()
        elif opcao == 4:
            alternar_favorito()
        elif opcao == 5:
            listar_favoritos()
        elif opcao == 6:
            excluir_contato()
        elif opcao == 7:
            print('\nObrigado por usar a agenda!\n')
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

    except ValueError:
        print("\nDigite um número válido.\n")