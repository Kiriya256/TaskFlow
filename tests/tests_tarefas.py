import sys
import os

sys.path.append(os.path.abspath("src"))

from tarefas import adicionar_tarefa

def test_adicionar_tarefa():
    assert adicionar_tarefa("Teste") is None