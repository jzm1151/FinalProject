$(document).ready(function() {
    $('.registerForm').hide();

    $('#loginRadio').change(function() {
        $('.registerForm').hide();
        $('.loginForm').show();
     });

    $('#registerRadio').change(function () {
        $('.loginForm').hide();
        $('.registerForm').show();
    });
});