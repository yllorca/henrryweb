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

## Custom tag de nuestro proyecto blog

1. Comment_count

`````
@register.simple_tag
def comment_count(post_id):
    post = Post.objects.get(id=post_id)
    return post.comments.filter(active=True).count()
`````

La función hace uso de la relación de uno a muchos existente entre el modelo "Post" y "Comment" para obtener una instancia del modelo "Post" que coincida con el identificador proporcionado (post_id). Luego, se filtran solo los comentarios activos (campo "active" es True) y se cuenta su número mediante el método "count()". Finalmente, se retorna el resultado.

Ahora podemos usar el tag en nuestro template de la siguiente manera:

En nuestro archivo home-content.html agregamos lo siguiente

`````
{% comment_count post.id %}
`````

La primera parte es el nombre de nuestro tag y la segunda parte es el
arg del post.id que hay que pasarle para que nos retorne el total de comentarios de ese post unicamente.

2. show_used_tags

`````
@register.inclusion_tag('snippets/used_tags.html')
def show_used_tags(count=20):
    used_tags = Post.tags.all()[:count]
    print(type(used_tags))
    return {'used_tags': used_tags}
`````

La función show_used_tags es un inclusion_tag de Django, lo que significa que permite incluir un fragmento de HTML en una plantilla de Django. Este tag específico se utiliza para mostrar una lista de las count etiquetas más utilizadas en los posts de la aplicación.

La función toma un argumento opcional count, que especifica el número de etiquetas que se deben mostrar. Si no se proporciona un valor, se usará el valor predeterminado de 20.

La función obtiene una lista de las etiquetas utilizadas en los posts a través del atributo tags en el modelo Post. Este atributo es un TaggableManager, que permite asignar etiquetas a los posts. La función obtiene las count primeras etiquetas de la lista de etiquetas y las asigna a la variable used_tags.

Finalmente, la función devuelve un diccionario con una clave 'used_tags' que contiene la lista de etiquetas utilizadas. Esta información se utiliza en la plantilla snippets/used_tags.html para mostrar las etiquetas en la página web.

3. show_latest_posts

`````
@register.inclusion_tag('snippets/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
``````

La función show_latest_posts es una función de inclusion tag de Django, que se utiliza para incluir un fragmento de HTML en otra página o plantilla. La función toma como argumento un conteo (count) que especifica cuántos de los últimos posts deben ser mostrados.

Dentro de la función, primero se obtiene un queryset con los últimos count posts publicados, usando el manager published y ordenándolos por la fecha de publicación (-publish). Luego, el queryset se pasa a un diccionario como una variable llamada latest_posts.

Finalmente, la función devuelve el diccionario, que luego se utiliza en el archivo snippets/latest_posts.html para mostrar los últimos posts en la plantilla.

4. show_most_commented_posts


`````
@register.inclusion_tag('snippets/most_commented_posts.html')
def show_most_commented_posts(count=5):
    most_commented_posts = Post.published.filter(comments__active=True).annotate(
               total_comments=Count('comments')
           ).order_by('-total_comments')[:count]
    return {'most_commented_posts': most_commented_posts}
`````

Esta función es un inclusion_tag personalizado en Django que se utiliza para mostrar los "count" número de publicaciones más comentadas en el blog. La función hace lo siguiente:

Obtiene los objetos "Post" publicados y filtra solo aquellos que tengan comentarios activos.

Utiliza el método "annotate" para agregar una nueva columna "total_comments" al queryset, que es la suma de los comentarios activos para cada publicación.

Ordena el queryset por "total_comments" en orden descendente y selecciona los "count" primeros elementos.

Finalmente, retorna un diccionario con la clave "most_commented_posts" que contiene el queryset seleccionado. Este diccionario será utilizado para renderizar el archivo "snippets/most_commented_posts.html" que se especifica en la decoración "@register.inclusion_tag".

¡Buen trabajo, Henrry!