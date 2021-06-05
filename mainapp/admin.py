from django.contrib import admin
from .models import reservation,buffet,items,menu
# Register your models here.

admin.site.register(reservation)
admin.site.register(buffet)
admin.site.register(items)
admin.site.register(menu)