from django.contrib import admin
from .models import *
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
from .models import Image

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Post, MarkdownxModelAdmin)