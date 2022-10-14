function criarCarta(){
    var primeira_tela = document.getElementById('tela-inicial');
    var main = document.getElementById('main')
    main.classList.add('-translate-y-full')
    primeira_tela.classList.add('-translate-y-full')
  }
  
function apareceBaixar(){
    var popup = document.getElementById('pop-up');
    popup.classList.remove('-z-10');
    popup.classList.add('z-10');


}