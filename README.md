# Xtudent

## 🗂️Índice

- [Objetivo do Projeto](#objetivo-do-projeto)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Colaboradores](#colaboradores)
- [Instalação local](#instalação-local)
- [Senhas e instruções de acesso](#senhas-e-instruções-de-acesso)
- [Video](#video)


## Objetivo do projeto

Xtudent é uma rede social para estudantes, construida como requisito parcial para obtenção de nota na disciplina de Programação para Sistemas Web II, do curso técnico integrado em Informática para Internet do IFBaiano - *campus* Guanambi.
---
## Tecnologias utilizadas
- ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
- ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
- ![SQLite](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
- ![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)


## Colaboradores
<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/riancesaros">
        <img src="https://avatars.githubusercontent.com/u/145462146?v=4" width="200px;" alt="Foto do Rian Cesar Oliveira Souza no GitHub"/><br>
        <sub>
          <b>Rian Cesar Souza</b>
        </sub>
      </a>
    </td>
      <td align="center">
      <a href="https://github.com/msantos7gabriel">
        <img src="https://avatars.githubusercontent.com/u/113394709?v=4" width="200px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Gabriel Montalvão</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/bruno-rodrigues0">
        <img src="https://avatars.githubusercontent.com/u/119943937" width="200px;" alt="Bruno Rodrigues"/><br>
        <sub>
          <b>Bruno Rodrigues</b>
        </sub>
      </a>
    </td>
    </tr>
</table>

## Instalação local

Caso queira rodar o Xtudent de forma local, segue as instruções:

1. Clone o repositório

```bash
git clone https://github.com/bruno-rodrigues0/PSW-FINAL
```

2. Crie um ambiente virtual e instale as dependencias

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Configuração do banco de dados

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

4. Execute o servidor de desenvolvimento

```bash
python3 manage.py runserver
```

---
## Video
#### Confira no link abaixo uma apresentação do sistema:

https://youtube.com/loremipsilum


