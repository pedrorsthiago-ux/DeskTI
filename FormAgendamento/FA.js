const formulario = document.getElementById("FormAgendamento");
const mensagem = document.getElementById("Mensagem");

formulario.addEventListener("submit", function(event) {

    mensagem.textContent = "Enviando solicitação...";

});