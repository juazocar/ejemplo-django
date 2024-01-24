from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def menu(request):
    request.session["usuario"]="jazocar"
    usuario=request.session["usuario"]
    context= {'usuario':usuario}
    return render(request, 'administrador/menu.html', context)
    