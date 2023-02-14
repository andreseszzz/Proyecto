from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def conocenos(request):
    return render(request, "conocenos.html")