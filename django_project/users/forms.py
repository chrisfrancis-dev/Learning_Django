# import forms from django
from django import forms
# import the User model to specify that the data from the form should be saved in the User model
from django.contrib.auth.models import User
# importing the UserCreationForm since we need to add a field in it
from django.contrib.auth.forms import UserCreationForm

# creating a class that inherits from the UserCreationForm
class UserRegistrationForm(UserCreationForm):
    # we are adding an email field to our form, we can add the required parameter, like required = False, to specify to the user that it is not compulsory to fill this field but if you leave it empty it is set to True by default
    email = forms.EmailField()
    # this class Meta is doing some configurations in our forms
    class Meta:
        # this line would configure that when we do a form.save() the data will be stored in the User model
        model = User
        # the fields that we have in this list are the fields that we want in the form in this particular order
        fields = ['username','email','password1','password2']
