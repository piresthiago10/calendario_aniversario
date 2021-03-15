# Calendário de Aniversários

  Uma simples agenda para armazenar datas de aniversários através do consumo de uma API Django via Vue.js.

# Autores:

* **Thiago Pires** - *Desenvolvedor Fullstack*

## Requisitos do sistema:

* Python 3.6;
* Django 3.1.7;
* Django Rest Framework 3.12.2;
* Node.js 10.24.0;
* Vue.js 2.5.11

## Instalção:

Após clonar o projeto para sua máquina siga as seguintes instruções:

Terminal 1:

1. Crie um ambiente virtual na pasta do projeto [django] e acesse-o:
```
python3 - m venv venv
source venv/bin/activate
```
2. Instale os requisitos do projeto:
```
pip install -r requirements.txt
```
3. Inicie o servidor da api no diretório que contém o arquivo manage.py:
```
python3 manage.py runserver
```

Terminal 2:
1. Inicie o projeto Vue em [calendario_aniversario]:
```
npm install
npm run dev
```
2. Abra o projeto no navegador:
```
http://localhost:8080/
```

## Testes da API:

Siga até o passo 2 do terminal 1 em uma nova aba do terminal e execute o comando:
```
python3 manage.py test
```

## Ferramentas utilizadas

Informe aqui as ferramentas utilizadas para o desenvolvimento do projeto

* [Visual Studio Code](https://code.visualstudio.com/)
* [Google Chrome](https://www.google.pt/intl/pt-PT/chrome/?brand=CHBD&gclid=Cj0KCQjwn_LrBRD4ARIsAFEQFKt3kLTIsdU6a-sk3FKsxrhplkKaYNHo6Pt3aRbaEAJ3TK4fZslZmtUaAvHVEALw_wcB&gclsrc=aw)
* [Postman](https://www.postman.com/)

