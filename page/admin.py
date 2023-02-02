from django.contrib import admin
from page.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Dastur)
admin.site.register(Internet)
admin.site.register(Wifi)
admin.site.register(Kompyuter)
admin.site.register(Server)
admin.site.register(Hodim)
admin.site.register(Kamera)
admin.site.register(Gps)
admin.site.register(Taklif)
admin.site.register(User2,UserAdmin)
