from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
html_base = """
    <h1>Mi web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about">Acerca de...</a></li>
    </ul>
"""

def home(request):
    return render(request, "nucleoCarolina/home.html")
def about(request):
    return render(request, "nucleoCarolina/about.html")
