from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def view(request):
    return render(request,'view.html')
