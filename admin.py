from django.contrib import admin
from .models import Photo, Person, PersonGallery

# Register models.
admin.site.register(Photo)
admin.site.register(Person)
admin.site.register(PersonGallery)
