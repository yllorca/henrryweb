## Implementar los comentarios para nuestro blog

Para poder implementar los comentarios voy a seguir los siguientes passos:

1. Crear un modelo para los comentarios
2. Crear un formulario que valide la data enviada en los comentarios
3. Implementar en la vista la lógica para almacenar los comentarios en la base de datos.
4. Editar nuestro template post-details.html para para visualizar los
comentarios aprobados y el formulario para enviar un nuevo comentario.

Abre el archivo models.py de nuestra app blog y agrega el siguiente código:

`````
class Comment(models.Model): 
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=False) 
 
    class Meta: 
        ordering = ('created',) 
 
    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post)
`````


El modelo Comment representa un comentario de un usuario en un post específico. El modelo tiene los siguientes atributos:

- post: Es una relación ForeignKey con el modelo Post, que representa el post en el que se ha hecho el comentario. La opción on_delete=models.CASCADE significa que si el post asociado con un comentario se elimina, entonces el comentario también será eliminado. La opción related_name='comments' permite acceder a los comentarios de un post a través de la relación de Post hacia Comment.

- name: Nombre del usuario que ha realizado el comentario. Es un campo de tipo CharField con una longitud máxima de 80 caracteres.

- email: Dirección de correo electrónico del usuario que ha realizado el comentario. Es un campo de tipo EmailField.

- body: Contenido del comentario. Es un campo de tipo TextField.

- created: Fecha y hora en la que se creó el comentario. Es un campo de tipo DateTimeField y se establece automáticamente con la fecha y hora actual al crear un nuevo comentario gracias a la opción auto_now_add=True.

- updated: Fecha y hora en la que se actualizó el comentario por última vez. Es un campo de tipo DateTimeField y se actualiza automáticamente cada vez que se guarda una actualización en el comentario gracias a la opción auto_now=True.

- active: Especifica si el comentario está activo o no. Es un campo de tipo BooleanField y su valor predeterminado es True.

La clase Meta dentro del modelo define el orden predeterminado de los objetos de Comment por la fecha de creación. La función __str__ retorna una representación en forma de texto del objeto Comment.

No olvidar ejecutar el makemigrations y el migrate.

## Crear formularios para nuestros modelos

Puedes generar un formulario en Django utilizando la clase forms.Form o forms.ModelForm.

Para crear un formulario a partir de un modelo, puedes utilizar forms.ModelForm y especificar el modelo con el que quieres trabajar. Por ejemplo, si quieres crear un formulario para el modelo Comment que acabas de describir, puedes hacer lo siguiente:

Crea un archivo forms.py dentro de app blog y el contenido de este form seria:

````
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
`````

## Manejo de ModelForms en vistas de django.

Modificamos nuestra vista post_detail de nuestra views.py de al app blog

`````
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  'post-detail.html',
                  {'post': post,
                   'comments': comments,
                    'new_comment': new_comment})
`````

Esta vista, post_detail, es utilizada para mostrar el detalle de un post publicado en particular.

La vista toma 4 argumentos en su URL: year, month, day y post. Con estos argumentos, se obtiene una instancia de Post a través del método get_object_or_404, que busca un objeto en la base de datos con un estado 'published' y una fecha de publicación correspondiente a los años, meses y días especificados en la URL. Si no se encuentra el objeto, se devuelve un error 404.

Luego, la vista obtiene una lista de comentarios activos para el post actual a través de la relación de Comment hacia Post, y filtrándolos por active=True.

Si el método HTTP es POST, se crea una instancia de CommentForm con los datos recibidos en la solicitud. Si el formulario es válido, se crea un objeto Comment pero no se guarda en la base de datos todavía. Luego, se asigna el post actual al comentario y se guarda en la base de datos.

Si el método HTTP es GET, se crea una instancia vacía del formulario CommentForm.

Finalmente, se renderiza la plantilla 'post-detail.html' y se pasa el post, la lista de comentarios y el nuevo comentario (si existe) a la plantilla como contexto.

## Añadir los comentarios al template

Para añadir los comentarios a nuestro blog vamos a implementar la siguiente lógica:

1. Visualizar el número total de comentarios publicados de un articlo
2. Visualizar una lista de los comentarios del árticulo.
3. Visualizar el formulario para que los visitantes dejes sus comentarios.


En nuestro template post-single-content.html agregamos la siguientes lineas:

`````
{% with comments.count as total_comments %}
                            <h3 id="comments-title">
                                <span>{{ total_comments }}</span> comment{{ total_comments|pluralize }}
                            </h3>
                        {% endwith %}
`````

En este fragmento de código, se está utilizando el contexto (contexto o context manager) "with" para crear una variable local llamada "total_comments" que almacena el número de comentarios en una publicación.

El número de comentarios se obtiene a través de la propiedad "count" en el objeto de comentarios. La variable "total_comments" se utiliza para mostrar el número total de comentarios en la publicación.

El filtro "pluralize" se usa para determinar si se debe mostrar "comentario" o "comentarios" dependiendo de si hay uno o más comentarios.





