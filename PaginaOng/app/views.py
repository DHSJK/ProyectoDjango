from django.shortcuts import render

# Create your views here.
def home(request):
    return  render(request, 'app/home.html')

def index(request):
    return render(request, 'app/index.html')

##def galeria(request):
  ##  return render(request, 'app/galeria.html')
