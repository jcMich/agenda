from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Registros, Grupos
from .forms import RegistrosForm,AddGrupoForm
from django.http import HttpResponseRedirect
from django.db.models import Q  #para consultas avansadas
# Create your views here.

def registros_view(request):
    registros = []
    msg = ''
    stts = False
    if request.method == "POST":
        if "buscar" in request.POST:
            s = request.POST['buscar']
            r = Registros.objects.filter(Q(nombre__contains=s) | Q(apellidos__icontains=s)).order_by('nombre')
            l = len(r)
            ctx = {'registros':r,'msg':"%s registros encontrados"%l}
            return render_to_response("registros/registros.html",ctx,context_instance=RequestContext(request))

        if "registro_id" in request.POST:
            try:
                id_reg = request.POST['registro_id']
                r = Registros.objects.get(pk=id_reg)
                r.delete()
                r = Registros.objects.filter(user=request.user)
                msg ={'msg':'Registro Eliminado Correctamente','registros':r}

                return render_to_response('registros/registros.html',msg,context_instance=RequestContext(request))
            except:
                msg = {'msg':"Error al eliminar registro"}
                return render_to_response('registros/registros.html',msg,context_instance=RequestContext(request))

    else: #get
        if request.user.is_authenticated():
            registros = Registros.objects.filter(user=request.user)
            if not registros:
                stts = True
    ctx = {'registros':registros,'stts':stts}
    return render_to_response('registros/registros.html',ctx,context_instance = RequestContext(request))


def registro_view(request,id_reg):
    reg = Registros.objects.get(pk=id_reg)
    ctx = {'registro':reg}
    return render_to_response('registros/registro.html',ctx,context_instance=RequestContext(request))

def addRegistro_view(request):
    if request.method == "POST":
        form = RegistrosForm(request.user,request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = request.user
            add.save()
            return HttpResponseRedirect('/registro/%s'%add.id)
    else:
        form = RegistrosForm(user = request.user)

    ctx = {'form':form}
    return render_to_response('registros/addRegistro.html',ctx,context_instance=RequestContext(request))


def addGrupo_view(request):
    grupos = []
    if request.method == "POST":
        form = AddGrupoForm(request.POST)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = request.user
            add.save()
            return HttpResponseRedirect('/')
    else:
        form = AddGrupoForm()
    ctx = {'form':form,'grupos':grupos}
    return render_to_response('registros/addGrupo.html',ctx,context_instance=RequestContext(request))

def editRegistro_view(request, id_edit):
    from ipdb import set_trace
    set_trace()
    r = Registros.objects.get(pk=id_edit)
    if request.method == "POST":
        form = RegistrosForm(request.POST, request.FILES, instance=r)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registros/')

    form = RegistrosForm(instance=r)
    ctx = {'form':form}
    return render_to_response('registros/editRegistro.html',ctx,context_instance=RequestContext(request))
