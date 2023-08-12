CONTACTS = []

function excluir(event) {
    nome = event.target.parentNode.parentNode.children[0].innerText
    celular = event.target.parentNode.parentNode.children[1].innerText
    answer = window.confirm("Tem certeza que deseja excluir esse contato? \n" + nome + " | " + celular)
    
    if (answer)
        axios.post('http://127.0.0.1:8000/delete', {
            nome: nome,
            celular: celular
        })

        location.reload()
}

