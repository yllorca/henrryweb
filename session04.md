## Creear una Aplicacion de Django
El administrador de Django es una interfaz web que permite a los desarrolladores y administradores realizar tareas administrativas en una aplicación Django sin tener que escribir código. Con el administrador de Django, puedes agregar, modificar y eliminar registros en la base de datos de tu aplicación y probar la integradidad de tu modelo de datos.

El administrador de Django es altamente personalizable y se puede adaptar a las necesidades específicas de tu aplicación. Por ejemplo, puedes definir qué campos se muestran en la lista de registros, qué campos son editables, qué tipos de filtros están disponibles, etc.


La clase ModelAdmin es una clase que proporciona la funcionalidad básica para personalizar la forma en que se muestran los modelos en el administrador de Django. Es una clase de Django que se encuentra en el módulo django.contrib.admin.


Por último, es importante registrar el modelo con el administrador personalizado utilizando el método admin.site.register. De esta manera, Django sabrá que debe utilizar el administrador personalizado en lugar del administrador predeterminado.

Abre el archivo admin.py de tu app blog e inserta el siguiente código

`````
from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',   
                       'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
`````

Este código es un ejemplo de un administrador personalizado para un modelo Post en Django.

La primera línea importa el módulo admin de Django, que es necesario para utilizar el administrador de Django. La segunda línea importa el modelo Post desde el módulo blog.models.

Luego, se utiliza la función admin.register para registrar el modelo Post con el administrador personalizado PostAdmin. Esta función es un decorador que hace que sea más fácil registrar un modelo con un administrador personalizado y va sustituir a la funcion por defecto admin.site.register() que utilizabamos hasta ahora.

La clase PostAdmin es una subclase de admin.ModelAdmin, y es la clase que personaliza la forma en que se muestran los registros del modelo Post en el administrador de Django.

Los atributos list_display, list_filter, search_fields, prepopulated_fields, raw_id_fields, date_hierarchy y ordering de la clase PostAdmin personalizan la forma en que se muestran los registros del modelo Post en el administrador de Django.

- list_display especifica los campos que se deben mostrar en la lista de registros.
- list_filter especifica los campos que se deben utilizar para filtrar los registros.
- search_fields especifica los campos que se deben utilizar para buscar registros.
- prepopulated_fields especifica los campos que se deben pre-rellenar automáticamente a partir de otros campos.
- raw_id_fields especifica los campos que deben mostrarse como un enlace a la página de edición del registro relacionado en lugar de como un selector de objetos.
- date_hierarchy especifica el campo que se debe utilizar para la jerarquía de fechas en la página de listado.
- ordering especifica el orden en que se deben mostrar los registros en la lista.

A modo de conclusión este fragmento de código es un ejemplo de cómo personalizar la forma en que se muestran los registros de un modelo en el administrador de Django utilizando la clase ModelAdmin. El nombre de la clase PostAdmin lo defines tú, por adopción de la comunidad siempre define el nombre de esta clase como MyModelAdmin donde MyModel sera el nombre de tu modelo.

¡Buen trabajo, Henrry!



