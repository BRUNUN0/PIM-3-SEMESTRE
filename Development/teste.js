//  // Função para definir o botão ativo
//     function setActiveButton() {
//         // Obtenha o caminho do arquivo atual
//         const path = window.location.pathname;
//         const currentPage = path.split("/").pop();

//         // Defina um mapeamento das páginas para os botões
//         const pageToButtonMap = {
//             'home.html': 'botao-home',
//             'plantacao.html': 'botao-plantacao',
//             'consumo.html': 'botao-consumo',
//             'atividades.html': 'botao-atividades'
//         };

//         // Obtenha o ID do botão correspondente à página atual
//         const activeButtonClass = pageToButtonMap[currentPage];

//         // Adicione a classe 'active' ao botão correspondente
//         if (activeButtonClass) {
//             document.querySelector(`.${activeButtonClass}`).classList.add('active');
//      }
// }

// Execute a função ao carregar a página
window.onload = setActiveButton;


document.querySelector('.botao-entrar').addEventListener('click', function() {
    window.location.href = 'home.html';
    });

document.querySelector('.botao-home').addEventListener('click', function() {
    window.location.href = 'home.html';
    });

    document.querySelector('.botao-plantacao').addEventListener('click', function() {
        window.location.href = 'plantacao.html';
        });