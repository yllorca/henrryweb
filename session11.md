## Como crear Custom template Tag

Los custom template tags son una herramienta de Django que permite extender las capacidades de los templates de Django. Se trata de una forma de encapsular código personalizado en una forma que pueda ser reutilizada fácilmente en diferentes partes de una aplicación. Los custom template tags pueden ser usados para hacer una amplia variedad de tareas, como procesar información compleja, mostrar información de forma condicional, o modificar el contenido de una plantilla antes de que sea renderizada.

Un custom template tag es una función Python que devuelve algo que puede ser renderizado en una plantilla HTML. Estos custom tags pueden ser invocados desde una plantilla usando la sintaxis especial de Django. Por ejemplo, si tienes un custom template tag llamado "current_time", podrías invocarlo en una plantilla de la siguiente manera:

Algunos ejemplos de tareas que se pueden realizar con custom template tags incluyen:

- Mostrar información de una base de datos: Puedes crear un custom template tag que recupere y muestre información de una base de datos en tus plantillas.

- Realizar cálculos: Puedes crear un custom template tag que realice cálculos complejos y muestre el resultado en tus plantillas.

- Controlar el flujo de la aplicación: Puedes crear un custom template tag que controle el flujo de la aplicación y muestre diferentes contenidos en función de ciertas condiciones.

- Mostrar información en un formato específico: Puedes crear un custom template tag que formatee y muestre información en un formato específico en tus plantillas.

Hay dos tipos de custom template tags: simple_tag y inclusion_tag.

Un simple_tag es una función que toma argumentos y devuelve una cadena que se inserta en la plantilla en el lugar donde se invocó el tag. Un simple_tag es útil cuando se necesita una pequeña cantidad de información o lógica en una plantilla, pero no se necesita acceder a un contexto más amplio o a otras plantillas.

Un inclusion_tag, por otro lado, es una función que toma argumentos y devuelve un diccionario con un contexto para ser utilizado por una plantilla. La plantilla especificada en el inclusion_tag se renderiza con el contexto proporcionado y el resultado se inserta en la plantilla en el lugar donde se invocó el tag. Un inclusion_tag es útil cuando se necesita un contexto más amplio o se desea renderizar varias plantillas en un solo tag.

En resumen, la principal diferencia entre un simple_tag y un inclusion_tag es el tipo de resultado que devuelven y el tipo de tareas que se pueden realizar. Un simple_tag es adecuado para tareas simples que devuelven una cadena, mientras que un inclusion_tag es adecuado para tareas más complejas que requieren un contexto más amplio y la renderización de varias plantillas.

## Configuración de los templates tag

1. Dentro de nuestra app blog creamos directorio que se va llamar templatetags.
2. Dentro del directorio creamos un archivo vacio con el nombre __init__.py. Este archivo le indica a django que el directrio va ser un paquete de python.
3. Creamos un archivo blog_tags.py


Agregamos a nuestro blog_tags.py el siguiente código:

`````
from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()
``````

Este código es un ejemplo de un custom template tag en Django.

El objetivo de este tag es retornar la cantidad de publicaciones (posts) que existen en la base de datos.

Aquí hay una explicación detallada del código:

- from django import template: Importa la librería de plantilla de Django.

- from ..models import Post: Importa el modelo de publicación (Post) desde otro lugar en la aplicación.

- register = template.Library(): Crea una instancia de la biblioteca de plantilla que se usará para registrar el custom template tag.

- @register.simple_tag: Decorador que indica que esta función es un custom template tag simple.

- def total_posts():: Define una función que retorna la cantidad de publicaciones (posts) en la base de datos.

- return Post.published.count(): Retorna la cantidad de publicaciones (posts) que tienen el estado "publicado" (published). Esto se hace utilizando el manager "published" que ha sido definido en el modelo de publicación (Post).

Ahora para poder usar nuestro tag agregamos el siguiente código a nuestro
html en la parte superior

````
{% load blog_tags %}
````

Por ejemplo ahora puedes ocupar el tag en tu template:

`````
{% total_posts %}
`````

Ahora vamos a crear otro tag para mostrar los ul
