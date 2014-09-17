

var tName = "#tabla_registros";
var btnDelete = ".delete";
var frmModel = '#frmEliminar';
var nombreVentanaModal = '#myModal';

$(document).on('ready',function(){
    $(btnDelete).on('click',function(e){
        console.log(e);
        e.preventDefault();
        var Pid = $(this).attr('id'); //id del registro a eliminar
        var name = $(this).data('name'); //nombre del registro a eliminar
        $('#modelIdRegistro').val(Pid)
    });

});