from django.contrib import admin

from .models import Person
from .models import Pet
# Register your models here.

admin.site.register(Pet)
admin.site.register(Person)

