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

//Redirecionamento dos Botões do Menu

// Botão "Minha Conta" abre Pop-up
function abrirPopup(event) {
    document.getElementById('popup-conta').classList.remove('hidden');
    event.stopPropagation();
}

// Esconde Pop-up
function fecharPopup() {
    document.getElementById('popup-conta').classList.add('hidden');
}

// Ativação da função
document.getElementById('botao-conta').onclick = abrirPopup;
document.querySelector('.botao-fechar').onclick = fecharPopup;

document.addEventListener('click', function(event) {
    const popup = document.getElementById('popup-conta');
    if (!popup.contains(event.target) && !document.getElementById('botao-conta').contains(event.target)) {
        fecharPopup();
    }
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


// Analisar
document.addEventListener("DOMContentLoaded", function() {
    var popup = document.getElementById("popup-conta");
    var btn = document.querySelector(".foto-perfil");
    var span = document.getElementsByClassName("botao-fechar")[0];

    btn.onclick = function() {
        fetchUserData();
        popup.classList.remove("hidden");
    }

    span.onclick = function() {
        popup.classList.add("hidden");
    }

    window.onclick = function(event) {
        if (event.target == popup) {
            popup.classList.add("hidden");
        }
    }

    function fetchUserData() {
        const data = {
            id: '12345',
            nome: 'João da Silva',
            email: 'joao.silva@gmail.com',
            dataNascimento: '1990-01-01',
            telefone1: '123456789',
            telefone2: '987654321'
        };
        
        preencherDados(data);
    }

    function preencherDados(data) {
        document.getElementById('id').value = data.id;
        document.getElementById('nome').value = data.nome;
        document.getElementById('email').value = data.email;
        document.getElementById('data-nascimento').value = data.dataNascimento;
        document.getElementById('telefone1').value = data.telefone1;
        document.getElementById('telefone2').value = data.telefone2;
    }
});
