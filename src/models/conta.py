# src/models/conta.py

"""
Módulo Conta

Define as classes Conta e ContaCorrente, que representam as contas bancárias.
"""

class Conta:
    """
    Representa uma conta bancária genérica.
    
    Atributos de Classe:
        numero_sequencial (int): Próximo número de conta a ser atribuído.
        
    Atributos de Instância:
        _saldo (float): Saldo atual da conta (privado).
        _numero (int): Número da conta.
        _agencia (str): Número da agência (fixo em "0001" neste projeto).
        _cliente (Cliente): Objeto Cliente proprietário da conta.
        _historico (Historico): Objeto para registrar as transações.
    """
    # Atributo estático/de classe
    AGENCIA = "0001"

    def __init__(self, cliente, numero):
        """
        Inicializa uma nova Conta.
        
        Args:
            cliente (Cliente): O objeto Cliente vinculado à conta.
            numero (int): O número sequencial da conta.
        """
        self._saldo = 0
        self._numero = numero
        self._agencia = Conta.AGENCIA
        self._cliente = cliente
        # Por simplicidade, usaremos uma lista como histórico por enquanto
        self._historico = [] 
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        """
        Método de classe para criar uma nova conta.
        
        Args:
            cliente (Cliente): Objeto cliente.
            numero (int): Número da conta.
            
        Retorna:
            Conta: Uma nova instância da classe Conta.
        """
        return cls(cliente, numero)

    @property
    def saldo(self):
        """Getter para o saldo."""
        return self._saldo

    @property
    def numero(self):
        """Getter para o número da conta."""
        return self._numero

    @property
    def agencia(self):
        """Getter para a agência."""
        return self._agencia

    @property
    def cliente(self):
        """Getter para o objeto cliente."""
        return self._cliente
    
    @property
    def historico(self):
        """Getter para o histórico."""
        return self._historico
    
    def sacar(self, valor):
        """
        Realiza a operação de saque na conta.
        
        Args:
            valor (float): O valor a ser sacado.
            
        Retorna:
            bool: True se o saque for bem-sucedido, False caso contrário.
        """
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            return False

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False

    def depositar(self, valor):
        """
        Realiza a operação de depósito na conta.
        
        Args:
            valor (float): O valor a ser depositado.
            
        Retorna:
            bool: True se o depósito for bem-sucedido, False caso contrário.
        """
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False


class ContaCorrente(Conta):
    """
    Representa uma conta corrente, herda de Conta.
    
    Adiciona a funcionalidade de limite e limite de saques diários.
    
    Atributos específicos:
        _limite (float): Limite de cheque especial/saque por operação.
        _limite_saques (int): Número máximo de saques permitidos por dia.
    """
    LIMITE_SAQUES = 3 # Limite de saques diários (constante de classe)
    
    def __init__(self, cliente, numero, limite=500):
        """
        Inicializa uma nova Conta Corrente.
        
        Args:
            cliente (Cliente): O objeto Cliente vinculado.
            numero (int): O número sequencial da conta.
            limite (float): O limite máximo por saque.
        """
        super().__init__(cliente, numero)
        self._limite = limite
        self._numero_saques = 0

    def sacar(self, valor):
        """
        Sobrescreve o método sacar para adicionar as regras de limite e saques.
        
        Args:
            valor (float): O valor a ser sacado.
            
        Retorna:
            bool: True se o saque for bem-sucedido, False caso contrário.
        """
        excedeu_limite = valor > self._limite
        excedeu_saques = self._numero_saques >= self.LIMITE_SAQUES

        if excedeu_limite:
            print(f"\n@@@ Operação falhou! O valor excede o limite de R$ {self._limite:.2f}. @@@")
        
        elif excedeu_saques:
            print(f"\n@@@ Operação falhou! Máximo de {self.LIMITE_SAQUES} saques diários excedido. @@@")
        
        # Chama a implementação da classe pai (Conta) se passar nas regras específicas
        else:
            if super().sacar(valor): # Se o saque na Conta (pai) foi bem-sucedido
                self._numero_saques += 1
                return True
        
        return False
    
    def __repr__(self):
        """Representação formal do objeto para debug/log."""
        return f"<ContaCorrente(agencia='{self.agencia}', numero={self.numero}, cliente='{self.cliente.nome}')>"
