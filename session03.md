## Creear una Aplicacion de Django

Una aplicación en Django es un componente reutilizable que se compone de un conjunto de modelos, vistas, plantillas y archivos de configuración que trabajan juntos para realizar una tarea específica en un proyecto Django.

La composición de una aplicación en Django incluye los siguientes componentes:

- Modelos: describen la estructura de los datos que se almacenarán en la base de datos, incluyendo el tipo de datos y las relaciones con otros modelos.

- Vistas: son las que controlan la lógica de negocio y la interacción con los modelos, procesando las solicitudes HTTP y devolviendo respuestas.

- Plantillas: son archivos HTML que se utilizan para presentar la información a los usuarios.

- Archivos de configuración: incluyen archivos como urls.py, que describen las URLs que la aplicación manejará, y apps.py, que contiene la configuración general de la aplicación.

Para crear una aplicación debemos ejecutar

`````
python manage.py startapp blog
`````

Para poder usar nuestra aplicación en django es necesario que la activemos agregandola al apartado INSTALLED_APPS de nuestro archivo settings.py. Ejemplo

`````
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog', <= aqui lo agregue
]
`````

## Definir Modelos en Django

En Django, se define un modelo en un archivo models.py en el interior de una aplicación. El modelo representa nuestra tabla en la base de datos.

Aquí hay un ejemplo de cómo definir un modelo llamado Post en para nuestra App Blog:

`````
from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 

class Post(models.Model): 
    STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    ) 
    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250,  
                            unique_for_date='publish') 
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='blog_posts') 
    body = models.TextField() 
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,  
                              choices=STATUS_CHOICES, 
                              default='draft') 

    class Meta: 
        ordering = ('-publish',) 

    def __str__(self): 
        return self.title
`````

El modelo "Post" define una tabla de datos en la base de datos con los siguientes atributos y comportamientos:

- title: un campo de texto con un máximo de 250 caracteres.
- slug: un campo de texto con un máximo de 250 caracteres, único por fecha de publicación.
- author: una clave foránea al modelo de usuario de Django, que representa al autor del post.
- body: un campo de texto largo para el cuerpo del post.
- publish: un campo de fecha y hora para la fecha de publicación del post.
- created: un campo de fecha y hora que se establece automáticamente en la fecha y hora actual cuando se crea el post.
- updated: un campo de fecha y hora que se establece automáticamente en la fecha y hora actual cada vez que se guarda el post.
- status: un campo de texto con un máximo de 10 caracteres que representa el estado del post, con opciones "draft" o "published".
- Meta: una clase interna que proporciona información adicional para el modelo, en este caso establece que los posts se deben ordenar por fecha de publicación en orden descendente.
- str: un método que define cómo se representa el objeto en una cadena, en este caso, el título del post.

Django nos proporciona diferentes tipos de campos que podemos utilizar en nuestros modelos. Puedes revisar la documentación oficial haciendo clic en el siguiente link

[Model field reference](https://docs.djangoproject.com/en/3.2/ref/models/fields/)

Es importante tener en cuenta que, después de definir los modelos, se deben realizar migraciones para que Django cree las tablas correspondientes en la base de datos. Esto se puede hacer ejecutando los siguientes comandos en la línea de comando:

`````
python manage.py makemigrations
python manage.py migrate
``````

Después de ejecutar makemigrations django va crear de forma automatica un archivo 0001_initial.py en la carpeta de migrations de tu app. En este archivo se expecifican las dependencias con otras migraciones y los campos necesarios para crear la tabla con los datos expecificados en el modelo.

La ORM (Object-Relational Mapping) es una tecnología que permite trabajar con bases de datos en un lenguaje de programación de manera más natural, utilizando objetos en lugar de sentencias SQL.

Django ORM es el sistema de mapeo de objetos de relación de Django que proporciona una interfaz para trabajar con bases de datos en Django. Con Django ORM, puedes definir tus modelos en Python y luego crear, consultar, actualizar y eliminar registros en la base de datos sin escribir ninguna sentencia SQL. Django ORM se encarga de traducir tus operaciones de modelo a sentencias SQL y ejecutarlas en la base de datos en tu nombre.

Opcional: Si queremos visualizar todo el código sql que se ejecuta con la migración ejecutamos:

`````
python manage.py sqlmigrate blog 0001
`````

Este comando nos retornara en consola el codigo sql que se utilizo para crear la tabla en la BD.

`````
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(250) NOT NULL, "slug" varchar(250) NOT NULL, "body" text NOT NULL, "publish" datetime NOT NULL, "created" datetime NOT NULL, "updated" datetime NOT NULL, "status" varchar(10) NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
``````

