from django.contrib import admin
from .models import Post

#do panelu admina, importujemy, dodajemy, model post. Od teraz jest on w nim widoczny :)
admin.site.register(Post)
