# PP2

## Navegação
1. [Sobre](#sobre)
1. [Branch Principal](#branch-principal)
1. [Dependências](#dependências)
1. [Autores](#autores)

## Sobre

Repositório para a disciplina de Programação para Internet 2 do curso TSI do IFB. São feitos commits a cada módulo completo na atividade.

## Branch principal

- Master

## Dependências

- Python 3.7
- Pip
- virtualenv
- Django 2.2
- HTML, CSS e JavaScript

## Como executar

Entre no diretório do projeto e execute o comando `runserver` do manage.py

```
git clone https://github.com/HackTestesIFB/PP2 experiencein_repo

cd ./experiencein_repo/experiencein

./manage.py runserver
```

## Implantação

Este é um guia simples de implantação pensado a partir da na plataforma [Python Anywhere](https://www.pythonanywhere.com/), outros ambientes podem requerer passos diferentes.

### Requisitos iniciais

* Tenha uma conta na plataforma [Python Anywhere](https://www.pythonanywhere.com/)

* Posso clonar o atual repositório

### Observações

* O Django do repositório é para **DESENVOLVIMENTO**, ou seja, algumas modificações devem ser feitas para a implantação em produção

* As exatas alterações necessárias serão detalhadas nos passos seguintes

### Passos

1. Inicie um console Bash na máquina do [Python Anywhere](https://www.pythonanywhere.com/)

2. Clone o repositório

```
git clone https://github.com/HackTestesIFB/PP2 experiencein_repo
```

3. Instale o `virtualenv` no ambiente (pule se já estiver instalado)

    * Verificação
    ```
    pip3 show virtualenv
    ```

    * Instalação
    ```
    pip3 install virtualenv
    ```

4. Crie o ambiente virtual

```
mkvirtualenv --python=/usr/bin/python3.7 experiencein-virtualenv
```

5. Instalação e verificação do django 2.2 no ambiente virtual

    * Instalção
    ```
    pip install django==2.2
    ```

    * Verificação
    ```
    python -m django version
    ```

6. Volte ao dashboard do [Python Anywhere](https://www.pythonanywhere.com/), mas não feche o terminal (vamos precisar dele logo)

7. Crie um novo "*web app*"

8. Use o domínio padrão

9. Selecione a configuração manual: "*Manual configuration (including virtaulenvs)*"

10. Selecione a versão 3.7 do Python

11. Aperte em próximo quando aparecer o aviso de configuração manual (WSGI)

12. Configure um caminho virtualenv

    * Dica: se você usou o mkvirtualenv, é bem provável que esse seja o caminho do ambiente virtual(substitua pelo seu nome de usuário)
    ```
    /home/NOME_DE_USUARIO/.virtualenvs/experiencein-virtualenv
    ```

13. Vá para a seção Code --> WSGI configuration file e retire os comentários da seção de Django

14. Ainda na seção Django do arquivo WSGI, altere 2 variáveis

```
path = '/home/NOME_DE_USUARIO/experiencein_repo/experiencein'

    ...

os.environ['DJANGO_SETTINGS_MODULE'] = 'experiencein.settings'
```

15. Acesse os arquivos ("*Files*"), localizado ao lado do Dashboard no topo da página

16. Altere o arquivo `/home/HackTestesIFB/experiencein_repo/experiencein/experiencein/settings.py` e insira a seguinte entrada à variável *ALLOWED_HOSTS*

```
ALLOWED_HOSTS = ['NOME_DO_DOMÍNIO']
```

17. Mude o valor da variável `DEBUG` para `False`
```
DEBUG = False
```

18. Volte ao terminal e execute o seguinte comando para coletar os arquivos estatáticos
```
cd ~/experiencein_repo/experiencein && python manage.py collectstatic
```

19. Volte ao painel "*Web*" o modifique o campo "*Static files*"

```
URL                     Directory

/static/                /home/NOME_DE_USUARIO/experiencein_repo/experiencein/static
```

**FINALIZADO**!!! Agora é só acessar o seu domínio!

[Domínio utilizado pelo repositório](https://hacktestesifb.pythonanywhere.com/)

## Autores

Caio Gomes Flausino
