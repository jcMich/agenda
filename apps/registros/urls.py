from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.registros.views',
    url(r'^registros/$','registros_view',name='registros'),
    url(r'^registro/(?P<id_reg>.*)/$','registro_view'), #dinamica
    url(r'^addRegistro/$','addRegistro_view',name='addRegistro'),
    url(r'^addGrupo/$','addGrupo_view',name='addGrupo'),
    url(r'^editRegistro/(?P<id_edit>.*)/$','editRegistro_view'),  #dinamica
)
