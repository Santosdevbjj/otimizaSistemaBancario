# src/models/cliente.py

"""
Módulo Cliente

Define a classe Cliente, que representa o usuário do banco.
"""

class Cliente:
    """
    Representa um cliente do banco.

    Atributos:
        _endereco (str): Endereço formatado do cliente (privado).
        contas (list): Lista de objetos Conta associados a este cliente.
    """
    def __init__(self, endereco):
        """
        Inicializa um novo Cliente.
        
        Args:
            endereco (str): Endereço no formato: logradouro, número, bairro, cidade/sigla estado.
        """
        self._endereco = endereco
        self.contas = [] # Lista para armazenar objetos de conta

    @property
    def endereco(self):
        """Getter para o endereço."""
        return self._endereco

    def realizar_transacao(self, conta, transacao):
        """
        Método abstrato que seria implementado em classes filhas (ex: PessoaFisica/Juridica).
        Por agora, apenas chama o método de transação da conta.
        
        Args:
            conta (Conta): Objeto da conta onde a transação será realizada.
            transacao (Transacao): Objeto da transação (ex: Saque, Deposito).
        """
        # A transação (Saque/Deposito) é quem tem a lógica de execução
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """
        Adiciona uma conta à lista de contas do cliente.
        
        Args:
            conta (Conta): Objeto da conta a ser adicionada.
        """
        self.contas.append(conta)
        print(f"\nConta {conta.numero} adicionada ao cliente com sucesso.")


class PessoaFisica(Cliente):
    """
    Representa um cliente pessoa física, herda de Cliente.

    Atributos específicos:
        _cpf (str): O número do CPF (somente números, privado).
        nome (str): Nome completo do cliente.
        data_nascimento (str): Data de nascimento (dd-mm-aaaa).
    """
    def __init__(self, nome, data_nascimento, cpf, endereco):
        """
        Inicializa uma nova Pessoa Física.
        
        Args:
            nome (str): Nome completo.
            data_nascimento (str): Data de nascimento.
            cpf (str): CPF (somente números).
            endereco (str): Endereço formatado.
        """
        # Chama o construtor da classe base (Cliente)
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def cpf(self):
        """Getter para o CPF."""
        return self._cpf

    def __repr__(self):
        """Representação formal do objeto para debug/log."""
        return f"<PessoaFisica(nome='{self.nome}', cpf='{self.cpf}')>"
