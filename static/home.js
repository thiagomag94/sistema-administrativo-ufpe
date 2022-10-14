(function () {
    var menu = document.getElementById('nav'); // colocar em cache
    
    window.addEventListener('scroll', function () {
        
        if (window.scrollY > 80){

            
            menu.classList.add('bg-imagem-header'); // > 0 ou outro valor desejado
           
            menu.classList.add('shadow-2xl');
            menu.classList.add('border-b')
            
        }
        else {
            menu.classList.remove('bg-imagem-header');
            menu.classList.remove('shadow-2xl');
            menu.classList.remove('border-b')
        }
    });
})();

function searchShow(){
    var input = document.getElementById('pesquisa');
    input.classList.remove('scale-x-0')
    input.style.transition = 'all 2s ease'
    input.classList.add('scale-x-100')

};


