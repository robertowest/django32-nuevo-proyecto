$(document).ready(function() {
    $("#login-btn").modalForm({
        modalID: "#modal-auth",
        formURL: "/usuarios/login/",
    });

    $("#signup-btn").modalForm({
        modalID: "#modal-auth",
        formURL: "/usuarios/signup/",
        // formURL: "{% url 'usuarios:signup' %}",
    });

    // ocultar mensajes
    $(".alert").fadeTo(2000, 500).slideUp(500, function(){
        $(".alert").slideUp(500);
    });

    // autofoco en el primer campo del formulario modal
    $('.modal').on('shown.bs.modal', function () {
        $('form').find('input[type=text]').filter(':visible:first').focus();
    });
});
