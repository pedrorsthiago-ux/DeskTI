
const formulario = document.getElementById("FormAgendamento");
const mensagem = document.getElementById("Mensagem");

formulario.addEventListener("submit", function(event) {
    event.preventDefault();

    mensagem.textContent = "Solicitação de atendimento enviada com sucesso!";

    formulario.reset();
});

