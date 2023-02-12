## Los queryset y los manager en Django

En Django, los QuerySet y los Manager son dos componentes clave para trabajar con la base de datos.

Un QuerySet es una lista de objetos de modelo que se pueden seleccionar, filtrar y ordenar en la base de datos. Es una representación abstracta de un conjunto de registros en la base de datos. Los QuerySet se pueden encadenar para crear consultas complejas y se pueden utilizar para realizar operaciones en la base de datos, como la actualización de registros o la eliminación de registros.

Un Manager es un objeto que se encarga de gestionar los QuerySet para un modelo. Es el encargado de filtrar y ordenar los registros en la base de datos y de crear nuevos registros. Cada modelo en Django tiene un Manager por defecto que se puede personalizar para cumplir con tus requisitos específicos.

En resumen, los QuerySet y los Manager son herramientas poderosas que te permiten trabajar con la base de datos en Django de manera eficiente y flexible. Te permiten crear consultas complejas, realizar operaciones en la base de datos y personalizar la forma en que se obtienen y se gestionan los registros en la base de datos.

## Como crear un objeto Post desde el Shell


````
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> my_user = User.objects.get(username="yllorca")
>>> print(my_user)
yllorca
>>> new_post = Post(title="post desde consola", slug="post-desde-consola", body="my body", author=my_user)
>>> new_post.save()
>>> my_posts = Post.objects.all()
>>> print(my_posts)
<QuerySet [<Post: post desde consola>, <Post: Creado por consola>, <Post: test de ejemplo>]>
````

Este código es un ejemplo de cómo se pueden crear y obtener registros en la base de datos desde la consola de Django.

En la primera línea, se importa el modelo User de la aplicación de autenticación de Django. En la segunda línea, se importa el modelo Post desde la aplicación blog.

Luego, se utiliza el método User.objects.get para obtener un usuario con el nombre de usuario "yllorca". Este método devuelve un objeto de modelo User que representa al usuario con el nombre de usuario especificado.

Después, se crea un nuevo registro de Post utilizando el constructor Post(). Se especifican los valores para los campos title, slug, body y author del modelo Post. El campo author se establece en el objeto de modelo User obtenido anteriormente.

Luego, se utiliza el método save() para guardar el nuevo registro en la base de datos.

Finalmente, se utiliza el método Post.objects.all() para obtener todos los registros de Post de la base de datos. Este método devuelve un QuerySet que representa todos los registros de Post en la base de datos. El resultado se imprime en la consola.

## Como actualizar un objeto Post desde el shell.

Para actualizar un objeto Post en django
debemos instanciarlo primero y despues actualizar el o los campos.

````
>>> new_post.title = "New Title"
>>> new_post.save()
`````

## El método filter en un queryset

El método filter en un QuerySet de Django es una herramienta para filtrar los registros de un modelo en la base de datos. Permite crear una consulta que devuelva solo aquellos registros que cumplan con ciertos criterios.

El método filter toma uno o varios argumentos que representan los criterios de filtrado. Cada argumento es una expresión que se evalúa como verdadera o falsa para cada registro en la base de datos. Si una expresión se evalúa como verdadera, el registro correspondiente se incluye en el resultado de la consulta.

Aquí hay un par de ejemplos que ilustran cómo se puede utilizar el método filter:

`````
# Ejemplo 1: Obtener todos los registros de Post que tengan el estado "publicado"
posts = Post.objects.filter(status="published")

# Ejemplo 2: Obtener todos los registros de Post que tengan un título que contenga la palabra "Django"
posts = Post.objects.filter(title__contains="Django")
`````

En el primer ejemplo, se utiliza el método filter para obtener todos los registros de Post que tengan el estado "publicado". El argumento status="published" especifica el criterio de filtrado.

En el segundo ejemplo, se utiliza el método filter para obtener todos los registros de Post que tengan un título que contenga la palabra "Django". El argumento title__contains="Django" especifica el criterio de filtrado. La doble barra baja (__) en el nombre del campo title es un operador de búsqueda que indica que se debe buscar la palabra "Django" en el campo title.

Es importante destacar que los resultados de una consulta con el método filter siempre son un QuerySet, que puede ser encadenado con otros métodos para crear consultas más complejas.

## El método exclude en un queryset

El método exclude en un QuerySet de Django es similar al método filter, pero en lugar de incluir los registros que cumplen con ciertos criterios, excluye los registros que cumplen con esos criterios.

Aquí hay un par de ejemplos que ilustran cómo se puede utilizar el método exclude:

`````
# Ejemplo 1: Obtener todos los registros de Post que no tengan el estado "publicado"
posts = Post.objects.exclude(status="published")

# Ejemplo 2: Obtener todos los registros de Post que no tengan un título que contenga la palabra "Django"
posts = Post.objects.exclude(title__contains="Django")
`````

En el primer ejemplo, se utiliza el método exclude para obtener todos los registros de Post que no tengan el estado "publicado". El argumento status="published" especifica el criterio de exclusión.

En el segundo ejemplo, se utiliza el método exclude para obtener todos los registros de Post que no tengan un título que contenga la palabra "Django". El argumento title__contains="Django" especifica el criterio de exclusión. La doble barra baja (__) en el nombre del campo title es un operador de búsqueda que indica que se debe buscar la palabra "Django" en el campo title.

Los métodos filter y exclude pueden encadenarse para crear consultas complejas con múltiples criterios de filtrado y exclusión.


Aquí hay un par de ejemplos que ilustran cómo se pueden utilizar los métodos filter y exclude en conjunto para crear consultas más complejas:


`````
# Ejemplo 1: Obtener todos los registros de Post que tengan el estado "publicado" y no tengan un título que contenga la palabra "Django"
posts = Post.objects.filter(status="published").exclude(title__contains="Django")
`````

En este ejemplo se utiliza el método filter para incluir los registros de Post que tengan el estado "publicado", y luego se utiliza el método exclude para excluir los registros que tengan un título que contenga la palabra "Django".

## El método order_by en un queryset

El método order_by en un QuerySet de Django es una herramienta para ordenar los registros de un modelo en la base de datos. Permite crear una consulta que devuelva los registros en un orden específico.

El método order_by toma uno o varios argumentos que representan los criterios de ordenamiento. Cada argumento es el nombre de un campo de modelo por el que se debe ordenar los registros. Si se especifica más de un argumento, los registros se ordenarán primero por el primer argumento y luego por el segundo argumento y así sucesivamente.

Aquí hay un par de ejemplos que ilustran cómo se puede utilizar el método order_by:

`````
# Ejemplo 1: Obtener todos los registros de Post ordenados por título
posts = Post.objects.all().order_by("title")

# Ejemplo 2: Obtener todos los registros de Post ordenados primero por fecha de publicación y luego por título
posts = Post.objects.all().order_by("-publish", "title")
`````

En el primer ejemplo, se utiliza el método order_by para ordenar todos los registros de Post por título. El argumento "title" especifica el criterio de ordenamiento.

En el segundo ejemplo, se utiliza el método order_by para ordenar todos los registros de Post primero por fecha de publicación y luego por título. El argumento "-publish" indica que se debe ordenar los registros en orden inverso (de manera descendente), mientras que el argumento "title" indica que se debe ordenar los registros por título.

Es importante destacar que los resultados de una consulta con el método order_by siempre son un QuerySet, que puede ser encadenado con otros métodos para crear consultas más complejas.

## Eliminar objetos en Django

En Django, se pueden eliminar registros en la base de datos usando el método delete() en un objeto.

El método delete() en un objeto: Este método se puede utilizar en un objeto individual para eliminar un solo objeto. Por ejemplo:

`````
# Eliminar un registro de Post en particular
post = Post.objects.get(id=1)
post.delete()
`````

Es importante destacar que una vez que un objeto se ha eliminado de la base de datos, no hay manera de recuperarlo. Por lo tanto, es importante ser cuidadoso al utilizar estos métodos y asegurarse de que se están eliminando los objetos correctos.

¡Buen trabajo, Henrry!