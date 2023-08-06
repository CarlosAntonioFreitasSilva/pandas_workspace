# Administrador de Blog

Vamos construir um administrador de postagens no qual podem ser exibidas em páginas web onde os visitantes poderão acessar as postagens do blog. Para tanto, utilizaremos o framework Django.

## Instalando Python
Para instalar o python acesse
https://www.python.org/downloads/ e baixe o instalador do Python para seu sistema operacional.

Para verificar se o Python foi instalado abra o terminal de seu Sistema Operacional e digite para obter a versão do Python, caso a instalação tenha sido feita


~~~
python --version
~~~


## Instalando Django

Vamos utilizar o Package Installer for Python para instalar o Django. Abra terminal do seu Sistema Operacional e digite
~~~
pip install Django==4.2.4
~~~

## Instalando SQLite
Instale o SQLite acessando https://www.sqlite.org/index.html para fazer download do instalador.

# Projeto Blog

Vamos criar um projeto no disco `C:`. Para isso vamos acessá-lo pelo terminal do sistema operacional. No caso do Windows digitamos o comando

~~~
cd c:\\
~~~

Agora vamos criar nosso projeto digitando o comando

~~~
django-admin startproject blog
~~~
Acesse o diretório que você criou e veja que o Django criou o projeto com uma estrutura de arquivos e pasta.
~~~
.
└── blog
    ├── blog
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        ├── wsgi.py
    ├── manage.py
~~~

Por ora, não vamos detalhar para que serve cada um desses arquivos. A medida em que avançamos no desenvolvimento do projeto passaremos por cada um deles.


Com o projeto criado vamos agora criar a nossa aplicação. Em um projeto Django podemos ter várias aplicações e uma aplicação pode estar em vários projetos. Por exemplo, suponha que você esteja criando um projeto de uma agenda. Nesse projeto você pode criar uma aplicação chamada `contato` para guardar nome, número de celular e e-mail de seus contatos, uma aplicação chamada `evento` para guardar compromissos agendados com local e data e uma aplicação chamada `notes` para armazenar anotações.

No nosso caso, vamos criar uma aplicação `posts` em que temos as postagens do nosso blog.

## Criando aplicação 

Para criar uma aplicação chamada `posts` acessamos o diretório blog pelo terminal, no caso do windows usamos o comando `cd blog` e digitamos 
~~~
py manage.py startapp posts
~~~

Após executar o comando acesse o diretório de seu projeto e observe que o Django criou uma nova pasta posts com a nossa aplicação cuja estrutura é mostrada a seguir:
~~~
.
└──posts
    ├──  migrations
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
~~~
No arquivo `apps.py` temos a classe da nossa aplicação criada pelo Django nomeada de `PostsConfig`

**Observação**: O Django cria a classe da aplicação utilizando nome da aplicação junto com a palavra Config.


### Adicionar aplicação 

Após a criação da aplicação `posts` devemos acessar as configurações do nosso projeto no arquivo `settings.py`. Ao abrir o arquivo você verá, como mostra o código a seguir, um array `INSTALLED_APPS` no qual possui todas as aplicações do projeto:

~~~python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
~~~
Devemos então adicionar a aplicação `posts` ao projeto. Para isso, adicionamos o item `posts.apps.PostsConfig` no array como mostra o código a seguir.

~~~python
# Application definition

INSTALLED_APPS = [
    'posts.apps.PostsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

~~~
 
**Observação**: O item adicionado refere-se ao diretório, onde posts significa a pasta posts, apps é o arquivo apps.py e PostsConfig é a classe da aplicação.

Após adicionarmos nossa aplicação `posts` ao projeto vamos criar os modelos da nossa aplicação.

### Modelos da aplicação 

Os modelos de uma aplicação são criados no arquivo `models.py`. Os modelos representam as tabelas do banco de dados e então cada tabela será uma classe que herda a classe `Model` do Django. No caso de uma postagem de um blog vamos utilizar um modelo simples onde cada postagem tem um título, texto da postagem, autor e a data. 

~~~python
from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    author = models.CharField(max_length=30)
    date = models.DateField(null=False)

    def __str__(self): 
        return self.title + " by " + self.author + " | postado dia " + str(self.date)
~~~

Com modelo criado vamos fazer a migração para o banco de dados. Nessa etapa o Django cuidará de criar as tabelas do nosso projeto no bando de dados para que não seja necessário nos preocupar em implementar comandos SQL. Qualquer alteração que fizermos nos nosso modelos o Django cuidará disso para nós.


### Migrate

Para fazer a migração do banco de dados digitamos no terminal o comando

~~~
py manage.py migrate
~~~
Após a execução do comando veja que aparecerá o bando de dados, arquivo`db.sqlite3`, no diretório do projeto criado pelo Django.  Ao abrirmos esses banco de dados veremos as tabelas que criadas pelo Django. Para que as tabelas dos nossos modelos sejam criadas digitamos oa comando

~~~
py manage.py makemigrations
~~~

Após a execução do comando veja que aparecerá 

~~~
Migrations for 'posts':
  posts\migrations\0001_initial.py
    - Create model Posts
~~~
Essa mensagem significa que e a tabela foi criada no banco de dados. Abra o banco de dados novamente que veremos a tabela criada sem que tenhamos utilizado comandos SQL.

**Observação**: abra o arquivo `settings.py` e verá um trecho de código com as configurações do banco de dados com um dictionary. O nome do banco de dados pode ser modificado caso você queira.

~~~python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
~~~
Agora que temos nossa aplicação `posts` criada e o nosso banco de dados, vamos agora criar um usuário para que possamos acessar nosso administrador de site onde podemos criar nossas postagens, editar e deletar para salvar no banco de dados. 

Esse site administrador já foi criado pelo Django, então o que precisamos fazer é so acessá-lo!


## Administrador de site

Para criar um super usuário digitamos no terminal 

~~~
py manage.py createsuperuser
~~~

Então criamos um usuário e senha para acessar o administrador. 

Após criar o usuário e senha vamos inicializar o servidor para acessar o administrador de site. Digitamos no terminal o comando

~~~
py manage.py runserver
~~~

Vamos agora abrir o navegador e acessar http://127.0.0.1:8000/admin

E digitamos o usuário e senha para fazer login.

Ao acessarmos está disponível as tabelas de grupos e usuários no qual podemos adicionar novos usuários e grupos, como mostra a figura a seguir

<img src="https://docentes.univasf.edu.br/carlos.freitas/imagens_markdown/admin_django_1.png" />

Para que a tabela de postagens esteja disponível na administração do site precisamos registrá-la o modelo. Abrimos o arquivo `admin.py` e digitamos o código

~~~python
from .models import Posts
admin.site.register(Posts)
~~~

<img src="https://docentes.univasf.edu.br/carlos.freitas/imagens_markdown/admin_django_2.png" />

Agora podemos adicionar, editar e deletar as postagens do nosso blog. Assim, temos nosso administrador de postagens do blog pronto! 

O que temos que fazer agora e criar as páginas HTML para que os visitantes possam visualizar nossas postagens. Para fazer isto criaremos as nossas views que são métodos que retornam repostas de solicitações HTTP. As views são criadas no arquivo `views.py` e configuraremos as urls no arquivo `urls.py`. Faremos isso no próximo tutorial.
