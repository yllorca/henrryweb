## Paginación en Django


Para implementar la paginación en Django, se puede usar el built-in Paginator de Django.

El built-in Paginator de Django es una clase que permite dividir una lista de objetos en varias páginas. Cada página tendrá un número limitado de objetos. Es una forma sencilla y eficiente de realizar la paginación para nuestro blog.

La clase Paginator se encuentra en el módulo django.core.paginator y puede ser utilizada para dividir cualquier lista de objetos en páginas. 

Al utilizarla, es necesario especificar el número de objetos que se desean en cada página y la lista de objetos que se desean paginar. La clase Paginator devolverá un objeto de la clase Page que permitirá acceder a las diferentes páginas y a los objetos que se encuentran en cada una.

Modificamos nuestra vista post_list con el siguiente código

``````
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'home.html', {'page': page, 'posts': posts})
`````

Este código implementa una paginación en una vista de Django, específicamente para el modelo Post.

Se importa el built-in Paginator de Django y se crea un objeto paginator con dos argumentos: el queryset posts y el número de objetos por página (en este caso, 3).

Luego, se obtiene la página actual de la petición GET y se utiliza la función page del objeto paginator para obtener los objetos correspondientes a esa página.

En caso de que la página no sea un entero, se entrega la primera página. Y en caso de que la página esté fuera de rango, se entrega la última página de resultados.

Finalmente, se envía la página actual y los objetos de la página actual a la plantilla home.html y se renderiza la respuesta.

Ahora creamos en nuestro template la paginación 


`````
<div class="d-flex justify-content-between mt-5">
    {% if page.has_previous %}
    <a href="?page={{ page.previous_page_number }}" class="btn btn-outline-secondary">&larr; Previous</a>
    {% endif %}
    <span class="current">
        Page {{ page.number }} of {{ page.paginator.num_pages }}
    </span>
    {% if page.has_next %}
    <a href="?page={{ page.next_page_number }}" class="btn btn-outline-dark">Newer &rarr;</a>
    {% endif %}
</div>
``````

Después agregamos a nuestra template home-content.html

`````
{% include "snippets/pagination.html" with page=posts %}
`````

Esta línea de código es una directiva de inclusion de plantillas en Django, que incluye el contenido de una plantilla llamada "snippets/pagination.html" en la plantilla actual. La directiva "with" permite pasar una variable llamada "page" con el valor de "posts" como argumento a la plantilla incluida.

## Agregando Img a nuestro modelos post

Para agregar una imagen a nuestro modelo debemos agregar un nuevo campo de tipo FileField.


`````
photo = models.FileField(upload_to=upload_file, editable=True, null=True, blank=True) 
``````

Esta linea de código es una declaración de un campo en el modelo Post en Django. Este campo es un FileField, lo que significa que es un campo que almacenará un archivo en el sistema de archivos.

El argumento upload_to es una función que especifica dónde se guardará el archivo subido. En este caso, se está utilizando la función upload_file.

El argumento editable especifica si este campo es editable o no. En este caso, se establece en True, lo que significa que se puede editar.

Los argumentos null y blank especifican si este campo puede ser nulo o estar en blanco. En este caso, ambos se establecen en True, lo que significa que el campo puede ser nulo o estar en blanco.

Creamos nuestra funcion auxiliar upload_file en la parte super del archivo models.py

`````
def upload_file(instance, filename):
    #obtengo el nombre del archivo y su extensión
    filebase, extension = filename.split(".")[-2:]
    ##se arma la ruta
    return "posts/{}.{}".format(str(uuid.uuid4())[:8], extension)
`````

Esta función upload_file es una función de "upload_to" personalizada utilizada en el campo photo del modelo Post. La función se utiliza para determinar la ruta de guardado para un archivo en particular.

La función toma dos argumentos: instance y filename. Instance representa la instancia actual del objeto del modelo Post. Filename representa el nombre original del archivo.

La función divide el nombre del archivo y su extensión utilizando la función split y luego arma la ruta de guardado para el archivo utilizando un identificador único generado por la función uuid.uuid4 (). La ruta de guardado se forma como "posts/{identificador_unico}.{extension}" y se devuelve como resultado de la función.

Esta función asegura que cada archivo tenga una ruta única y no se sobreescriba con archivos con el mismo nombre.

¡Buen trabajo, Henrry!



