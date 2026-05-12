# fincli — controle financeiro sem complicacao

> Sabe quando o dinheiro some e voce nao faz ideia pra onde foi?
> O fincli resolve isso em segundos — direto do seu terminal.

[![CI](https://github.com/leticiasza/fincli-bootcamp2/actions/workflows/ci.yml/badge.svg)](https://github.com/leticiasza/fincli-bootcamp2/actions)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

> **Deploy:** https://github.com/leticiasza/fincli-bootcamp2#como-executar-deploy

---

## O problema

Todo mundo ja passou por isso:

* chega no fim do mes e o dinheiro simplesmente **sumiu**
* voce ate pensa em se organizar... mas nunca mantem
* planilhas sao chatas, apps sao pesados, tudo exige login

Resultado: desorganizacao, falta de controle e decisoes financeiras ruins.

---

## A solucao

O **fincli** foi feito pra ser o oposto disso.
Nada de app pesado. Nada de cadastro. Nada de complicacao.

Voce abre o terminal e digita:

```bash
fincli add "Almoco" 32.50
```

Pronto. Registrado. Simples assim.

E agora o `fincli total` tambem mostra o quanto voce gastou em outras moedas, em tempo real:

```
Total gasto: R$ 660,30
USD: $ 134,50   (dolar -0.66% hoje)
EUR: E 114,03   (euro  -0.12% hoje)
BTC: 0.00166097
```

---

## Pra quem isso e?

* Estudantes tentando controlar a grana do mes
* Freelancers organizando despesas
* Pessoas que ja tentaram se organizar e desistiram

Se voce ja disse **"preciso controlar melhor meu dinheiro"**, isso e pra voce.

---

## O que voce pode fazer

| Comando | O que acontece |
|---------|----------------|
| `fincli add <descricao> <valor>` | Registra um gasto em segundos |
| `fincli list` | Mostra todos os gastos com total |
| `fincli remove <indice>` | Remove um gasto errado |
| `fincli total` | Mostra o total em BRL, USD, EUR e BTC com variacao do dia |
| `fincli help` | Mostra ajuda |

---

## Integracao com API publica

O `fincli total` consome a [AwesomeAPI](https://docs.awesomeapi.com.br/) em tempo real para converter o total gasto em dolar, euro e bitcoin — sem precisar de login ou chave de acesso.

---

## Deploy

O fincli e uma aplicacao CLI — roda no terminal, nao no navegador.

Para usar em qualquer computador:

```bash
git clone https://github.com/leticiasza/fincli-bootcamp2.git
cd fincli-bootcamp2
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/Mac
pip install -e .
pip install -r requirements.txt
fincli help
```

Sem servidor. Sem hospedagem. Os dados ficam salvos localmente em `~/.fincli/expenses.json`.

---

## Como o projeto foi pensado

Esse nao e so um script — e um projeto estruturado de verdade.

Ele segue **Arquitetura Hexagonal (Ports & Adapters)**:

```
src/fincli/
├── models.py      <- Dominio (regras de negocio)
├── repository.py  <- Porta (contrato de persistencia)
├── adapters.py    <- Adaptador (JSON local)
├── services.py    <- Casos de uso
└── cli.py         <- Interface CLI + integracao com API
```

A logica nao depende de banco, a interface nao depende da regra, tudo pode evoluir sem quebrar o resto.

---

## Tecnologias usadas

* **Python 3.11+** — moderno e simples
* **pytest** — testes automatizados (unitarios e de integracao)
* **ruff** — qualidade e padronizacao de codigo
* **GitHub Actions** — validacao automatica (CI)
* **AwesomeAPI** — cotacao de moedas em tempo real

---

## Como instalar

```bash
git clone https://github.com/leticiasza/fincli-bootcamp2.git
cd fincli-bootcamp2
pip install -e .
pip install -r requirements.txt
```

---

## Como usar na pratica

```bash
fincli add "Cafe" 5.50
fincli add "Academia" 89.90
fincli add "Uber" 18.00
fincli list
fincli total
fincli remove 0
```

---

## Onde os dados ficam?

Tudo e salvo localmente no seu computador:

* Linux/Mac: `~/.fincli/expenses.json`
* Windows: `C:\Users\SeuUsuario\.fincli\expenses.json`

Sem nuvem. Sem login. Sem depender de nada externo.

---

## Testes

```bash
pytest
```

Os testes cobrem:

* cadastro de gastos
* validacao de erros
* calculo do total
* integracao com a AwesomeAPI (valida que a cotacao veio correta para USD, EUR e BTC)

---

## Qualidade de codigo (lint)

```bash
ruff check .
```

---

## Versao

Este projeto segue **versionamento semantico (SemVer)**.
Versao atual: `1.0.0`

---

## Autora

**Leticia Souza** — https://github.com/leticiasza

## Repositorio

https://github.com/leticiasza/fincli-bootcamp2
