def adicionar_tarefa(tarefas, nome_tarefa):
    tarefas.append({"tarefas": nome_tarefa, "Finalizada": True})
    print(f"Tarefa {nome_tarefa} adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\n Lista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["Finalizada"] else " "
        nome_tarefa = tarefa["tarefas"]
        print(f"{indice}. {nome_tarefa} {status}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefas"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice de tarefa inválido.")
        return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado]["Finalizada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["Finalizada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas.")
    return

tarefas = []
while True:
    print("\nMenu gerenciador de tarefas")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar tarefa")
    print("4. Marcar tarefa como concluída")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    
    escolha = input("Escolha uma opção: ")


    if escolha =="1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o numero da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
       ver_tarefas(tarefas)
       indice_tarefa = input("Digite o numero da tarefa que deseja completar: ")
       completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break

print("Programa Finalizado")
