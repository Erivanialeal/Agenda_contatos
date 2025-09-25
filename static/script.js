
// Espera o DOM carregar para evitar erro de elemento não encontrado.
document.addEventListener("DOMContentLoaded", () => {
    // selecionar o botão com id.
    document.getElementById("btn-pesquisar").addEventListener("click" , function(){
        console.log("Botão pesquisar foi clicado");
        //pegamos o valor digitado no campo.
        const nome =document.getElementById("area-input").value;

        // fazemos a reuquisição GET para o Backend.
        fetch(`/contatos/pesquisar?nome=${encodeURIComponent(nome)}`)
            .then(response => {
                if (!response.ok){
                    throw new Error("Erro na requisição");
                }
                return response.json(); // transforma resposta em um objeto json

            })
            .then(data => {
                // mostar o resultado na tela
                const saida = document.getElementById("saida");
                if (data.erro){
                    saida.innerText = data.erro; //exibi a mensagem de erro
                } else{
                    // preecher os campos  individualmente
                    document.getElementById("nome").textContent=`Nome: ${data.nome}`;
                    document.getElementById("telefone").textContent=`Telefone:${data.telefone}`;
                    document.getElementById("email").textContent=`Email:${data.email}`;
                }
            })
            .catch(erro => {
                console.error("Erro:", erro);
            })
    })

});