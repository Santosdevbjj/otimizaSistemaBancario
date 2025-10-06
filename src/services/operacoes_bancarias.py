# src/services/operacoes_bancarias.py

"""
Módulo de Funções de Operações Bancárias

Contém as funções centrais para o sistema bancário, 
incluindo depósito, saque, extrato, e o cadastro de 
usuários e contas.
"""

# Constante para a agência
AGENCIA = "0001"

def depositar(saldo, valor, extrato, /):
    """
    Realiza a operação de depósito.
    
    Argumentos:
        saldo (float): O saldo atual da conta (Posicional Only).
        valor (float): O valor a ser depositado (Posicional Only).
        extrato (str): O histórico de transações (Posicional Only).
        
    Retorna:
        tuple: (saldo atualizado, extrato atualizado).
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque.
    
    Argumentos:
        saldo (float): Saldo atual (Keyword Only).
        valor (float): Valor do saque (Keyword Only).
        extrato (str): Histórico de transações (Keyword Only).
        limite (float): Limite máximo por saque (Keyword Only).
        numero_saques (int): Quantidade de saques realizados (Keyword Only).
        limite_saques (int): Limite máximo de saques diários (Keyword Only).
        
    Retorna:
        tuple: (saldo atualizado, extrato atualizado, numero_saques atualizado).
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato bancário.
    
    Argumentos:
        saldo (float): Saldo atual (Posicional Only).
        extrato (str): Histórico de transações (Keyword Only).
    
    Retorna:
        None
    """
    print("\n================ EXTRATO ================")
    # O f-string é mais legível aqui para o caso de extrato vazio
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    """
    Cadastra um novo usuário (cliente) no sistema.
    
    O CPF é a chave única.
    
    Argumentos:
        usuarios (list): Lista de usuários cadastrados.
        
    Retorna:
        list: Lista de usuários atualizada.
    """
    cpf = input("Informe o CPF (somente números): ")
    # Verifica se já existe usuário com o CPF
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com este CPF! @@@")
        return usuarios

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    
    # Formato do endereço: logradouro, número, bairro, cidade/sigla estado
    logradouro = input("Informe o logradouro (Rua/Av): ")
    numero = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade_estado = input("Informe a cidade/sigla estado (Ex: São Paulo/SP): ")
    
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade_estado}"

    # Adiciona o novo usuário na lista
    usuarios.append({
        "nome": nome, 
        "data_nascimento": data_nascimento, 
        "cpf": cpf, 
        "endereco": endereco
    })
    
    print("\n=== Usuário criado com sucesso! ===")
    
    return usuarios


def filtrar_usuario(cpf, usuarios):
    """
    Busca um usuário na lista de usuários pelo CPF.
    
    Argumentos:
        cpf (str): CPF a ser buscado.
        usuarios (list): Lista de usuários.
        
    Retorna:
        dict: O objeto usuário encontrado, ou None se não encontrar.
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    # Retorna o primeiro (e único) elemento ou None
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    """
    Cria uma nova conta corrente e a vincula a um usuário existente.
    
    Argumentos:
        agencia (str): O número fixo da agência (0001).
        numero_conta (int): O número sequencial da nova conta.
        usuarios (list): A lista de usuários cadastrados.
        
    Retorna:
        dict: O objeto da nova conta criada, ou None em caso de falha.
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        # Vincula a conta ao usuário encontrado (objeto)
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia": agencia, 
            "numero_conta": numero_conta, 
            "usuario": usuario # Armazena a referência do objeto usuário
        }
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None


def listar_contas(contas):
    """
    Exibe todas as contas correntes cadastradas.
    
    Argumentos:
        contas (list): Lista de contas correntes.
        
    Retorna:
        None
    """
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    print("\n========== LISTA DE CONTAS ==========")
    for conta in contas:
        # Formata a string de forma clara para exibição
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("-" * 40)
        print(linha)
    print("=====================================")

