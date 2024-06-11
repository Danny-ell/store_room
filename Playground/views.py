from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request-> Response
#request handler
name="Daniel"
def say_hello(request):
    context={"name":name}
    return render (request, "Doaz.html", context)
def new_window(request):
    return HttpResponse("You clicked the logo")