document.addEventListener('DOMContentLoaded', () => {

    console.log("Início do script");

    // COMPONENTES

    class ListaProdutos {

    }

    class Pedido {

    }

    class Entrega {

    }

    class Unidade {

    }

    class PontoDeVenda {

    }

    class Entregador {

    }

    class Produto {

    }

    class Producao {

    }








    class Modal {

        constructor(conteudo="Este é um modal") {
            
            /* Cria os elementos */
            this.modal = document.createElement('div');
            this.modal.setAttribute('id', 'modalSimples');
            this.modal.classList.add('janela-modal');

            this.conteudo_modal = document.createElement('div');
            this.conteudo_modal.classList.add('conteudo-modal');
            this.conteudo = conteudo;

            this.botao_fechar_modal = document.createElement('span');
            this.botao_fechar_modal.classList.add('botao-fechar-modal');
            this.botao_fechar_modal.innerHTML = '&times;';

            this.botao_fechar_modal.addEventListener('click', (evento) => {
                this.destruir();
            });



            /* Anexa os elementos */
            this.modal.append(this.conteudo_modal);
            this.conteudo_modal.append(this.botao_fechar_modal);
            this.conteudo_modal.append(this.conteudo);

            /* */
            /*return this.modal;*/

        }

        gerar_elemento() {
            return this.modal;
        }

        definir_mensagem (mensagem) {
            this.mensagem.innerText = mensagem;
        }

        destruir() {

            let elemento_pai = this.modal.parentNode;

            elemento_pai.removeChild(this.modal);
        }
    }

    class Publicacao {

        constructor(titulo, conteudo, autor="Desconhecido", data_criacao="01/01/2000") {
            
            /* Cria os elementos */
            this.publicacao = document.createElement('div');


            /* DEBUG */
            this.container_debug = document.createElement('div');
            this.botao_logar_conteudo = document.createElement('span');
            this.botao_alterar_conteudo = document.createElement('span')

            /* CONTAINER OPÇÕES */
            this.container_opcoes = document.createElement('div');
            this.botao_apagar = document.createElement('span');
            this.botao_editar = document.createElement('span');

            /* CONTAINER INFO */
            this.container_info = document.createElement('div');
            this.autor = document.createElement('span');
            this.data_criacao = document.createElement('span');

            /* TÍTULO E CONTEÚDO */
            this.container_titulo = document.createElement('h4');
            this.titulo = titulo;
            this.container_conteudo = document.createElement('div');
            this.conteudo = conteudo;
            
            /* Atribui classes CSS */

            /* DEBUG */
            this.container_debug.classList.add('container-opcoes-publicacao');
            this.botao_alterar_conteudo.classList.add('botao-editar-publicacao');
            this.botao_logar_conteudo.classList.add('botao-editar-publicacao');

            /* CONTAINER OPÇÕES */
            this.container_opcoes.classList.add('container-opcoes-publicacao');
            this.botao_editar.classList.add('botao-editar-publicacao');
            this.botao_apagar.classList.add('botao-apagar-publicacao');
            
            /* CONTAINER INFO */

            this.data_criacao.classList.add('span-data-criacao-publicacao');
            this.autor.classList.add('span-autor-publicacao');

            /* TÍTULO E CONTEÚDO */
            this.publicacao.classList.add('publicacao');
            this.container_titulo.classList.add('titulo-publicacao');
            this.container_conteudo.classList.add('conteudo-publicacao');

            /* Preenche elementos com as informações */

            /* DEBUG */
            this.botao_alterar_conteudo.innerText = "Alterar Conteúdo";
            this.botao_logar_conteudo.innerText = "Logar Conteúdo";

            this.botao_apagar.innerHTML = 'Apagar &times;';
            this.botao_editar.innerText = 'Editar';

            this.autor.innerText = autor;
            this.data_criacao.innerText = data_criacao;

            this.container_titulo.innerText = this.titulo;
            this.container_conteudo.innerHTML = this.conteudo;

            /* Anexa os elementos */

            /* DEBUG */
            this.publicacao.append(this.container_debug);
            this.container_debug.append(this.botao_logar_conteudo);
            this.container_debug.append(this.botao_alterar_conteudo);

            this.publicacao.append(this.container_opcoes);
            this.container_opcoes.append(this.botao_editar);
            this.container_opcoes.append(this.botao_apagar);

            this.publicacao.append(this.container_info);
            this.container_info.append(this.autor);
            this.container_info.append(this.data_criacao);

            this.publicacao.append(this.container_titulo);
            this.publicacao.append(this.container_conteudo);




            this.botao_alterar_conteudo.addEventListener('click', () => {

                console.log("Botão alterar conteúdo clicado.");
                this.alterar_conteudo();
            });

            this.botao_logar_conteudo.addEventListener('click', () => {
                this.logar_conteudo();
            });

            /* Quando o botão APAGAR for clicado */
            this.botao_apagar.addEventListener('click', () => {

                this.destruir();
            });


            /* Quando o botão EDITAR for clicado */
            this.botao_editar.addEventListener('click', () => {

                let formulario_edicao = document.createElement('form');
                let container_titulo = document.createElement('div');
                let container_conteudo = document.createElement('div');
                let input_titulo = document.createElement('input');
                let textarea_conteudo = document.createElement('textarea');



                input_titulo.value = this.titulo;

                textarea_conteudo.value = this.conteudo;




                formulario_edicao.append(container_titulo);
                container_titulo.append(input_titulo);

                formulario_edicao.append(container_conteudo);
                container_conteudo.append(textarea_conteudo);

                let modal = new Modal(formulario_edicao);

                let main = document.getElementById('main');

                main.appendChild(modal.gerar_elemento());

            });

        }

        gerar_elemento() {
            return this.publicacao;
        }

        selecionar_titulo() {
            return this.titulo;
        }

        selecionar_conteudo() {
            return this.conteudo;
        }


        definir_titulo (titulo) {
            this.titulo = titulo;
            this.container_titulo.innerText = this.titulo;
        }

        definir_conteudo (conteudo) {
            this.conteudo = conteudo;
            this.container_conteudo.innerHTML = this.conteudo;
        }


        alterar_conteudo() {

            let titulo_alterado = this.conteudo;

            let conteudo_alterado = this.titulo;

            this.definir_titulo(titulo_alterado)

            this.definir_conteudo(conteudo_alterado);

        }

        logar_conteudo() {
            console.log(this.conteudo);
        }

        destruir() {

            /*this.publicacao.classList.add('publicacao-desaparecendo');*/

            let elemento_pai = this.publicacao.parentNode;

            elemento_pai.removeChild(this.publicacao);
        }
    }

    /* NÃO FINALIZADA */
    class Comentario {

        constructor(comentario, autor="Desconhecido", data_criacao = new Date()) {

        }
    }

    /* NÃO FINALIZADA */
    class Tag {

        constructor(nome) {
            
            /* Cria os elementos */
            this.tag = document.createElement('span');

            this.icone = document.createElement('i');

            this.nome = document.createElement('span');


            /* Anexa os elementos */
            this.publicacao.append(this.container_info);

        }

        gerar_elemento() {
            return this.publicacao;
        }

        destruir() {

            let elemento_pai = this.modal.parentNode;

            elemento_pai.removeChild(this.modal);
        }

    }







    let botao_modal = document.getElementById('botaoModal');

    botao_modal.addEventListener('click', (evento) => {

        evento.preventDefault();

        let mensagem = document.getElementById('mensagemModal');

        let modal = new Modal(mensagem.value);

        let main = document.getElementById('main');

        main.appendChild(modal.gerar_elemento());
    });


    let botao_publicacao = document.getElementById('botaoPublicacao');

    botao_publicacao.addEventListener('click', (evento) => {

        evento.preventDefault();

        let titulo_publicacao = document.getElementById('tituloPublicacao').value;

        let conteudo_publicacao = document.getElementById('conteudoPublicacao').value;

        let publicacao = new Publicacao(titulo_publicacao, conteudo_publicacao);

        let publicacoes = document.getElementById('publicacoes');

        publicacoes.append(publicacao.gerar_elemento());
    });

    console.log("Fim do script");
});