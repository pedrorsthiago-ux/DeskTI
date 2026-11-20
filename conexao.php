
<?php

$host = "localhost";
$porta = "3307";
$banco = "deskti";
$usuario = "root";
$senha = "";

$conexao = new PDO(
    "mysql:host=$host;port=$porta;dbname=$banco;charset=utf8mb4",
    $usuario,
    $senha
);

?>
