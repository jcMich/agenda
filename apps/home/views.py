from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import LoginForm,ContactForm, RegistrarUsuarioForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives # envio de html
from apps.home.models import userProfile
# Create your views here.
def index_view(request):
    return render_to_response('home/index.html',context_instance = RequestContext(request))

def about_view(request):
    return render_to_response('home/about.html',context_instance=RequestContext(request))


def login_view(request):
    mensaje = " "
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            usuario = authenticate(username=usuario,password=password)
            if usuario is not None and usuario.is_active:
                login(request,usuario)
                return HttpResponseRedirect("/")
            else:
                mensaje = 'Usuario y/o password incorrectos'
    else: #GET
        form = LoginForm()
    ctx = {'form':form,'mensaje':mensaje}
    return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def contacto_view(request):
    mensaje = " "
    info_enviada = False
    email = ""
    titulo =""
    comentario = ""

    form = ContactForm()
    if request.user.is_authenticated():
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                formv = ContactForm()
                email = form.cleaned_data['email']
                titulo = form.cleaned_data['titulo']
                comentario =form.cleaned_data['comentario']
                #configuracon de envio via gmail
                to_admin = 'jc.fie.umich@gmail.com'
                html_context = 'Informacion recivida de:  %s El titulo es: %s <br> <h2>contenido:</h2><br> <h3>%s</h3>'%(email,titulo,comentario)

                msg = EmailMultiAlternatives('Correo de contacto',html_context,'from@server.com',[to_admin])
                msg.attach_alternative(html_context,'text/html') #def contenido html
                msg.send()

                mensaje = "mensaje enviado"

                ctx = {'form':formv,'mensaje':mensaje}
                return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))
        else: # GET
            form = ContactForm()
    else:
        mensaje = "Solo usuarios logeados pueden comentar .|."
    ctx = {'form':form,'mensaje':mensaje}
    return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))


def registrarUsuario_view(request):
    if request.method == "POST":
        form = RegistrarUsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.cleaned_data['usuario']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            photo = form.cleaned_data['photo']
            # crear instancia de usuario y
            u = User.objects.create(username=user)
            u.set_password(password_one)
            u.save()  #guardamos nuevo usuario
            up = userProfile.objects.create(user=u,photo=photo)
            up.save() #guardamos imagen de usuario

            return HttpResponseRedirect('/login/')
    else:
        form = RegistrarUsuarioForm()
    ctx = {'form':form}
    return render_to_response('home/registrarUsuario.html',ctx,context_instance=RequestContext(request))