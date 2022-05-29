
console.log('data ok')
var regiones = []
var comunas = []
fetch('https://apis.digital.gob.cl/dpa/regiones/')
.then(response => response.json())
.then((data) =>{ console.log(data)
    let options = data.map((item)=>{return `<option value="${item.nombre}">${item.nombre}</option>`})
    options = options.join('')
    //console.log(options)
    let select = `<select onchange='setcomunas(this.value)' name="cars" id="cars" class="form-control" form="carform" >${options}</select>`
    console.log('cargada regiones')
    document.getElementById('formulario').innerHTML = select
    //console.log('regiones cargadas')
    regiones = data
});

fetch(`https://apis.digital.gob.cl/dpa/comunas`)
.then(response => response.json())
.then((data) =>{ //console.log(data)
    console.log('cargadas comuna')
    comunas = data
});

var setcomunas = (region)=>{
    console.log(region,regiones)
    let id
    for(let i=0;i<regiones.length;i++){
        if(region===regiones[i].nombre){
            id = regiones[i].codigo
            break
        }
    }
    let data = []
    for(let i=0;i<comunas.length;i++){
        let cod = comunas[i].codigo
        console.log(id)
        if(id===comunas[i].codigo.substr(0,2)){
            data.push(comunas[i])
        }
    }
    console.log(data)
    //data = data.join('')
    let options = data.map((item)=>{return `<option value="${item.nombre}">${item.nombre}</option>`})
    options = options.join('')
    console.log(options)
    let select = `<select name="cars" id="cars" form="carform" class="form-control">${options}</select>`
    document.getElementById('comunas').innerHTML = select
}


// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();
















