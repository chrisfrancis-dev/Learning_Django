from django.shortcuts import render
# Since we are not using HttpResponse anymore I commented it out
# from django.http import HttpResponse # added import statement
# Create your views here.

post = [
    {
        'author':'Chris Francis',
        'topic':'HTML Basics',
        'description':'This is the Basics',
        'date':'July-20'
    },
    {
        'author':'Chris Francis',
        'topic':'HTML Basics',
        'description':'This is the Basics',
        'date':'July-20'
    }
] 

def home(request):
    context = {
        'posts':post
    }
    # return HttpResponse('<h1>HOME PAGE<h1>') commented since we don't need it 
    # request, then the template where the html page is located and then context which is data which will be manipulated on the html page
    return render(request,'blog/home.html',context) 

def about(request):
    # return HttpResponse('<h1>BLOG ABOUT<h1>') commented since we don't need it
    return render(request,'blog/about.html',{'title': 'about'})