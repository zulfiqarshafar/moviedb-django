from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(MPAA_Rating)
admin.site.register(MPAA_Rating_Type)