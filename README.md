# CRUD - Python & Vue

Este é um projeto baseado na ideia do Linktree, desenvolvido com React.js, Tailwind CSS e Firebase. O sistema inclui roteamento de páginas, banco de dados, sistema de login e um painel de administrador.



## Backend 
This is the backend part of the VueCRUD project. It is built using Flask and connects to a MongoDB database to handle user data.



- User Management: Create, read, update, and delete users.
- MongoDB Integration: All user data is stored in a MongoDB database.
- RESTful API: The backend exposes a REST API for interacting with user data


### Setup
#### Prerequisites
Python 3.x
Flask
Flask-CORS
pymongo

- Cadastro e Login

    - Autenticação via Firebase Authentication

    - Login com email/senha

- Gerenciamento de Links

    - Adicionar, editar e remover links

    - Personalização do perfil

- Painel de Admin

    - Controle total sobre os links cadastrados

    - Configuração do tema e design

### InstalaçãO
 1. Clone this repository

        
        git clone https://github.com/pedrohfreitas01/deepSyste-CRUD
        cd backend



2. Install dependencies:

        
        pip install -r requirements.txt


3. ensure MongoDB is running locally or configure it to connect to a remote MongoDB instance.

        
4. Inicie o projeto:
 python app.py
