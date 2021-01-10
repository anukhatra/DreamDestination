from django.shortcuts import render, HttpResponse 

# Create your views here.
def index(request):
       context = {
          "variable" : "this is context"
       }
       return render(request , "index.html", context )
def home(request):
       return render(request , "home.html" )

def about(request):
   return render(request , "about.html" )
  # return HttpResponse("this is about page")

def services(request):
   return render(request , "services.html" )
  
def contact(request):
  return render(request , "contact.html" )
