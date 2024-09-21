from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def intro(request):
    return render(request,'intro.html')
def index(request):
    return render(request,'index.html')
