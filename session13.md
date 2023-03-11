## Implementar un sitemap para blog

Un sitemap es un archivo XML que contiene una lista de las páginas web de un sitio y información adicional acerca de esas páginas, como la frecuencia con la que se actualizan y la importancia relativa de cada página. Los sitemaps son utilizados por los motores de búsqueda para indexar de manera más efectiva los sitios web y para ayudar a los webmasters a informar a los motores de búsqueda sobre las páginas que deben ser indexadas. Utilizando un sitemap, los webmasters pueden asegurarse de que todas las páginas de su sitio sean indexadas por los motores de búsqueda y, por lo tanto, sean más fácilmente encontrables por los usuarios.

Django tiene un framework de sitemap incorporado en el paquete django.contrib.sitemaps. Este framework permite generar automáticamente un sitemap para tu sitio web, que puede ser enviado a los motores de búsqueda para mejorar la indexación de tus páginas. Con el framework de sitemap de Django, puedes especificar qué URLs deben incluirse en el sitemap y cuánta frecuencia deben actualizarse.

Para activar el sitemap en nuestro proyecto es necesario agregar
al los INSTALLED_APPS django.contrib.sites y django.contrib.sitemaps. Ademas el bloque de INSTALLED_APPS debemos agregregar SITE_ID = 1.

SITE_ID = 1 es una línea de configuración en el archivo settings.py de una aplicación Django. Especifica el identificador (ID) del sitio que se está utilizando en el proyecto.

En Django, puede tener varios sitios en un solo proyecto. Cada sitio tiene una dirección URL única y una configuración diferente. La ID del sitio se utiliza para identificar el sitio actual que se está utilizando en la aplicación y se refiere a la instancia del modelo Site que representa el sitio actual.

Ahora debemos correr las migraciones ejecutando python manage.py migrate para que se creen las tablas correspondiente al dominio.

Ahora creamos dentro de nuestro app blog un archivo sitemap.py

Agregamos el siguiente código a nuestro archivo sitemap.py

````
from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
`````

El código crea una clase llamada PostSitemap que hereda de la clase Sitemap de Django. La clase PostSitemap es una clase que representa un mapa del sitio para un modelo específico de la aplicación, en este caso, el modelo Post.

Los atributos changefreq y priority establecen la frecuencia de cambios y la prioridad de los posts dentro del sitemap.

El método items devuelve un queryset de todos los posts publicados.

El método lastmod devuelve la fecha de actualización más reciente para cada objeto post. Esta fecha se utiliza para indicar cuándo un post fue modificado por última vez y se incluirá en el archivo XML del sitemap para proporcionar información a los motores de búsqueda.

Finalmente debemos agregar el sitemap a nuestro archivo url.py principal de proyecto

`````
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
`````

Estas líneas de código están importando la vista sitemap de django.contrib.sitemaps.views y el objeto PostSitemap de la clase PostSitemap en el módulo blog.sitemaps.

Luego, se define un diccionario sitemaps con una clave 'posts' y como valor el objeto PostSitemap. Este diccionario contiene la información necesaria para crear el sitemap de los posts.

Por último, se está utilizando la función path de django.urls para agregar una URL al proyecto que llama a la vista sitemap, pasándole el diccionario sitemaps como argumento. La URL se identifica con el nombre 'django.contrib.sitemaps.views.sitemap'.

Ahora si visitamos la url http://127.0.0.1:8000/sitemap.xml visualizamos nuestro sitemap.xml

Por defecto cuando se activa los dominios en django se crea http://example.com/.

Para cambiar este dominio debemos ingresar a nuestro admin e ir a la sección de site.

Ahora nuestro sitemap se veria con las url validas.

`````
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
<url>
<loc>http://127.0.0.1:8000/2023/3/5/bienvenido-a-chile/</loc>
<lastmod>2023-03-05</lastmod>
<changefreq>weekly</changefreq>
<priority>0.9</priority>
</url>
<url>
<loc>http://127.0.0.1:8000/2023/3/4/bienvenidos-a-mi-primer-post-del-blog/</loc>
<lastmod>2023-03-05</lastmod>
<changefreq>weekly</changefreq>
<priority>0.9</priority>
</url>
</urlset>
`````

¡Buen trabajo, Henrry!