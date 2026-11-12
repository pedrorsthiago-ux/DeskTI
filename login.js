const formulario = document.getElementById("loginForm");
const email = document.getElementById("email");
const mensagem = document.getElementById("mensagem");
const esqueci = document.getElementById("esqueci");

esqueci.addEventListener("click", function(event) {
    event.preventDefault();

    if (email.value === "") {
        mensagem.textContent = "Digite seu e-mail institucional.";
    } else if (!email.checkValidity()) {
        mensagem.textContent = "Digite um e-mail válido.";
    } else {
        mensagem.textContent = "Se o e-mail for valido, você recebera um email para alterar sua senha.";
    }
});

formulario.addEventListener("submit", function(event) {
    event.preventDefault();
});