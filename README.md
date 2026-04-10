# 💸 fincli — controle financeiro sem complicação

> Sabe quando o dinheiro some e você não faz ideia pra onde foi?
> O fincli resolve isso em segundos — direto do seu terminal.

[![CI](https://github.com/your-username/fincli/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/fincli/actions)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 😤 O problema

Todo mundo já passou por isso:

* chega no fim do mês e o dinheiro simplesmente **sumiu**
* você até pensa em se organizar… mas nunca mantém
* planilhas são chatas, apps são pesados, tudo exige login

Resultado: desorganização, falta de controle e decisões financeiras ruins.

---

## 💡 A solução

O **fincli** foi feito pra ser o oposto disso.

Nada de app pesado. Nada de cadastro. Nada de complicação.

👉 Você abre o terminal e digita:

```bash
fincli add "Almoço" 32.50
```

Pronto. Registrado.

Simples assim.

---

## 👥 Pra quem isso é?

* 🎓 Estudantes tentando controlar a grana do mês
* 💻 Freelancers organizando despesas
* 🧠 Pessoas que já tentaram se organizar e desistiram

Se você já disse **"preciso controlar melhor meu dinheiro"**, isso é pra você.

---

## ✨ O que você pode fazer

| Comando                          | O que acontece                   |
| -------------------------------- | -------------------------------- |
| `fincli add <descrição> <valor>` | Registra um gasto em segundos    |
| `fincli list`                    | Mostra todos os gastos com total |
| `fincli remove <índice>`         | Remove um gasto errado           |
| `fincli total`                   | Mostra quanto você já gastou     |
| `fincli help`                    | Mostra ajuda                     |

---

## 🏗️ Como o projeto foi pensado

Esse não é só um script — é um projeto estruturado de verdade.

Ele segue **Arquitetura Hexagonal (Ports & Adapters)**:

```
src/fincli/
├── models.py      ← Domínio (regras de negócio)
├── repository.py  ← Porta (contrato de persistência)
├── adapters.py    ← Adaptador (JSON local)
├── services.py    ← Casos de uso
└── cli.py         ← Interface CLI
```

👉 A ideia é simples:

* a lógica não depende de banco
* a interface não depende da regra
* tudo pode evoluir sem quebrar o resto

---

## 🛠️ Tecnologias usadas

* **Python 3.11+** — moderno e simples
* **pytest** — testes automatizados
* **ruff** — qualidade e padronização de código
* **GitHub Actions** — validação automática (CI)

---

## 🚀 Como instalar

```bash
# Clonar o projeto
git clone https://github.com/your-username/fincli.git
cd fincli

# Instalar (cria o comando fincli)
pip install -e .

# Instalar dependências de desenvolvimento
pip install -r requirements.txt
```

---

## ▶️ Como usar na prática

```bash
fincli add "Café" 5.50
fincli add "Academia" 89.90
fincli add "Uber" 18.00

fincli list
fincli total
fincli remove 0
```

---

## 💾 Onde os dados ficam?

Tudo é salvo localmente no seu computador:

* Linux/Mac: `~/.fincli/expenses.json`
* Windows: `C:\Users\SeuUsuario\.fincli\expenses.json`

👉 Sem nuvem. Sem login. Sem depender de nada externo.

---

## 🧪 Testes

```bash
pytest
```

Os testes cobrem:

* cadastro de gastos
* validação de erros
* cálculo do total

---

## 🔍 Qualidade de código (lint)

```bash
ruff check .
```

---

## 📦 Versão

Este projeto segue **versionamento semântico (SemVer)**.

Versão atual:

```
1.0.0
```

---

## 👨‍💻 Autor

**Leticia Souza**

https://github.com/leticiasza
---

## 🔗 Repositório

https://github.com/leticiasza/fincli-bootcamp2.git

---
