function redirecionarHome() {
    window.location.href = "home.html";
}
function redirecionarPlantação() {
    window.location.href = "plantacao.html";
}
function redirecionarConsumo() {
    window.location.href = "consumo.html";
}
function redirecionarAtividades() {
    window.location.href = "atividades.html";
}

document.getElementById('botao-home').onclick = redirecionarHome;
document.getElementById('botao-plantacao').onclick = redirecionarPlantação;
document.getElementById('botao-consumo').onclick = redirecionarConsumo;
document.getElementById('botao-atividades').onclick = redirecionarAtividades;