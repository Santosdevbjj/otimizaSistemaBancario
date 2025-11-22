## Otimizando o Sistema Bancário com Funções Python.

![PythonDeveloper001](https://github.com/user-attachments/assets/47f8e7eb-1ede-4051-8894-100171801849)



**Bootcamp Suzano - Python Developer #2**

---



# 🏦 Otimização do Sistema Bancário com Funções e POO em Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
![Status](https://img.shields.io/badge/Status-Ativo-success?style=flat)
![License](https://img.shields.io/badge/Licença-MIT-green)
![Paradigmas](https://img.shields.io/badge/Paradigmas-Funcional%20%2B%20POO-orange)
[![GitHub last commit](https://img.shields.io/github/last-commit/Santosdevbjj/otimizaSistemaBancario)](https://github.com/Santosdevbjj/otimizaSistemaBancario/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Santosdevbjj/otimizaSistemaBancario)](https://github.com/Santosdevbjj/otimizaSistemaBancario)

---

## 📌 Sobre o Projeto

Este projeto representa a **evolução de um sistema bancário simples** desenvolvido em Python.  
O objetivo principal foi **refatorar o código inicial**, aplicando:

- ✅ **Modularização**
- ✅ **Funções dedicadas com regras estritas de argumentos**
- ✅ **Programação Orientada a Objetos (POO)** para modelar entidades centrais: `Cliente` e `Conta`

> O resultado é um sistema mais organizado, extensível e próximo de um design profissional de aplicações reais.

---

## 🎯 Objetivos Centrais

- 🧱 **Modularização** → Separar a lógica de negócios da lógica de controle (menu principal).  
- 🧠 **Funções específicas** → Depósito, Saque, Extrato, Cadastro de Usuário e Conta.  
- 👤 **Modelagem POO** → Classes para `Cliente`, `PessoaFisica`, `Conta` e `ContaCorrente`.  
- 📝 **Argumentos Posicionais e Nomeados** → Aplicação de boas práticas no design de funções.

---

## 🏗️ Estrutura do Repositório 

<img width="902" height="806" alt="Screenshot_20251006-155906" src="https://github.com/user-attachments/assets/07992823-7175-4cca-ab13-f65d71bf9f75" /> 


---


## 📂 Detalhamento dos Arquivos e Módulos

### 1. **`main.py`**
- Ponto de entrada da aplicação.
- Controla o **loop principal** e apresenta o menu interativo.
- Gerencia o estado global (`saldo`, `extrato`, `usuarios`, `contas`).
- Encaminha as ações para as funções de serviço.

---

### 2. **`src/services/operacoes_bancarias.py`**
Contém a lógica de negócios do sistema, com funções desenhadas para garantir **clareza e manutenção futura**:

| Função            | Tipo de Argumentos  | Propósito                                                                 |
|-------------------|---------------------|---------------------------------------------------------------------------|
| `depositar()`     | Posicional Only `/` | Realiza o depósito e atualiza saldo/extrato.                              |
| `sacar()`         | Keyword Only `*`    | Realiza o saque com regras de limite e número de saques.                  |
| `exibir_extrato()`| Posicional + Keyword| Exibe saldo e histórico de transações.                                   |
| `criar_usuario()` | Padrão             | Cadastra novo cliente (CPF único).                                        |
| `criar_conta()`   | Padrão             | Cria nova conta e vincula a um cliente existente.                         |
| `listar_contas()` | Padrão             | Exibe todas as contas cadastradas.                                       |

---

### 3. **`src/models/cliente.py`**
Define a estrutura dos clientes:

- `class Cliente`: Base para qualquer tipo de cliente.
- `class PessoaFisica(Cliente)`: Herda e adiciona atributos como nome, data de nascimento e CPF (privado).  
- Uso de **`@property`** para encapsular acesso seguro aos atributos.

---

### 4. **`src/models/conta.py`**
Modela as contas bancárias:

- `class Conta`: Responsável pela lógica básica de `sacar()` e `depositar()`.
- `class ContaCorrente(Conta)`: Sobrescreve `sacar()` com **limites diários e por operação**.

---

### 5. **`.gitignore`**
Ignora:
- Pastas `__pycache__`
- Ambientes virtuais `venv/`
- Arquivos temporários de IDEs

Mantendo o repositório **limpo e organizado** ✅

---



## 🧭 Diagrama UML Simplificado

```text
+-----------------+          +------------------+
|    Cliente      |<>--------|  Conta           |
+-----------------+          +------------------+
| - nome          |          | - numero         |
| - endereco      |          | - saldo          |
| - cpf (privado) |          | - agencia        |
+-----------------+          +------------------+
         ^
         |
+-----------------+
| PessoaFisica    |
+-----------------+
| - data_nasc     |
+-----------------+

ContaCorrente herda de Conta e redefine sacar() com regras específicas.


---

```

**Como Executar o Sistema**

1. Clone o Repositório

git clone https://github.com/Santosdevbjj/otimizaSistemaBancario.git
cd otimizaSistemaBancario

2. Execute o Sistema

python main.py


---


🧪 **Fluxo de Uso Recomendado**

1. [nu] Novo Usuário → Cadastrar cliente (obrigatório).


2. [nc] Nova Conta → Vincular conta ao CPF do cliente.


3. [d] Depositar e [s] Sacar → Movimentações.


4. [e] Extrato → Visualizar transações.


5. [lc] Listar Contas → Ver contas ativas.


6. [q] Sair → Finalizar sistema.




---

🛠️ **Tecnologias Utilizadas**

🐍 Python 3.10+

🧠 Programação Funcional e Orientada a Objetos

🗂️ Arquitetura modular para manutenção e escalabilidade



---

📄 **Licença**

Este projeto está licenciado sob a Licença MIT.
Sinta-se à vontade para usar, estudar e melhorar! 🙌


---

🌟 **Contribuições**

Contribuições são bem-vindas!
Abra uma issue ou envie um pull request com sugestões de melhoria.

---

**Contato:**

[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://santosdevbjj.github.io/portfolio/)
[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz) 


---


