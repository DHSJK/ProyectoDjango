document.addEventListener('DOMContentLoaded', function() {
let imagenes = [
    {img: 'app/../img/donacion_2.jpg'},
    {img: '../img/donacion_3.jpg'},
    {img: './img/donacion_1.jpg'},
    {img: './img/donacion_4.jpg'},
    {img: './img/donacion_5.jpg'},
    {img: './img/donacion_6.jpg'},
    {img: './img/donacion_7.jpg'},
    {img: './img/donacion_8.jpg'},
    {img: './img/donacion_9.jpg'}
]
let contador = 0
const contenedor = document.querySelector('.slideshow');
const overlay = document.querySelector('.overlay');
const galeria_imagenes = document.querySelectorAll('.galeria img');
const img_slideshows = document.querySelector('.slideshow img');


contenedor.addEventListener('click', function(event) {
    let atras = contenedor.querySelector('.atras'),
        adelante = contenedor.querySelector('.adelante'),
        img = contenedor.querySelector('img'),
        tgt = event.target
    if (tgt == atras) {
        if (contador > 0) {
            img.src = imagenes[contador - 1].img
            contador--
        } else {
            img.src = imagenes[imagenes.length - 1].img
            contador = imagenes.length - 1
        }
    } else if (tgt == adelante) {
        if (contador < imagenes.length - 1) {
            img.src = imagenes[contador + 1].img
            contador++
        } else {
            img.src = imagenes[0].img
            contador = 0
        }
    }

})
Array.from(galeria_imagenes).forEach(img => {
    img.addEventListener('click', event => {
        const imagen_seleccionada = +(event.target.dataset.imgMostrar)
        img_slideshows.src = imagenes[imagen_seleccionada].img
        contador = imagen_seleccionada
        overlay.style.opacity = 1
        overlay.style.visibility = 'visible'
    })
})

var span = document.getElementsByClassName("btn_cerrar")[0];
span.onclick = function() {
    overlay.style.visibility = "hidden";
}
})