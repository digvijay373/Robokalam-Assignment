from django.contrib import admin
from .models import Info

class InfoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Info, InfoAdmin)