$(document).ready(function() {
    $('.registerForm').hide();

    $('#loginRadio').change(function() {
        $('.registerForm').hide(500);
        $('.loginForm').show(500);
     });

    $('#registerRadio').change(function () {
        $('.loginForm').hide(500);
        $('.registerForm').show(500);
    });
});