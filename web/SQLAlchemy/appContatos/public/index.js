window.onload = function () {

    axios.get('http://127.0.0.1:8000/')
        .then(function (response){
            const list = document.getElementById("list")

            const contacts = response.data

            contacts.forEach(element => {
                const item = document.createElement('li')
                item.innerText = element.nome + "  |  " + element
                .celular

                list.appendChild(item)
            });
        })
        .catch (function (error) {
        // manipula erros da requisição
        console.error(error);
    })
            .finally(function () {
        // sempre será executado
    });
    

    document.getElementById("form").onsubmit = function () {

        const nome = document.getElementById('nome')
        const celular = document.getElementById('celular')

        axios.post('http://127.0.0.1:8000/gravar/', {
            nome: nome.value,
            celular: celular.value
        })
            .then(function (response) {
                // manipula o sucesso da requisição
                console.log(response);
            })
            .catch(function (error) {
                // manipula erros da requisição
                console.error(error);
            })
            .finally(function () {
                // sempre será executado
            });
    }



}