### CONVERSOR DE MOEDAS - WSBACKEND-FABRICA25.1

Este é um projeto Django que permite a conversão de moedas utilizando a API Fixer. O frontend foi desenvolvido com Bootstrap, e o projeto é conteinerizado usando Docker.

---

## ÍNDICE
1. Descrição do Projeto
2. Funcionalidades
3. Tecnologias Utilizadas
4. Como Executar o Projeto
5. Estrutura do Projeto
6. Integração com a API Fixer
7. Contribuição
8. Licença

---

## DESCRIÇÃO DO PROJETO

O projeto é um conversor de moedas que utiliza taxas de câmbio em tempo real da API Fixer. Ele armazena o histórico de conversões e exibe os dados em uma tabela no frontend.

---

## FUNCIONALIDADES

- Conversão de moedas em tempo real.
- Histórico de conversões.
- Interface responsiva com Bootstrap.
- Conteinerização com Docker.

---

## TECNOLOGIAS UTILIZADAS

- Backend: Django
- Frontend: Bootstrap
- API: Fixer (https://fixer.io/documentation)
- Banco de Dados: SQLite
- Conteinerização: Docker

---

## COMO EXECUTAR O PROJETO

LOCALMENTE

 1. Clone o repositório:
 ```bash
   git clone https://github.com/mista-bit/wsBackend-Fabrica25.1.git
   cd wsBackend-Fabrica25.1
   ```

 2. Crie um ambiente virtual e instale as dependências:
 ```bash
   python -m venv venv
   source venv/bin/activate (No Windows: venv\Scripts\activate)
   pip install -r requirements.txt
   ```

3. Execute as migrações do banco de dados:
```bash
   python manage.py migrate
   ```

4. Inicie o servidor:
```bash
   python manage.py runserver
   ```

5. Acesse em: http://127.0.0.1:8000

COM DOCKER

1. Certifique-se de ter Docker instalado.

2. Construa e inicie os containers:
```bash
   docker-compose up --build
   ```

3. Acesse em: http://localhost:8000

---

## INTEGRAÇÃO COM A API FIXER

A chave da API Fixer está configurada em settings.py:

---
