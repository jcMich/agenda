from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.home.views',
    url(r'^$','index_view',name='index'),
    url(r'^about/$','about_view', name='about'),
    url(r'^login/$','login_view', name='login'),
    url(r'^logout/$','logout_view',name='logout'),
    url(r'^contacto/$','contacto_view',name='contacto'),
    url(r'^registrarUsuario/$','registrarUsuario_view',name='registrarUsuario'),
)
