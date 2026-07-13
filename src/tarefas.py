ARQUIVO = "tarefas.txt"


def adicionar_tarefa(nome):
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};Pendente\n")


def listar_tarefas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            tarefas = arquivo.readlines()

            if not tarefas:
                print("\nNenhuma tarefa cadastrada.")
                return

            print("\nLISTA DE TAREFAS")
            for i, tarefa in enumerate(tarefas, start=1):
                nome, status = tarefa.strip().split(";")
                print(f"{i} - {nome} [{status}]")

    except FileNotFoundError:
        print("\nNenhuma tarefa cadastrada.")


def editar_tarefa(indice, novo_nome):
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        tarefas = arquivo.readlines()

    nome, status = tarefas[indice].strip().split(";")
    tarefas[indice] = f"{novo_nome};{status}\n"

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(tarefas)


def excluir_tarefa(indice):
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        tarefas = arquivo.readlines()

    tarefas.pop(indice)

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(tarefas)


def concluir_tarefa(indice):
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        tarefas = arquivo.readlines()

    nome, status = tarefas[indice].strip().split(";")
    tarefas[indice] = f"{nome};Concluída\n"

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(tarefas)