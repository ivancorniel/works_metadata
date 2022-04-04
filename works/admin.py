from operator import imod
from django.contrib import admin

from .models import Works, Contributor

admin.site.register(Works)
admin.site.register(Contributor)
