# Como Rodar a API

### pré-requisitos:

- python 3.6^
- pip

Os comandos devem ser executados na pasta raiz do projeto.

## 1. Criar uma venv (*opcional*):

> $ sudo apt-get install -y python3-venv
>
> $ python3 -m venv <nome_da_venv>
>
> $ source <nome_da_venv>/bin/activate

## 2. Instalar os pacotes necessários para rodar o projeto:

> $ pip install -r requirements.txt

## 3. Migrar o banco de dados

> $ python manage.py makemigrations
>
> $ python manage.py migrate

## 4. Rodar a api

> $ python manage.py runserver

A API estará disponível na porta 8000

# Como utilizar a API

## Accounts

Para utilizar os outros end-points, é necessário fazer cadastro utilizando os endpoints do
pacote [djoser](https://djoser.readthedocs.io/en/latest/getting_started.html). Todos os endpoits do djoser se encontram
em /api/accounts/. Aapós o login receberá uma token que deve ser enviada nos Request Headers, exemplo:

Endpoint para cadastro: /api/accounts/users/

Endpoint para login: /api/accounts/token/login

> Authorization:Token 07097e1223b7a95fff9a87854931863125eb474c

## Profiles

### /api/profiles/?page=<número_da_página>&cpf=<cpf_do_usuário>

#### 'GET'

Retorna lista de objetos de perfis. Cada página possui 50 objetos, se não fo especificado o parâmetro page retorna a
primeira. Informando o cpf retorna lista apenas com o objeto do perfil específico.

Exemplo de resposta:

```javascript
[
    {
        "cpf": "94041965098",
        "nome": "batman",
        "data_nascimento": "1212-12-12",
        "telefone": "123456789",
        "endereco_cep": "123132",
        "endereco_nome_rua": "vento",
        "endereco_complemento": "que faz a curva",
        "endereco_numero": "24",
        "endereco_nome_cidade": "Ventania",
        "endereco_estado": "CC",
        "created_at": "2021-05-13T00:36:39.316891Z",
        "photo": "http://127.0.0.1:8000/media/photos/exemplo.jpg",
        "is_employee": false,
        "created_by": 2
    },
    {
        "cpf": "11090210035",
        "nome": "joaquim",
        "data_nascimento": "1998-12-10",
        "telefone": "1234567899",
        "endereco_cep": "72831234",
        "endereco_nome_rua": "vento",
        "endereco_complemento": "que faz a curva",
        "endereco_numero": "24",
        "endereco_nome_cidade": "Ventania",
        "endereco_estado": "CC",
        "created_at": "2021-05-13T00:14:10.456150Z",
        "photo": "http://127.0.0.1:8000/media/photos/photo-1481349518771-20055b2a7b24.jpeg",
        "is_employee": true,
        "created_by": 2
    }
]
```

### /api/profiles/create/

#### 'POST'

Recebe um json como o seguinte para cadastrar um cliente.

```javascript
{
    "cpf"
:
    "",
        "nome"
:
    "",
        "data_nascimento"
:
    null,
        "telefone"
:
    "",
        "photo"
:
    null,
        "is_employee"
:
    false,
        "endereco_cep"
:
    "",
        "endereco_nome_rua"
:
    "",
        "endereco_complemento"
:
    "",
        "endereco_numero"
:
    "",
        "endereco_nome_cidade"
:
    "",
        "endereco_estado"
:
    ""
}
```

### /api/profiles/photos/

#### 'GET'

Retorna lista de todos os usuários contendo nome, foto e cpf.

```javascript
[
    {
        "nome": "joaquim",
        "photo": "http://127.0.0.1:8000/media/photos/photo-1481349518771-20055b2a7b24.jpeg",
        "cpf": "11090210035"
    },
    {
        "nome": "batman",
        "photo": "http://127.0.0.1:8000/media/photos/caderno-de-receitas-receitas.jpg",
        "cpf": "94041965098"
    }
]
```

## Events

### /api/events/

#### 'POST'

Cria um novo evento de entrada ou saída de cliente, json de exemplo:

```javascript
{
    "entrance"
:
    false, // Foi entrada?
        "temp"
:
    "36", // Temperatura
        "user"
:
    11090210035 // cpf
}
```

#### 'GET'

Retorna lista de objetos de eventos. Cada página possui 50 objetos, se não fo especificado o parâmetro page retorna a
primeira. Informando o cpf retorna lista de eventos de um usuário específico.

Exemplo de resposta:

```javascript
[
    {
        "id": 3,
        "timestamp": "2021-05-13T01:57:56.731406Z",
        "entrance": true,
        "temp": "36",
        "user": "11090210035"
    },
    {
        "id": 2,
        "timestamp": "2021-05-13T01:57:44.056570Z",
        "entrance": false,
        "temp": "13",
        "user": "94041965098"
    },
    {
        "id": 1,
        "timestamp": "2021-05-13T01:57:16.783456Z",
        "entrance": true,
        "temp": "25",
        "user": "11090210035"
    }
]
```