from django.urls import path
from . import views # . means current directory and views is a file in that
# the control here comes from project urls 
urlpatterns = [
    path('', views.home, name = 'blog-home'), #empty path for the home page, views.home imports the home function from views name gives it a name
    path('about', views.about, name = 'blog-about'), # about is a function in views
]