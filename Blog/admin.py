from django.contrib import admin
from .models import *

# Register your models here.
class commentAdmin(admin.ModelAdmin):
    list_display = ['body', 'commentAuthor', 'commentBlog']

admin.site.register(Blog_m)
admin.site.register(Comment_m,commentAdmin)
# admin.site.register(Comment_m)

