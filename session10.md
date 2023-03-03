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

## Mostrar articulos similares

Ahora que hemos implementado el etiquetado de las publicaciones de nuestro blog, podemos hacer muchas cosas interesantes con ellas. Usando etiquetas, podemos clasificar muy bien las publicaciones de nuestro blog. 

Las publicaciones sobre temas similares tendrán varias etiquetas en común. 

Construiremos una funcionalidad para mostrar publicaciones similares por la cantidad de etiquetas que comparten. De esta forma, cuando un usuario lee una publicación, podemos sugerirle que lea otras publicaciones relacionadas. 

Para recuperar publicaciones similares para una publicación específica, debemos realizar los siguientes pasos:

1. Recuperar todas las etiquetas de la publicación actual

2. Vamos a obtener todas las publicaciones que se etiquetan con cualquiera de esas etiquetas

3. Vamos a exluir de la publicación actual de esa lista para evitar recomendar la misma publicación

4. Ordene los resultados por el número de etiquetas compartidas con la publicación actual.

5. En caso de dos o más publicaciones con el mismo número de etiquetas, recomendar la publicación más reciente

6. Limitar la consulta al número de publicaciones que queremos recomendar 

Estos pasos se traducen en un QuerySet complejo que incluiremos en nuestra vista post_detail

Importamos en nuestro view

`````
from django.db.models import Count
`````

El import Count de django.db.models es una clase que se utiliza para agregar una funcionalidad de conteo a una consulta de base de datos en Django. Esta clase permite contar el número de ocurrencias de un objeto o un campo específico en una consulta de base de datos y retornar el resultado en una consulta de base de datos. Por ejemplo, podrías usar la clase Count para contar el número de comentarios que tienen una publicación y retornar el resultado en una consulta. Esto te permite realizar consultas más complejas y obtener resultados más precisos y detallados.

Existen muchas otras funciones de agregación en Django. Algunas de las más comunes incluyen:

- Sum: Calcula la suma de un campo numérico.
- Avg: Calcula el promedio de un campo numérico.
- Min: Calcula el valor mínimo de un campo numérico.
- Max: Calcula el valor máximo de un campo numérico.
- Stddev: Calcula la desviación estándar de un campo numérico.
- Variance: Calcula la varianza de un campo numérico.
- F: Agrupa y combina varias funciones de agregación en una sola consulta.

Todas estas funciones se utilizan en combinación con la función .aggregate() para realizar consultas complejas.

Nuestro lógica para filtrar los publicaciones relacionas seria asi:

`````
    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]
`````

Este fragmento de código busca publicaciones similares a la publicación actual. Aquí está lo que hace cada línea de código:

1. post_tags_ids = post.tags.values_list('id', flat=True): obtiene una lista de los IDs de los tags asociados a la publicación actual. La función values_list devuelve una lista de valores de un campo específico en lugar de objetos completos. La opción flat=True indica que se devuelve una lista plana en lugar de una lista de tuplas.

2. similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id): filtra las publicaciones que tienen alguno de los mismos tags que la publicación actual y excluye la publicación actual. El filtro tags__in se aplica a los tags asociados a cada publicación y devuelve las publicaciones que tienen al menos uno de los IDs de tag en la lista post_tags_ids.

3. similar_posts = similar_posts.annotate(same_tags=Count('tags')): agrega una nueva columna llamada same_tags que contiene el número de tags que tienen en común cada publicación similar y la publicación actual. La función Count cuenta el número de tags asociados con cada publicación similar.

4. similar_posts.order_by('-same_tags','-publish')[:4]: ordena las publicaciones similares por el número de tags que tienen en común con la publicación actual y la fecha de publicación, y luego selecciona solo las 4 primeras publicaciones. La opción -same_tags indica que las publicaciones con más tags en común deben aparecer primero en la lista, y la opción -publish indica que las publicaciones más recientes deben aparecer primero en la lista si dos publicaciones tienen el mismo número de tags en común.






¡Buen trabajo, Henrry!