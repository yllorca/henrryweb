## Los Manager en Django

Los managers en Django son objetos que se utilizan para gestionar los objetos de un modelo en la base de datos. Los managers se encargan de realizar operaciones en la base de datos, como filtrar, ordenar y crear objetos.

Un modelo en Django puede tener uno o más managers. El manager por defecto se llama objects, y se puede acceder a él usando el nombre del modelo seguido de .objects. Por ejemplo, si tiene un modelo llamado Post, puede acceder al manager por defecto usando Post.objects.

Además del manager por defecto, también se pueden crear managers personalizados. Por ejemplo, si desea un manager que devuelva solo los registros de Post que tengan un estado "publicado", puede crear un manager personalizado llamado published:

Los manager se definen en el archivo models.py de tu app.

`````
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")

class Post(models.Model):
    ...
    objects = models.Manager() # Manager por defecto
    published = PublishedManager() # manager personalizado
`````

En este ejemplo, se crea un manager personalizado llamado PublishedManager que hereda de models.Manager y sobreescribe el método get_queryset para devolver solo los registros de Post que tengan un estado "publicado". Luego, se crea una instancia de PublishedManager llamada published y se asigna al modelo Post.

Puede acceder a los managers personalizados de la misma manera que accede al manager por defecto. Por ejemplo, puede acceder a los registros de Post que tengan un estado "publicado" usando Post.published.all().

## Las vistas en Django

Las vistas en Django son funciones o clases que se encargan de gestionar las solicitudes HTTP y devolver las respuestas HTTP. En otras palabras, las vistas son el intermediario entre la parte frontal (el navegador web) y la parte posterior (la base de datos) de su aplicación.

Las vistas reciben una solicitud HTTP y devuelven una respuesta HTTP. La respuesta puede ser una página web, una imagen, un archivo PDF, un JSON o cualquier otro tipo de contenido que desee enviar al navegador.

Hay dos maneras principales de escribir vistas en Django. Estan las vistas basadas en función que son las más simples y las vistas basadas en clases.

En ambos casos, la vista recibe una solicitud HTTP y devuelve una respuesta HTTP. La respuesta se crea usando la función render, que toma la solicitud "el request", el nombre de una plantilla y devuelve una respuesta.

Es importante destacar que las vistas son solo una parte de la arquitectura de Django, es decir, no trabajan solas, se requieren configurar las url y templates para crear una aplicación completa que funcione en el navegador.

## Creación de vistas de lista y detalle

Este es un ejemplo de un archivo views.py en Django. La vista se llama post_list y se encarga de mostrar una lista de publicaciones (posts) en la aplicación.


`````
from django.shortcuts import render

from blog.models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

`````

Aquí está una explicación detallada del código:

- from django.shortcuts import render: Se está importando la función render de la biblioteca de accesorios de Django. La función render se utiliza para generar una respuesta HTTP que incluya una plantilla.

- from blog.models import Post: Se está importando el modelo Post de la aplicación blog. El modelo Post representa las publicaciones en la aplicación.

- def post_list(request):: Esta es la definición de la vista post_list. La vista recibe un argumento request que representa la solicitud HTTP.

- posts = Post.published.all(): Aquí se está obteniendo un QuerySet de todos los objetos Post que tengan un estado "publicado". El manager personalizado published se crea en el modelo Post y se puede acceder a él usando Post.published.

- return render(request, 'blog/post/list.html', {'posts': posts}): Aquí se está devolviendo una respuesta HTTP que incluye una plantilla llamada list.html. La plantilla se encuentra en el directorio blog/post/ y se pasa un contexto que incluye una variable posts que contiene el QuerySet de publicaciones.


### post_detail View

Este es un ejemplo de una vista en Django. La vista se llama post_detail y se encarga de mostrar los detalles de una publicación (post) específica en la aplicación.

`````
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
`````

Aquí está una explicación detallada del código:

- def post_detail(request, year, month, day, post):: Esta es la definición de la vista post_detail. La vista recibe cuatro argumentos adicionales a request, que representan el año, el mes, el día y el identificador único (slug) de la publicación que se desea mostrar.

- post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day): Aquí se está obteniendo un objeto Post que coincida con los criterios especificados. La función get_object_or_404 se importa desde django.shortcuts y se utiliza para obtener un objeto específico de la base de datos o devolver un error 404 si no se encuentra un objeto que coincida con los criterios. En este caso, se está buscando un objeto Post que tenga el identificador único (slug) igual al argumento post, un estado "publicado" y una fecha de publicación que coincida con el año, el mes y el día especificados.

- return render(request, 'blog/post/detail.html', {'post': post}): Aquí se está devolviendo una respuesta HTTP que incluye una plantilla llamada detail.html. La plantilla se encuentra en el directorio blog/post/ y se pasa un contexto que incluye una variable post que contiene el objeto Post que se ha obtenido en el paso 2.

## Agregar url a nuestras vistas

Las URL patterns en Django son una forma de asociar URLs con vistas en una aplicación. Cada URL pattern especifica un patrón de URL y una vista que se encarga de procesar la solicitud HTTP correspondiente.

Todas las url de nuestra app son almacenas en un archivo urls.py que debemos crear dentro de nuestra app.

Por ejemplo, para nuestra vista llamada post_list que muestra una lista de publicaciones en su aplicación. Para asociar una URL con la vista post_list, puede crear una URL pattern que se vea así:

`````
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]
`````

En este ejemplo, se está importando la vista post_list desde el archivo views.py y se está creando una URL pattern que asocia la URL /posts/ con la vista post_list. La URL pattern se agrega a una lista de URL patterns que se encuentra en el archivo urls.py de la aplicación.

Cuando un usuario visita la URL /posts/ en su navegador, Django buscará en la lista de URL patterns y encontrará la URL pattern que coincide con la URL solicitada. Django llamará entonces a la vista asociada (post_list) para procesar la solicitud HTTP.

Aquí está una explicación detallada del código de nuestra url para la vista post_detail:

1. "path('<int:year>/<int:month>/<int:day>/<slug:post>/', ...)": Aquí se está especificando el patrón de URL que se desea asociar con la vista. El patrón incluye cuatro partes que representan el año, el mes, el día y el identificador único (slug) de una publicación. Cada parte se especifica usando una variable entre paréntesis angulares, por ejemplo <int:year> o <slug:post>. Las variables int y slug son tipos de conversión que se utilizan para convertir la parte correspondiente de la URL en un valor de Python que se pueda pasar a la vista.

2. views.post_detail: Aquí se está especificando la vista que se desea asociar con la URL pattern. La vista post_detail se importa desde el archivo views.py de la aplicación.

3. name='post_detail': Aquí se está especificando un nombre para la URL pattern. Este nombre se puede usar en el código para generar URLs dinámicamente en lugar de tener que escribir la URL completa.

La URL pattern se agrega a una lista de URL patterns que se encuentra en el archivo urls.py de la aplicación. Cuando un usuario visita una URL que coincide con el patrón de URL especificado en la URL pattern, Django llamará a la vista post_detail para procesar la solicitud HTTP. La vista post_detail recibirá los valores de año, mes, día y slug de la URL como argumentos y los utilizará para mostrar los detalles de una publicación específica en la aplicación.

¡Buen trabajo, Henrry!
