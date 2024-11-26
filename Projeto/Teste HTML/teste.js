// Redirecionamento dos botões da navbar
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

// Ativação dos botões da navbar
document.getElementById('botao-home').onclick = redirecionarHome;
document.getElementById('botao-plantacao').onclick = redirecionarPlantação;
document.getElementById('botao-consumo').onclick = redirecionarConsumo;
document.getElementById('botao-atividades').onclick = redirecionarAtividades;

// Abrir pop-up do menu
function abrirMenu(event) {
    document.getElementById('menu').classList.toggle('hidden');
    event.stopPropagation();
}
// Fechar pop-up do menu
function fecharMenu(event) {
    const menu = document.getElementById('menu');
    if (!menu.classList.contains('hidden') && !menu.contains(event.target)) {
        menu.classList.add('hidden');
    }
}
document.getElementById('foto-perfil').onclick = abrirMenu;
document.addEventListener('click', fecharMenu);

//Redirecionamento dos Botões do Menu
document.addEventListener('DOMContentLoaded', function() {
    function popupMinhaConta() {
        const botaoPerfil = document.getElementById('botao-perfil');
        const popupPerfil = document.getElementById('popup-perfil');
        const botaoFecha = document.getElementById('fecha-perfil');
        const menu = document.getElementById('menu');
        const botaoSair = document.getElementById('botao-sair');

        // Função para abrir o popup e esconder o menu
        botaoPerfil.addEventListener('click', function() {
            popupPerfil.classList.remove('hidden');
            menu.classList.add('hidden'); // Esconde o menu
        });

        // Função para fechar o popup
        botaoFecha.addEventListener('click', function() {
            popupPerfil.classList.add('hidden');
        });

        // Fechar popup ao clicar fora dele
        window.addEventListener('click', function(event) {
            if (event.target === popupPerfil) {
                popupPerfil.classList.add('hidden');
            }
        });
    }

    popupMinhaConta();
});





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
