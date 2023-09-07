# FINECAP

An application to manager FINECAP stands.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

## Templates

### Setting up static files

- Este projeto utiliza o 
- Padrão Digital de Governo Design System | Versão 3.4.0 | https://www.gov.br/ds/home

### Instalação

- Requisitos

O projeto requer a versão mínima do node >= v18.13.0
Serão criados automaticamente os seguintes arquivos em seu projeto:

      $ package.json: configurações do seu projeto
      $ node_modules/@govbr-ds/core: pasta com os módulos necessários para o funcionamento do Design System

Instalação com npm
Confira sempre a versão referência ao baixar o pacote @govbr-ds/core.

Execute o comando: $ npm install @govbr-ds/core
