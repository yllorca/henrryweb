## Implementar los Feed para nuestro blog

Un feed es muy util para un blog porque permite compartir las últimas publicaciones en un formato estándar, como RSS o Atom, que puede ser leído por una variedad de aplicaciones, incluidas las agregadoras de noticias y los lectores de feeds. Un feed permite a los usuarios suscribirse a un blog y recibir notificaciones automáticas de las últimas publicaciones. Esto es útil para mantenerse al tanto de los últimos contenidos de un blog sin tener que visitarlo constantemente.

Afortunadamente django ya viene un framework de feed incorporado llamado Django Feeds.

La implementación es muy similar a del sitemap creada en la session13.

Creamos un archivo feeds.py dentro de nuestro app Blog. El archivo contiene el siguiente código.

`````
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
`````

Estas líneas de código crean una clase LatestPostsFeed que hereda de la clase Feed de Django. La clase LatestPostsFeed define los detalles de un feed de noticias, como el título, el enlace y la descripción del feed. Además, también define los elementos que se incluirán en el feed (método items) y cómo se mostrarán cada uno de estos elementos (métodos item_title y item_description).

El método items devuelve los últimos 5 posts publicados de la tabla de publicaciones. El método item_title devuelve el título de cada publicación y el método item_description devuelve una descripción truncada de la publicación con solo 30 palabras.

Ahora debemos agregar agregar nuestro feed a las url.py de nuestro app blog.

`````
from .feeds import LatestPostsFeed
...
path('feed/', LatestPostsFeed(), name='post_feed'),
`````

Ahora como paso final agregamos un enlace a nuestro feed para cada árticulo publicado en nuesto blog.

Para eso abrimos nuestro archivo post-single-content.html

`````
<a href="{% url 'blog:post_feed' %}" class="social-icon si-borderless si-rss">
    <i class="icon-rss"></i>
    <i class="icon-rss"></i>
</a>
`````

Puedes instalar un plugin para chrome de rss suscription para probar los feed.

¡Buen trabajo, Henrry!


