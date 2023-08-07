from django.contrib import admin
from owner import models
# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
  list_display =['lib_name', 'lib_contact','lib_address']

admin.site.register(models.Library, LibraryAdmin)