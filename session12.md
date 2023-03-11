## Implementar la Busqueda en nuestro blog

Lo primero que debemos hacer definir un formulario en nuestro arhivo
forms.py con un campo de busqueda.

`````
class SearchForm(forms.Form):
    query = forms.CharField()
`````

La función SearchForm es una clase de un formulario de Django, la cual define un formulario de búsqueda con un único campo de entrada de texto llamado "query". Este formulario permitirá a los usuarios ingresar una consulta de búsqueda en el sitio web.

2. Creamos nuestra función post_search en nuestro archivo views.py de nuestra app blog que se encargara de la lógica de busqueda.

`````
def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gt=0.3).order_by('-similarity')
    return render(request,
                  'search.html',
                  {'form': form,
                   'query': query,
                   'results': results})
`````

Esta función es una vista en Django que se encarga de realizar una búsqueda de publicaciones en un blog. La búsqueda se realiza mediante un formulario, que es instanciado como SearchForm. La vista comprueba si en la petición GET existe un parámetro query que representa la consulta que el usuario quiere realizar. Si existe, se crea una instancia de SearchForm con el valor de query.

Luego, la vista comprueba si el formulario es válido. Si lo es, se almacena en la variable query el valor de la consulta. Luego, se realiza una consulta en la base de datos utilizando el modelo Post y el método annotate, que permite agregar un campo virtual a la consulta. En este caso, se agrega un campo similarity que almacena el resultado de la similitud trigramática entre el título de cada publicación y la consulta del usuario. Finalmente, se filtran las publicaciones con una similitud mayor a 0.3 y se ordenan por el valor de la similitud en orden descendente.

Por último, la vista renderiza una plantilla search.html que es enviada a la respuesta HTTP con los siguientes contextos: el formulario form, la consulta query y los resultados de la búsqueda results.

`````
<section id="content">
  <div class="content-wrap">

    <div class="container clearfix">
    {% if query %}
    <h1>Posts containing "{{ query }}"</h1>
    <h3>
      {% with results.count as total_results %}
          Found {{ total_results }} result{{ total_results|pluralize }}
      {% endwith %}
    </h3>
    {% for post in results %}
        <h4><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h4>
        {{ post.body|truncatewords:5 }}
    {% empty %}
      <p>There are no results for your query.</p>
    {% endfor %}
    <p><a href="{% url "blog:post_search" %}">Search again</a></p>
  {% else %}
    <h1>Search for posts</h1>
    <form action="." method="get">
      {{ form.as_p }}
      <input type="submit" value="Search">
    </form>
  {% endif %}
  </div>

  </div>
  </section>
  `````

Agregamos este fragmento de código a nuestro arhivo search-content.html
que hay que crear previamente del de la carpeta templates de nuestra app blog

Este código corresponde a una plantilla HTML en Django que utiliza el lenguaje de template de Django para mostrar una página de búsqueda de publicaciones. La plantilla muestra un formulario de búsqueda si no se ha realizado una búsqueda previamente, y los resultados de la búsqueda si se ha realizado una búsqueda previamente.

El formulario de búsqueda es un formulario de Django que se renderiza utilizando el método form.as_p que genera una representación en HTML de los campos del formulario. Al hacer submit en el formulario, se envía una solicitud GET con la consulta de búsqueda.

En el caso de que se haya realizado una búsqueda previamente, se muestra un encabezado con el término de búsqueda y el número de resultados encontrados. Luego se itera sobre los resultados de la búsqueda, y se muestra un título y una descripción de cada publicación. Si no se encontraron resultados para la búsqueda, se muestra un mensaje correspondiente.

Por último, se ofrece un enlace para realizar una nueva búsqueda.

Y debemos modificar nuestro archivo header-global.html para poder
agregar esta funcionalidad a la busqueda global en el sitio.

`````
<form class="top-search-form" action="{% url 'blog:post_search' %}" method="get">
    <input type="text" name="query" class="form-control" value="{% if query %} {{ query }} {% endif %}" placeholder="Type and hit enter..." autocomplete="off">
</form>
`````

¡Buen trabajo, Henrry!
