
function carregaOwl(){
  $('.owl-carousel').owlCarousel({
    loop:false,
    margin:10,
    nav:true,
    responsive:{
    0:{
        items:1
    },
    600:{
        items:2
    },
    1000:{
        items:3
    }
  }
})
};



async function carregando(){
  var botao_enviar = window.document.getElementById('submit');
  botao_enviar.style.display = "none";
  var gif = window.document.getElementById('gif');
  gif.style.display = 'block';

}

function mudaPlaceholder(){
  var bg = window.document.getElementById('place-jinja');
  bg.style.color = 'blue';
  console.log('carregada a função')
}


function apareceMenu(){
  var botao_enviar = window.document.getElementById('submit');
  var body = window.document.getElementById('body')
  var menu = window.document.getElementById('nav-bar');
  var main = window.document.getElementById('main');
  botao_enviar.style.display = "none";
  menu.style.transition = 'all 2s ease'
  menu.style.display = 'flex';
  menu.style.transform = "translateY(75vh)";
 
  main.classList.add('blur-none');
  main.style.opacity = 0.1;
  body.style.backgroundColor = 'black';
  console.log(menu.style.transition )
  carregaOwl()
  
}



function fechaMenu(){
  var botao_fechar = window.document.getElementById('fechar-menu');
  var menu = window.document.getElementById('nav-bar');
  var main = window.document.getElementById('main');
  var botao_enviar = window.document.getElementById('submit');
  botao_enviar.style.display = "flex";
  menu.style.display = 'none';
  menu.style.transform = "translateY(-75vh)";
  main.style.opacity = 1
  menu.style.transition = 'all 10s ease 2s'
  console.log(menu.style.transition)
  
}



// Loaded via <script> tag, create shortcut to access PDF.js exports.
var pdfjsLib = window['pdfjs-dist/build/pdf'];
// The workerSrc property shall be specified.
pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://mozilla.github.io/pdf.js/build/pdf.worker.js';

$("#arquivo").on("change", function(e){
	var files = e.target.files;
  
  for (let i = 0; i < files.length; i++) {
    let file = files.item(i);
    
    if(file.type == "application/pdf"){
      var fileReader = new FileReader();  
      fileReader.onload = function() {
        var pdfData = new Uint8Array(this.result);
        // Using DocumentInitParameters object to load binary data.
        var loadingTask = pdfjsLib.getDocument({data: pdfData});
        loadingTask.promise.then(function(pdf) {
          console.log('PDF loaded');
          
          // Fetch the first page
          var pageNumber = 1;
          pdf.getPage(pageNumber).then(function(page) {
          console.log('Page loaded');
          
          var scale = 1;
          var viewport = page.getViewport({scale: scale});
  
          // Prepare canvas using PDF page dimensions
          var canvas = document.createElement('canvas');
          var div_esp = document.createElement('div');
          div_esp.classList.add('item');
          canvas.classList.add('h-64');
          canvas.classList.add('shadow-lg')
          canvas.style.borderRadius = "5px";
          canvas.style.borderWidth = "2px";
          canvas.style.borderColor = "red"
          var context = canvas.getContext('2d');
          div_esp.appendChild(canvas);
          $('.owl-carousel').append(div_esp)

          
          canvas.height = viewport.height;
          canvas.width = viewport.width;
  
          // Render PDF page into canvas context
          var renderContext = {
            canvasContext: context,
            viewport: viewport
          };
          var renderTask = page.render(renderContext);
          renderTask.promise.then(function () {
            console.log('Page rendered');
          });
          });
        }, function (reason) {
          // PDF loading error
          console.error(reason);
        });
      };
      fileReader.readAsArrayBuffer(file);
  
    }
  }


});





function enviadados() {
  console.log('rodando')
  var carta = document.getElementById('arquivo');
  var portaria = document.getElementById('arquivo2');
  var form = document.getElementById('form');
  var files_cartas = carta.files;
  var files_portaria = portaria.files;
  var formData = new FormData();
    
  console.log(files_cartas)
  
  for (let i = 0; i < files_cartas.length; i++) {
      formData.append('cartas', files_cartas.item(i)) 
  };
  console.log(formData.getAll('cartas'))
    


  formData.append('portaria', files_portaria[0], files_portaria[0].name)
  console.log(formData.getAll('portaria'))
    
  $.ajax({
      type: 'POST',
      url: '/upload',
      data: formData,
      contentType: false,
      cache: false,
      processData: false,
      success: function(data) {
          console.log('Success!');
      },
      error: function(data){
        console.log("Error !!");
    }
  });

}
  



  






