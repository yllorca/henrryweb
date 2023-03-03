## Implementar el Etiquetado de artículos en el blog

django-taggit es una biblioteca de etiquetado para Django. Permite a los usuarios asignar etiquetas a los objetos en una aplicación Django, de manera similar a cómo se asignan etiquetas a las publicaciones en blogs o fotos en sitios web de compartición de fotos. La biblioteca proporciona una forma fácil de agregar y gestionar etiquetas en una aplicación Django, sin la necesidad de escribir una lógica compleja para ello. Es una herramienta muy útil para añadir una funcionalidad de etiquetado a una aplicación Django de manera rápida y sencilla.

Para instalar django-taggit debemos tener activo nuestro entorno virtual
y ejecutamos:

`````
pip install django-taggit
`````

Agregamos el biblioteca a nuestro archivo INSTALL_APP de django

Después en nuestro archivo models.py de nuestro app blog agregamos
el manager personalizado de nuestro biblioteca taggit

`````
from taggit.managers import TaggableManager # hay que importalos
....
tags = TaggableManager() # manager de la libreria taggit
`````

Ahora debemos correr el makemigrations y el migration para agregar
las tablas respectivas a la BD.

Debo modificar mi vista post_list para agregar el la funcionalidad del tag:

La vista quedaria asi:

`````
def post_list(request, tag_slug=None):
    posts = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 1) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'home.html', {'page': page, 'posts': posts, 'tag': tag})
`````

Este código está filtrando los post publicados que tienen una etiqueta específica. La variable tag_slug representa el identificador único de la etiqueta y se utiliza para buscar la etiqueta correspondiente en la base de datos. Si tag_slug es especificado, se utiliza para filtrar los post que tienen esa etiqueta. La función get_object_or_404 es una función de ayuda que se utiliza para obtener un objeto de la base de datos o retornar un error 404 si el objeto no existe.

Una vez que se ha recuperado la etiqueta, se filtran los post que tienen esa etiqueta usando object_list.filter(tags__in=[tag]). El argumento tags__in indica que se está filtrando por una lista de etiquetas y [tag] es la lista que contiene la etiqueta específica que se está buscando.

Después de filtrar los post, la variable posts contiene una lista de post que tienen la etiqueta especificada.

Debemos agregar una url para poder filtrar los post a partir de las tags.

Abrimos nuestro archivo urls.py y agrega la siguiente url a nuestra vista
post_list

`````
path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
`````

Después en nuestro template agregamos el siguiente for para traernos
todas las tags relacionadas con el post.tag

`````
<li><i class="icon-folder-open"></i>
                                    {% for tag in post.tags.all %}
                                        <a href="{% url "blog:post_list_by_tag" tag.slug %}">
                                        {{ tag.name }}
                                        </a>
                                        {% if not forloop.last %}, {% endif %}
                                        {% empty %}
                                        Sin tags
                                    {% endfor %}
                                </li>
                                `````

Este fragmento de código muestra una lista de etiquetas asociadas a un post en particular. La lista se genera a partir de la relación de etiquetas de un post y se muestra en una lista HTML.

El código utiliza un bucle for para iterar sobre las etiquetas del post. Por cada etiqueta, se muestra un enlace a la página de listado de posts filtrados por esa etiqueta, utilizando la URL que se define en la vista post_list_by_tag y el slug de la etiqueta como argumento.

El enlace muestra el nombre de la etiqueta. Si hay más de una etiqueta, se separan con una coma. Si no hay ninguna etiqueta asociada al post, se muestra el texto "Sin tags".

El fragmento de código utiliza también la variable forloop para controlar si se está en el último elemento del bucle y evitar mostrar una coma después de la última etiqueta.

En la vista post_detail, puedes obtener los tags asociados a un post de la siguiente manera:

`````
post_tags = post.tags.all()
`````

Luego puedes pasar la lista de tags a la plantilla como un contexto adicional. Por ejemplo:

`````
return render(request,
                  'post-detail.html',
                  {'post': post,
                   'comments': comments,
                    'new_comment': new_comment,
                    'comment_form': comment_form,
                    'post_tags': post_tags,
                    })
``````

En la plantilla, puedes acceder a los tags de un post de la siguiente manera:

`````
{% for tag in post_tags %}
<a href="{% url "blog:post_list_by_tag" tag.slug %}">
{{ tag.name }}
</a>
{% if not forloop.last %}, {% endif %}
{% empty %}
    Sin tags
{% endfor %}
`````

¡Buen trabajo, Henrry!