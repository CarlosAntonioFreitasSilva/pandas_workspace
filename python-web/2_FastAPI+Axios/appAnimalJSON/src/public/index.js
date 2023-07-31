async function carregarAnimais() {
    const response = await axios.get('http://localhost:8000/animais')
    
    const animais = response.data

    const lista = document.getElementById('lista-animais')

    animais.forEach(animal =>{
    const item = document.createElement('li')
    item.innerText =  "Nome: " + animal.nome + "\nCor: " + animal.cor + "\nSexo: " + animal.sexo + "\nIdade: " + animal.idade

    lista.appendChild(item)
    })   
}

function manipularFormulario(){
    const form_animal = document.getElementById('form-animal')
    const input_nome = document.getElementById('nome')
    const input_idade = document.getElementById('idade')
    const input_sexo = document.getElementById('sexo')
    const input_cor = document.getElementById('cor')
    form_animal.onsubmit = async ()=>{

        await axios.post('http://127.0.0.1:8000/animais',{
            nome : input_nome.value,
            idade:input_idade.value,
            sexo: input_sexo.value,
            cor: input_cor.value
        })
    }
}

function app() {
    console.log('App iniciada')
    carregarAnimais()
    manipularFormulario()
}

app()