# addin the redirect method to the import statement to change the page once the registration has been done 
from django.shortcuts import render, redirect 
# django already has a form template for us so that we don't have to worry about user authentication etc, we are importing that form
# from django.contrib.auth.forms import UserCreationForm # commenting this out because we will be using our new created form
# imports the packages to show a flash message
from django.contrib import messages
# importing the form that we made in forms.py this has an extra email field
# so now we have to replace UserCreationForm with UserRegistrationForm
from .forms import UserRegistrationForm
# Create your views here.

def register(request):
    print(request)
    # checks if the request is POST, if it is then data is comming from the form
    if request.method == 'POST':
        # this renders a form with the data that was inputed by the user
        form = UserRegistrationForm(request.POST)
        # checking if the form data is valid
        if form.is_valid():
            # will save the user in the database
            form.save()
            # getting the username from the form 
            username = form.cleaned_data.get('username')
            # sending a message to show the username on top, and the code for this is written in base.html
            messages.success(request, f'Account created for {username}!') # sends the message along with redirect to home.html on the next line
            return redirect('blog-home') # this was the name given to the home page in the urls.py of the blog app
    else:
        # rendering a blank form 
        form = form = UserRegistrationForm()     
    return render(request, 'users/register.html', {'form':form}) # passed users as a parameter
