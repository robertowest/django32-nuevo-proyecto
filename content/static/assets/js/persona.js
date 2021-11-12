$(document).ready(function() {
    $("#persona-crear").modalForm({
        formURL: "{% url 'personas:create' %}"
    });
});
