document.getElementById("formulario")
.addEventListener("submit", function(event) {

    event.preventDefault();

    alert(
        "Solicitação preenchida com sucesso! " +
        "O sistema ainda precisa ser conectado " +
        "ao banco de dados para registrar o pedido."
    );

    this.reset();

});