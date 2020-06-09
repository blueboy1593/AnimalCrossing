from django.contrib import admin
from .models import Fish, Insect, Fossil, Animal, Painting
admin.site.register(Painting)
admin.site.register(Fish)
admin.site.register(Insect)
admin.site.register(Animal)
admin.site.register(Fossil)