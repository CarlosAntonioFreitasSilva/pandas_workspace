async function carregarPessoas() {
    const response = await axios.get('http://localhost:8000/pessoas')
    
    const pessoas = response.data

    console.log(pessoas)
    const lista = document.getElementById('lista-pessoas')

    pessoas.forEach(pessoa =>{
    const item = document.createElement('li')
    item.innerText =  "Nome: " + pessoa[1] + "\nCPF: " + pessoa[2]

    lista.appendChild(item)
    })   
}

function gravarFormulario(){
    const form_pessoa = document.getElementById('form-pessoa')
    const input_nome = document.getElementById('nome')
    const input_cpf = document.getElementById('cpf')
    form_pessoa.onsubmit = async ()=>{

        await axios.post('http://127.0.0.1:8000/pessoas',{
            nome : input_nome.value,
            cpf:input_cpf.value
        })
    }
}

function app() {
    console.log('App iniciada')
    carregarPessoas()
    gravarFormulario()
}

app()