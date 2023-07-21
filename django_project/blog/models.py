from django.db import models
# this is added
from django.utils import timezone
# django has already created a User table in this location 'django.contrib.auth.models' and we will use this to connect to our Post database
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    '''
    here we are creating fields for the database
    CharField(max_length = 100) takes input of multiple characters
    '''
    title = models.CharField(max_length = 100)
    # TextField is used because we will be having multiple lines of content 
    content = models.TextField()
    '''
    date_posted = models.DateTimeField(auto_now = True) # this will update the date everytime the post is updated
    date_posted = models.DateTimeField(auto_now_add = True) # this will set the date only when the post is created
    default = timezones.now this argument is used because I want the option to change the date
    '''
    date_posted = models.DateTimeField(default = timezone.now)
    '''
    the author is a ForeignKey and it is connected to the User table the 'on_delete=models.CASCADE' parameter specifies what happens to the user once the post is deleted
    we are using a ForeingKey because one user can have multiple posts but one post can have only one user
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
# this is added to make the Post more discriptive
    def __str__(self):
        return self.title