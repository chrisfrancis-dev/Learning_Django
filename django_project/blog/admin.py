from django.contrib import admin
from .models import Post # importing the post model 
# Register your models here.
admin.site.register(Post) # this is to get the post model in the admin portal
