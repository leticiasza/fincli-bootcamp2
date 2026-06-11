# fincli — controle financeiro sem complicacao

> Sabe quando o dinheiro some e voce nao faz ideia pra onde foi?
> O fincli resolve isso — agora como API web com banco de dados na nuvem.

[![CI](https://github.com/leticiasza/fincli-bootcamp2/actions/workflows/ci.yml/badge.svg)](https://github.com/leticiasza/fincli-bootcamp2/actions)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## O problema

Todo mundo ja passou por isso:

* chega no fim do mes e o dinheiro simplesmente **sumiu**
* planilhas sao chatas, apps sao pesados, tudo exige login

Resultado: desorganizacao, falta de controle e decisoes financeiras ruins.

---

## A solucao

O **fincli** e uma API de controle de gastos pessoais — simples, direto ao ponto.

Registre, liste, remova gastos e veja o total convertido em USD, EUR e BTC em tempo real.

---

## Deploy

**API em producao:** https://fincli-bootcamp2.onrender.com

Documentacao interativa (Swagger): https://fincli-bootcamp2.onrender.com/docs

---

## Endpoints

| Metodo | Rota | O que faz |
|--------|------|-----------|
| `POST` | `/expenses` | Registra um gasto |
| `GET` | `/expenses` | Lista todos os gastos |
| `DELETE` | `/expenses/{id}` | Remove um gasto |
| `GET` | `/total` | Total em BRL, USD, EUR e BTC |

---

## Integracao com API publica

O endpoint `/total` consome a [AwesomeAPI](https://docs.awesomeapi.com.br/) em tempo real para converter o total gasto em dolar, euro e bitcoin.

---

## Arquitetura

Projeto estruturado com **Arquitetura Hexagonal (Ports & Adapters)**:
src/fincli/
├── models.py           <- Dominio (regras de negocio)
├── repository.py       <- Porta (contrato de persistencia)
├── adapters.py         <- Adaptador JSON (legado)
├── supabase_adapter.py <- Adaptador Supabase (producao)
├── services.py         <- Casos de uso
├── api.py              <- Interface FastAPI
└── cli.py              <- Interface CLI (legado)

---

## Tecnologias

* **Python 3.13**
* **FastAPI + Uvicorn** — API web
* **Supabase (PostgreSQL)** — banco de dados na nuvem
* **Render** — deploy e hospedagem
* **pytest** — testes automatizados
* **ruff** — qualidade de codigo
* **GitHub Actions** — CI
* **AwesomeAPI** — cotacao de moedas em tempo real

---

## Como executar localmente

```bash
git clone https://github.com/leticiasza/fincli-bootcamp2.git
cd fincli-bootcamp2
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
pip install -e .
```

Crie um arquivo `.env` com:
SUPABASE_URL=sua_url
SUPABASE_KEY=sua_chave

Inicie a API:

```bash
uvicorn fincli.api:app --reload
```

---

## Testes

```bash
pytest
```

---

## Qualidade de codigo

```bash
ruff check .
```

---

## Autora

**Leticia Souza** — [@leticiasza](https://github.com/leticiasza)

## Repositorio

https://github.com/leticiasza/fincli-bootcamp2