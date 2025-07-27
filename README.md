# 🧮 Calculadora Django

Este é um projeto de uma **calculadora desenvolvida com Django**.  
Você pode rodar o projeto usando o `Pipenv` (ambiente original), ou com o `requirements.txt` para instalar as dependências em outro gerenciador de ambiente virtual como `venv`.

---

## 🚀 Requisitos

- Python 3.10 ou superior
- Pip
- Pipenv (opcional, mas recomendado)

---

## 🛠️ Como executar o projeto

### ✅ Opção 1: Usando Pipenv (recomendado)

1. Instale o Pipenv (caso ainda não tenha):

   ```bash
   pip install pipenv
   ```

2. Instale as dependências:

   ```bash
   pipenv install
   ```

3. Ative o ambiente virtual:

   ```bash
   pipenv shell
   ```

4. Rode o servidor:

   ```bash
   python manage.py runserver
   ```

---

### ✅ Opção 2: Usando requirements.txt (sem Pipenv)

1. Crie um ambiente virtual com `venv`:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```

2. Instale as dependências via pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Rode o servidor:

   ```bash
   python manage.py runserver
   ```

---

## 🧪 Funcionalidades

- Interface simples e funcional
- Operações básicas: adição, subtração, multiplicação, divisão
- Desenvolvida como aplicação web com Django

---

## 📂 Estrutura do projeto

```
calculator/
│
├── static/               # Arquivos estáticos (CSS, JS, imagens)
├── templates/            # Templates HTML
├── setup/                # Configurações do projeto Django
├── apps/                 # Apps da calculadora
├── manage.py
├── Pipfile               # Arquivo do pipenv
├── Pipfile.lock
├── requirements.txt      # Gerado a partir do Pipfile
└── README.md

```

---

## 🧑‍💻 Autor

Desenvolvido por [Wilian Soares dos Santos].

---
