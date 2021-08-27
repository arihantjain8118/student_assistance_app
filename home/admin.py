from django.contrib import admin

# Register your models here.


from .models import Lecture, Batch

admin.site.register(Lecture)
admin.site.register(Batch)