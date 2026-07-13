from tarefas import *

while True:

    print("\n===== TASKFLOW =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Concluir tarefa")
    print("0 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        nome = input("Nome da tarefa: ")
        adicionar_tarefa(nome)

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        listar_tarefas()
        indice = int(input("Número da tarefa: ")) - 1
        novo = input("Novo nome: ")
        editar_tarefa(indice, novo)

    elif opcao == "4":
        listar_tarefas()
        indice = int(input("Número da tarefa: ")) - 1
        excluir_tarefa(indice)

    elif opcao == "5":
        listar_tarefas()
        indice = int(input("Número da tarefa: ")) - 1
        concluir_tarefa(indice)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")