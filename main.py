# main.py

"""
Sistema Bancário - Versão 2.0 (Otimizado com Funções)

Este é o arquivo principal do sistema bancário. Ele gerencia o menu,
o estado global do sistema (saldo, extrato, usuários, contas) e
chama as funções de operações bancárias importadas do módulo de serviços.

Autor: [Seu Nome/Nome da Equipe]
"""

# Importa todas as funções e constantes do módulo de serviços
from src.services.operacoes_bancarias import (
    depositar, 
    sacar, 
    exibir_extrato, 
    criar_usuario, 
    criar_conta, 
    listar_contas,
    AGENCIA
)

def menu():
    """
    Exibe o menu de opções e solicita a entrada do usuário.
    """
    menu_str = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
=> """
    return input(menu_str)

# --- Variáveis de Estado Global ---
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = [] # Lista para armazenar dicionários de usuários
contas = [] # Lista para armazenar dicionários de contas
numero_conta = 1 # Contador sequencial para o número da conta

# --- Loop Principal do Sistema ---
while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        # Chamada da função com Argumentos Posicionais
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Chamada da função com Argumentos Nomeados (Keyword Only)
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "e":
        # Chamada da função com Argumento Posicional (saldo) e Nomeado (extrato)
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        # Chamada da função para criar um novo usuário
        usuarios = criar_usuario(usuarios)

    elif opcao == "nc":
        # Chamada da função para criar uma nova conta
        nova_conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
        if nova_conta:
            contas.append(nova_conta)
            # Incrementa o número da conta somente se a criação for bem-sucedida
            numero_conta += 1

    elif opcao == "lc":
        # Chamada da função para listar as contas
        listar_contas(contas)

    elif opcao == "q":
        print("\nObrigado por usar nosso sistema bancário. Volte sempre!")
        break

    else:
        print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

