// Espera o DOM carregar para evitar erro de elemento não encontrado.
document.addEventListener("DOMContentLoaded", () => {
    // Botão de pesquisar contato
    document.getElementById("btn-pesquisar").addEventListener("click", function () {
        console.log("Botão pesquisar foi clicado");

        // Pega o valor digitado no campo de entrada
        const nome = document.getElementById("area-input").value;

        // Faz a requisição GET para o backend
        fetch(`/contatos/pesquisar?nome=${encodeURIComponent(nome)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Erro na requisição");
                }
                return response.json(); // Transforma resposta em objeto JSON
            })
            .then(data => {
                // Seleciona o container onde os dados serão exibidos
                const saida = document.getElementById("saida");
                const btnExcluir = document.getElementById("btn-excluir");

                // Garante que o container esteja visível
                saida.style.display = "block";

                // Verifica se houve erro na resposta
                if (data.erro) {
                    // Exibe a mensagem de erro nos campos individuais
                    document.getElementById("nome").textContent = data.erro;
                    document.getElementById("telefone").textContent = "";
                    document.getElementById("email").textContent = "";

                    // Esconde o botão "Excluir" caso haja erro
                    if (btnExcluir) {
                        btnExcluir.classList.remove("mostrar");
                    }
                } else {
                    // Preenche os campos com os dados do contato
                    document.getElementById("nome").textContent = `Nome: ${data.nome}`;
                    document.getElementById("telefone").textContent = `Telefone: ${data.telefone}`;
                    document.getElementById("email").textContent = `Email: ${data.email}`;

                    // Exibe o botão "Excluir" e armazena o ID do contato
                    if (btnExcluir) {
                        btnExcluir.classList.add("mostrar"); // Aplica a classe que torna o botão visível
                        btnExcluir.setAttribute("data-id", data.id); // Armazena o ID para futura exclusão
                        console.log("Classe do botão:", btnExcluir.className); // Verificação no console
                    } else {
                        console.log("Botão não encontrado");
                    }
                }

                // Log para verificar os dados recebidos
                console.log("Dados recebidos:", data);
            })
            .catch(error => {
                console.error("Erro na requisição:", error);
            });
    });

    // Botão de adicionar contato (salvar)
    document.getElementById("btn-salvar").addEventListener("click", function () {
        // Pega os valores adicionados nos campos
        const nome = document.getElementById("input-nome").value;
        const telefone = document.getElementById("input-telefone").value;
        const email = document.getElementById("input-email").value;

        // Cria o objeto com os dados do novo contato
        const novoContato = {
            nome: nome,
            telefone: telefone,
            email: email
        };

        // Faz a requisição POST para adicionar o contato
        fetch("/contatos/adicionar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(novoContato)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro ao salvar contato");
            }
            // Sucesso silencioso
        })
        .catch(error => {
            console.error("Erro ao salvar:", error);
        });
    });
});
