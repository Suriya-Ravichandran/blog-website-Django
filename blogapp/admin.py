from django.contrib import admin
from .models import Post,Catagory
# Register your models here.
# class PostAdmin(admin.ModelAdmin):

admin.site.register(Post)
admin.site.register(Catagory)