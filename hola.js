function validateForm() {
    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    var email = document.getElementById('email').value;
    var celular = document.getElementById('celular').value;
    var area = document.getElementById('area').value;

    var nombreRegex = /^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$/;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    var nombreValid = nombreRegex.test(nombre);
    var apellidoValid = nombreRegex.test(apellido);
    var emailValid = emailRegex.test(email);
    var celularValid = !isNaN(celular) && celular.length === 10;
    var areaValid = area !== '';
    document.getElementById('nombre').innerText;
    if (!nombreValid) {
        document.getElementById('nombreError').innerText = 'Ingrese un nombre válido.';
    } else {
        document.getElementById('nombreError').innerText = '';
    }

    if (!apellidoValid) {
        document.getElementById('apellidoError').innerText = 'Ingrese un apellido válido.';
    } else {
        document.getElementById('apellidoError').innerText = '';
    }
    if (!emailValid) {
        document.getElementById('emailError').innerText = 'Ingrese un correo electrónico válido.';
    } else {
        document.getElementById('emailError').innerText = '';
    }
    if (!celularValid) {
        document.getElementById('celularError').innerText = 'Ingrese un número de 10 dígitos).';
    } else {
        document.getElementById('celularError').innerText = '';
    }
    var cadena=document.getElementById('comentario').value;
    //document.write('*'+cadena+'*');
    let L=cadena.length;
    //document.write('*'+L+'*');
    if (L==0) {
        document.getElementById('comentarioError').innerText = 'Comentario no puede quedar vacío';
    } else {
        document.getElementById('comentarioError').innerText = '';
    }
    return nombreValid && apellidoValid && emailValid && celularValid && areaValid;
}
// script.js
document.addEventListener('DOMContentLoaded', function() {
    const ratings = document.querySelectorAll('.rating input');
    ratings.forEach(rating => {
        rating.addEventListener('change', function() {
            alert('Has seleccionado una puntuación de ' + this.value);
        });
    });
});
