from django.shortcuts import render
from .models import Alumno, Genero
from .forms import GeneroForm, AlumnoForm
# Create your views here.

def crud(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos':alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnosAdd(request):
    print(request.method)
    if request.method != "POST":
        print('if')
        generos = Genero.objects.all()
        context = {'generos': generos}
        return render(request, 'alumnos/alumnos_add.html', context)
    else:
        print('else')
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"] 
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create(rut = rut,
                                    nombre = nombre,
                                    apellido_paterno = aPaterno,
                                    apellido_materno = aMaterno,
                                    fecha_nacimiento = fechaNac,
                                    id_genero = objGenero,
                                    telefono = telefono,
                                    email = email,
                                    direccion = direccion, 
                                    activo = 1)
        obj.save()
        context = {'mensaje': 'Ok, datos grabados...'}
        return render(request, 'alumnos/alumnos_add.html', context)

def alumnos_del(request, pk):
    context={}
    try:
        alumno = Alumno.objects.get(rut=pk)
        alumno.delete()
        mensaje = "Bien, datos eliminados..."
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje':mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    except:
        mensaje = "Error, rut no existe..."
        alumnos = Alumno.objects.all()
        context={'alumnos': alumnos, 'mensaje':mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)


def index(request):
    alumnos = Alumno.objects.all()
    form = AlumnoForm()

   
    
    if request.method == 'POST':
        request.session["email"]="ju.azocar@profesor.duoc.cl"
        print("por el post")
    else: 
        request.session["email"]="No autenticado"
        print("por el get")
    
    email = request.session["email"]

    context={"alumnos": alumnos, 'form': form, 'email':email}


    return render(request, 'alumnos/index.html', context)