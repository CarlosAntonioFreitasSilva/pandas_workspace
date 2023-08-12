from django.shortcuts import render

nome = {"nome":"Carlos Antônio"}

# Create your views here.
def home(request):
    return render(request,'post/index.html',nome)