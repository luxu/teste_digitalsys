# Sistema de Gestão de Propostas de Empréstimo Pessoal 

O aplicativo tem como finalidade gerar propostas de empréstimos que serão enviadas e analisadas pela financeira 

## Backend do projeto

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
* Crie um usuário padrão.

```
git clone https://github.com/luxu/teste_digitalsys.git
cd backend
python3 -m venv .venv
.venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements/dev.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email="admin@admin.com"
```
