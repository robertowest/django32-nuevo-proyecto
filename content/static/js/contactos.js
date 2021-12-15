function AgregarTelefono(obj) {
    // persona_id = document.getElementById('id_persona').options.selectedIndex;
    telefono_id = $('#id_telefono :selected').val();
    $.ajax({
        url: obj.getAttribute("href"),
        data: { telefono: telefono_id },
        success: function(response) {
            $('#comunicaciones').html(response);
        },
        error: function(xhr, status, error) {
            $('#comunicaciones').html("<span class='text-danger'>Se produjo un error de carga el formulario.</span>");
            console.log(xhr.responseText);
        }
    });
    return false;
};