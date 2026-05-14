![PythonDeveloper001](https://github.com/user-attachments/assets/47f8e7eb-1ede-4051-8894-100171801849)

# 🏦 Otimização do Sistema Bancário — Refatoração com Funções e POO em Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
![Status](https://img.shields.io/badge/Status-Ativo-success?style=flat)
![License](https://img.shields.io/badge/Licença-MIT-green)
![Paradigmas](https://img.shields.io/badge/Paradigmas-Funcional%20%2B%20POO-orange)
[![GitHub last commit](https://img.shields.io/github/last-commit/Santosdevbjj/otimizando-sistema-bancario)](https://github.com/Santosdevbjj/otimizando-sistema-bancario/commits/main)
![Bootcamp](https://img.shields.io/badge/Bootcamp-Suzano_Python_Developer_%232-purple)

> Refatoração completa de um sistema bancário procedural de usuário único para uma arquitetura modular com domínio orientado a objetos, suporte a múltiplos clientes e contratos explícitos de funções — padrão de evolução técnica diretamente aplicável a sistemas financeiros reais.

---

## 1. Problema de Negócio

O sistema bancário original ([v1](https://github.com/Santosdevbjj/sistema-bancario-em-python)) operava com **um único usuário implícito** e misturava regras de negócio com lógica de apresentação no mesmo bloco de código. Isso criava três limitações concretas:

- **Não escalava para múltiplas contas:** não havia modelo de cliente nem vinculação entre conta e titular.
- **Impossível de testar em isolamento:** as regras de saque estavam acopladas à lógica de menu.
- **Sem contrato explícito entre módulos:** qualquer extensão exigia leitura e alteração de todo o código.

O objetivo desta versão é resolver os três problemas simultaneamente — entregando uma arquitetura que suporta múltiplos clientes, separa domínio de apresentação e define contratos explícitos entre camadas.

---

## 2. Contexto

O projeto é a **Versão 2.0** de uma série de evoluções do mesmo sistema bancário, desenvolvida no **Bootcamp Suzano – Python Developer #2** (DIO). O escopo foi deliberadamente restrito a CLI para manter o foco na qualidade arquitetural — não na interface.

O sistema entrega:

- Cadastro de múltiplos clientes com CPF único como chave de identificação.
- Criação de contas correntes vinculadas a clientes existentes.
- Operações de depósito, saque e extrato com regras de negócio encapsuladas na classe `ContaCorrente`.
- Listagem de todas as contas ativas com seus respectivos titulares.

---

## 3. Premissas

- CPF é a chave única de identificação de cliente — duplicatas são rejeitadas no cadastro.
- O limite de R$ 500,00 por saque e o teto de 3 saques diários são configuráveis na instanciação de `ContaCorrente` (não hardcoded no fluxo principal).
- Não há persistência entre sessões nesta versão — o estado é mantido em memória durante a execução.
- `src/models/conta.py` define a hierarquia de classes de conta; `src/services/operacoes_bancarias.py` mantém funções compatíveis com a versão anterior para demonstrar coexistência dos dois paradigmas.

---

## 4. Estratégia da Solução

A refatoração seguiu três decisões técnicas sequenciais:

**Decisão 1 — Separação em camadas**

O código foi dividido em duas camadas deliberadamente independentes:

```
main.py                          ← Apresentação: menu + orquestração
src/
├── models/
│   ├── cliente.py               ← Domínio: entidades Cliente e PessoaFisica
│   └── conta.py                 ← Domínio: entidades Conta e ContaCorrente
└── services/
    └── operacoes_bancarias.py   ← Serviços: funções de operação com contratos explícitos
```

`main.py` nunca implementa regra de negócio. Toda lógica de validação (saldo, limite, limite diário) está encapsulada nas camadas de modelo e serviço.

**Decisão 2 — Contratos explícitos de argumentos Python**

As funções de serviço usam três convenções de argumentos de forma intencional, não arbitrária:

| Função | Convenção | Justificativa |
|---|---|---|
| `depositar(saldo, valor, extrato, /)` | Posicional Only (`/`) | Saldo e valor são posicionais por natureza — a ordem importa, não o nome |
| `sacar(*, saldo, valor, extrato, ...)` | Keyword Only (`*`) | Múltiplos argumentos numéricos — nomes obrigatórios eliminam erros de ordem |
| `exibir_extrato(saldo, /, *, extrato)` | Misto | Saldo é posicional; extrato nomeado para legibilidade na chamada |

Essa escolha transforma a assinatura da função em documentação executável — qualquer desenvolvedor que chame `sacar()` sem nomear os argumentos recebe erro imediato.

**Decisão 3 — Hierarquia de classes com especialização de comportamento**

```
Cliente
└── PessoaFisica          ← Adiciona CPF (privado), nome e data de nascimento

Conta
└── ContaCorrente         ← Sobrescreve sacar() com limite por operação e limite diário
```

`ContaCorrente.sacar()` chama `super().sacar()` apenas após validar suas regras específicas — o princípio de substituição de Liskov aplicado: qualquer `ContaCorrente` pode ser tratada como `Conta` sem quebrar o sistema.

---

## 5. Decisões Técnicas e Trade-offs

**Por que manter dois paradigmas (funcional em `services/` e POO em `models/`) no mesmo projeto?**

Porque refletir a realidade de codebases em evolução é mais valioso do que demonstrar pureza técnica. Em sistemas reais, funções procedurais e classes coexistem durante migrações — saber quando e como separar responsabilidades em projetos heterogêneos é uma habilidade de engenharia concreta.

**Por que CPF como chave única e não ID autoincremental?**

CPF é a chave de domínio real no sistema financeiro brasileiro. Usar ID autoincremental seria correto tecnicamente mas ignoraria o domínio. Modelar o domínio com fidelidade é o que diferencia um sistema bancário de um CRUD genérico.

**Por que `_cpf` privado com `@property` e não atributo público?**

CPF é dado sensível. Expô-lo como atributo público permitiria mutação direta (`cliente.cpf = "999"`). O `@property` garante acesso de leitura sem setter — encapsulamento com propósito, não por convenção.

**Trade-off aceito:** as funções em `operacoes_bancarias.py` retornam tuplas atualizadas de estado (`saldo, extrato`) em vez de operar sobre objetos. Em uma v3, essas funções seriam substituídas por métodos diretamente nas classes — mas a coexistência foi mantida para demonstrar a estratégia de migração incremental.

---

## 6. Diagrama UML — Hierarquia de Classes

```
┌─────────────────────────┐          ┌──────────────────────────────────┐
│         Cliente         │◇─────────│            Conta                 │
├─────────────────────────┤          ├──────────────────────────────────┤
│ - _endereco : str       │          │ - _saldo : float                 │
│ + contas : list         │          │ - _numero : int                  │
├─────────────────────────┤          │ - _agencia : str = "0001"        │
│ + endereco (property)   │          │ - _cliente : Cliente             │
│ + realizar_transacao()  │          │ - _historico : list              │
│ + adicionar_conta()     │          ├──────────────────────────────────┤
└─────────────────────────┘          │ + saldo / numero / agencia       │
           ▲                         │ + sacar(valor) : bool            │
           │                         │ + depositar(valor) : bool        │
┌─────────────────────────┐          │ + nova_conta() [classmethod]     │
│     PessoaFisica        │          └──────────────────────────────────┘
├─────────────────────────┤                         ▲
│ - _cpf : str            │                         │
│ + nome : str            │          ┌──────────────────────────────────┐
│ + data_nascimento : str │          │        ContaCorrente             │
├─────────────────────────┤          ├──────────────────────────────────┤
│ + cpf (property)        │          │ - _limite : float = 500.0        │
│ + __repr__()            │          │ - _numero_saques : int           │
└─────────────────────────┘          │ LIMITE_SAQUES : int = 3          │
                                     ├──────────────────────────────────┤
                                     │ + sacar(valor) : bool [override] │
                                     │ + __repr__()                     │
                                     └──────────────────────────────────┘
```

---

## 7. Estrutura do Projeto

```
otimizando-sistema-bancario/
├── src/
│   ├── models/
│   │   ├── cliente.py               # Entidades Cliente e PessoaFisica
│   │   └── conta.py                 # Entidades Conta e ContaCorrente
│   └── services/
│       └── operacoes_bancarias.py   # Funções de serviço com contratos de argumentos
├── main.py                          # Ponto de entrada: menu e orquestração
├── .gitignore
└── README.md
```

---

## 8. Como Executar

**Pré-requisitos:** Python 3.10+

```bash
# 1. Clone o repositório
git clone https://github.com/Santosdevbjj/otimizando-sistema-bancario.git
cd otimizando-sistema-bancario

# 2. Execute
python main.py
```

**Fluxo recomendado de uso:**

```
[nu] Novo Usuário    → Cadastre ao menos um cliente (CPF obrigatório)
[nc] Nova Conta      → Vincule uma conta ao CPF cadastrado
[d]  Depositar       → Efetue depósito na conta ativa
[s]  Sacar           → Saque respeitando limite e teto diário
[e]  Extrato         → Visualize histórico e saldo atual
[lc] Listar Contas   → Consulte todas as contas ativas com seus titulares
[q]  Sair
```

---

## 9. Resultados

A refatoração entregou três melhorias mensuráveis em relação à v1:

**Extensibilidade:** adicionar um novo tipo de conta (ex: `ContaPoupança`) exige apenas herdar de `Conta` e sobrescrever `sacar()` — sem tocar em `main.py` ou nos serviços.

**Testabilidade:** `ContaCorrente.sacar()` pode ser testado unitariamente com `pytest` sem instanciar menu, sem capturar `input()`, sem estado global — porque a lógica de negócio está completamente isolada da apresentação.

**Legibilidade de contrato:** a assinatura `sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)` torna impossível chamar a função na ordem errada. O erro acontece em tempo de execução imediatamente, não silenciosamente em produção.

---

## 10. Aprendizados

**O que foi mais valioso:**

A distinção entre argumentos posicionais-only (`/`) e keyword-only (`*`) não é apenas sintaxe — é design de API. Ao escolher `depositar(saldo, valor, extrato, /)`, a função comunica: *"a ordem importa aqui, não invente nomes alternativos"*. Ao escolher `sacar(*, ...)`, comunica: *"com tantos floats, nomes obrigatórios são proteção contra bugs silenciosos"*. Isso é raciocínio de engenharia, não decoração de código.

**O que faria diferente:**

Eliminaria o estado global em `main.py` (`saldo`, `extrato`, `numero_saques` como variáveis soltas). Uma classe `SistemaBancario` que agrega a lista de clientes e contas tornaria o estado explícito e eliminaria a dependência de variáveis de módulo — pré-requisito para testes de integração limpos.

---

## 11. Próximos Passos

- [ ] Criar classe `SistemaBancario` para encapsular estado global de `main.py`
- [ ] Adicionar classe `Historico` para substituir a lista plana `_historico` em `Conta`
- [ ] Implementar classes `Transacao`, `Saque` e `Deposito` como objetos de domínio
- [ ] Adicionar persistência com SQLite via `sqlite3` ou SQLAlchemy
- [ ] Escrever testes unitários com `pytest` para `ContaCorrente.sacar()` e `depositar()`
- [ ] Expor operações via API REST com FastAPI (v3)

---

## Tecnologias Utilizadas

| Tecnologia | Uso no Projeto |
|---|---|
| Python 3.10+ | Linguagem principal |
| POO com herança e polimorfismo | Modelagem do domínio bancário |
| Type hints (`typing`) | Contratos explícitos nos métodos |
| Argumentos posicionais-only e keyword-only | Design de API de funções |
| Arquitetura modular (`src/models`, `src/services`) | Separação de responsabilidades |

---

## Autor

**Sérgio Santos**
Senior Data Engineer & Cloud Architect

[![Portfólio](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://portfoliosantossergio.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz)
[![GitHub](https://img.shields.io/badge/GitHub-Santosdevbjj-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Santosdevbjj)

---

## Licença

Distribuído sob licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
