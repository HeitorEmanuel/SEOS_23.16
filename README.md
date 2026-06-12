# SEOS 23.16 - Sistema de Emissão de Ordem de Serviço

## Descrição do Projeto

O SEOS (Sistema de Emissão de Ordem de Serviço) é uma aplicação desenvolvida utilizando Python e Django para gerenciamento de clientes, ordens de serviço, estoque de peças e acompanhamento de atendimentos técnicos.

O sistema permite controlar todo o fluxo de manutenção de equipamentos, desde o cadastro do cliente até a conclusão do serviço, incluindo histórico de alterações e auditoria das operações realizadas.

## Integrantes do Grupo

* Heitor Emanuel da Silva Amorim
* Heitor Leoni Costa Bezerra
* Sony Jones da Silva Vitoriano
* José Damasceno Filho

## Tecnologias Utilizadas

* Python 3.13
* Django
* SQLite
* HTML
* CSS
* JavaScript
* Jazzmin

## Requisitos para Execução

* Python 3.13 ou superior
* Git (opcional)
* Navegador Web moderno

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/HeitorEmanuel/SEOS_23.16.git
cd SEOS_23.16
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar ambiente virtual

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

### 4. Atualizar o pip

```bash
python -m pip install --upgrade pip
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

Caso necessário:

```bash
pip install django
pip install jazzmin
pip install django-extensions
pip install pydot
```

### 6. Aplicar as migrações

```bash
python manage.py migrate
```

### 7. Criar superusuário (Opcional)

```bash
python manage.py createsuperuser
```

### 8. Executar o sistema

```bash
python manage.py runserver
```

## Acesso ao Sistema

### Painel do Cliente

```text
http://127.0.0.1:8000/
```

### Painel Administrativo

```text
http://127.0.0.1:8000/admin/
```

## Módulos Principais

* Cadastro de Usuários
* Cadastro de Clientes
* Ordens de Serviço
* Controle de Estoque
* Entrada e Saída de Peças
* Histórico de Ordens de Serviço
* Auditoria do Sistema
* Painel do Cliente
* Impressão de OS
* Etiquetas

## Controle de Acesso

### Atendente

* Cadastro de clientes
* Cadastro de ordens de serviço
* Impressão de documentos

### Técnico / Administrador

* Acesso completo ao sistema

### Almoxarifado

* Controle de peças
* Movimentação de estoque

### Cliente

* Acompanhamento das próprias ordens de serviço

## Observações

* Banco de dados SQLite incluso no projeto.
* Arquivo `db.sqlite3` utilizado para armazenamento dos dados.
* Arquivos temporários, cache e configurações locais não fazem parte do repositório.
* Projeto desenvolvido para fins acadêmicos utilizando a metodologia RAD.
