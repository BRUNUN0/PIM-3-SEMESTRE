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

// Abrir pop-up do menu
function abrirMenu() {
    document.getElementById('menu').classList.toggle('hidden');
    event.stopPropagation();
}
// Fechar pop-up do menu
function fecharMenu() {
    const menu = document.getElementById('menu');
    if (!menu.classList.contains('hidden') && !menu.contains(event.target)) {
        menu.classList.add('hidden')
    }
}
document.getElementById('foto-perfil').onclick = abrirMenu;
document.addEventListener('click', fecharMenu);


// Função Relógio
function atualizarRelogio() {
    const agora = new Date();

    let horas = agora.getHours();
    let minutos = agora.getMinutes();
    let segundos = agora.getSeconds();

    //Garantir que sempre tenha dois dígitos
    horas = horas < 10 ? '0' + horas : horas;
    minutos = minutos <10 ? '0' + minutos : minutos;
    segundos = segundos < 10 ? '0' + segundos : segundos;

    // Seleciona o relógio pelo id
    const relogio = document.getElementById('relogio');
    relogio.textContent = `${horas}:${minutos}:${segundos}`;
}

// Atualiza o relógio a cada segundo
setInterval(atualizarRelogio, 1);