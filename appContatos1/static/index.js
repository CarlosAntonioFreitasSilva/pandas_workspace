CONTACTS = []
function show_contacts() {
    axios.post('http://127.0.0.1:8000/contatos')
        .then(function (response) {
            const list = document.getElementById("list")

            const contacts = response.data

            contacts.forEach(element => {
                const item = document.createElement('li')
                item.innerHTML = '<span>' + element.nome + '</span> | <span>' + element
                    .celular + '</span> <div class="controls"> <span class="edit" onclick="edit(event)"> Editar</span> | <span class="delete" onclick="excluir(event)"> Excluir</span> </div>'

                list.appendChild(item)
                CONTACTS.push(element.celular)
            });
        })
        .catch(function (error) {
            // manipula erros da requisição
            console.error(error);
        })
        .finally(function () {
            // sempre será executado
        });
}

function check(celular) {
    return CONTACTS.includes(celular)
}

function submitListener() {
    nome = document.getElementById('nome')
    celular = document.getElementById('celular')

    document.getElementById("form").onsubmit = function () {
        if (check(celular.value)) {
            alert("Esse celular já existe!")
        } else {
            axios.post('http://127.0.0.1:8000/gravar', {
                nome: nome.value,
                celular: celular.value
            })
                .catch(function (error) {
                    // manipula erros da requisição
                    alert(error);
                })
                .finally(function () {
                    alert(response.data)
                });
        }

    }
}

function excluir(event) {
    answer = window.confirm("Tem certeza que deseja excluir esse contato?")
    if (answer)
        nome = event.target.parentNode.parentNode.children[0].innerText
    celular = event.target.parentNode.parentNode.children[1].innerText

    axios.post('http://127.0.0.1:8000/delete', {
        nome: nome,
        celular: celular
    })

    location.reload()
}

function edit(event) {
    nome = event.target.parentNode.parentNode.children[0].innerText
    celular = event.target.parentNode.parentNode.children[1].innerText

    key = event.target.parentNode.parentNode.children[1].innerText

    document.getElementById('nome').value = nome
    document.getElementById('celular').value = celular

    document.getElementById("form").onsubmit = function (event) {
        new_name = document.getElementById('nome').value
        new_phone = document.getElementById('celular').value

        if (new_phone == celular && new_name != nome) {
            axios.post('http://127.0.0.1:8000/update', {
                key: key,
                nome: new_name,
                celular: new_phone
                })
                .catch(function (error) {
                    // manipula erros da requisição
                    alert(error);
                })
                .finally(function () {
                    alert(response.data)
                });
        } else {
            if (check(new_phone)) {
                event.preventDefault()
                alert("Esse número já existe")
            } else {
                alert("Atualizado")
                axios.post('http://127.0.0.1:8000/update', {
                key: key,
                nome: new_name,
                celular: new_phone
                })
                .catch(function (error) {
                    // manipula erros da requisição
                    alert(error);
                })
                .finally(function () {
                    alert(response.data)
                });
            }



        }
    }
}

window.onload = function () {
    show_contacts()
    console.log(CONTACTS)
    submitListener()
}