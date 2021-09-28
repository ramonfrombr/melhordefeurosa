document.addEventListener('DOMContentLoaded', () => {

    /*
        var socket = io();

        socket.on('connect', function() {
            socket.emit('my event', {data: 'I\'m connected!'});
        });
    */
    

    const lista_produtos = [
        {'produto_id': 1,'nome_produto': "🍞 Pão Caseiro Grande", 'preco': 7.0 },
        {'produto_id': 2,'nome_produto': "🍮 Empadinha", 'preco': 2.0 },
        {'produto_id': 3,'nome_produto': "🧃 Suco", 'preco': 1.0 },
        {'produto_id': 4,'nome_produto': "☕️ Cafézinho", 'preco': 1.0 },
        {'produto_id': 5,'nome_produto': "🥐 Croissant", 'preco': 1.0 },
        {'produto_id': 6,'nome_produto': "🥯 Sonho", 'preco': 1.0 },
        {'produto_id': 7,'nome_produto': "🍩 Donut", 'preco': 1.0 },
        {'produto_id': 8,'nome_produto': "🥨 Mentira", 'preco': 1.0 },
        {'produto_id': 9,'nome_produto': "🍪 Cookie", 'preco': 1.0 },
        {'produto_id': 10,'nome_produto': "🥞 Panquecas", 'preco': 1.0 },
        {'produto_id': 11,'nome_produto': "🧁 Cupcake", 'preco': 1.0 },
        {'produto_id': 12,'nome_produto': "🍰 Fatia de Bolo", 'preco': 1.0 },
        {'produto_id': 13,'nome_produto': "🎂 Bolo", 'preco': 1.0 },
        {'produto_id': 14,'nome_produto': "🍬 Bombom", 'preco': 1.0 },
        {'produto_id': 15,'nome_produto': "🥪 Misto", 'preco': 1.0 },
        {'produto_id': 16,'nome_produto': "🌭 Cachorro Quente", 'preco': 1.0 },
        {'produto_id': 3,'nome_produto': "🍔 Hamburger", 'preco': 1.0 },
        {'produto_id': 3,'nome_produto': "🍕 Fatia de Pizza", 'preco': 1.0 },
    ]

    for(let produto of lista_produtos) {
        console.log(produto);
    }


    class FormularioNovoPedido {

        // Recebe um vetor de objetos (produtos)
        constructor(lista_produtos) {

            // Declara o valor total do pedido em reais R$
            this.valor_total = 0;

            function criar_formulario() {

                let formulario = document.createElement('div');

                formulario.style.marginBottom = '3em';
                formulario.style.padding = '1em';
                formulario.style.backgroundColor = 'rgb(250, 250, 250)';
                
                formulario.append(criar_menu_adicionar_itens());

                formulario.append(criar_lista_itens());

                return formulario;
            }

            function criar_menu_adicionar_itens() {

                let menu = document.createElement('div');

                menu.style.display = 'flex';
                menu.style.justifyContent = 'space-between';
                menu.style.marginBottom = '20px';


                menu.append(new ListaProdutos(lista_produtos));

                menu.append(new BotaoAdicionarItem());

                return menu;
            }

            function criar_lista_itens() {
                
                let lista = document.createElement('div');

                lista.setAttribute('id', 'lista-itens');

                return lista;
            }
            
            return criar_formulario();
        }
    }

    class ListaProdutos {

        constructor(lista) {

            // Cria o elemento
            this.lista = document.createElement('select');

            // Estilo
            this.lista.style.width = '100%';
            this.lista.style.height = '1.5em';
            this.lista.style.fontSize = '1.8em';

            // ID
            this.lista.setAttribute('id', 'lista-produtos');

            // Para cada produto no vetor de produtos
            for(let produto of lista) {
                
                function criar_opcao_lista_produtos(produto) {

                    let opcao = document.createElement('option');

                    opcao.dataset.produto_id = produto.produto_id;
                    opcao.dataset.nome_produto = produto.nome_produto;
                    opcao.dataset.preco = produto.preco;

                    opcao.value = produto.produto_id;
                    opcao.innerText = `${produto.nome_produto} (R$ ${produto.preco})`;
            
                    return opcao;
                }

                let opcao = criar_opcao_lista_produtos(produto);

                console.log(opcao);

                // Adicione o produto como sendo uma opção da lista
                this.lista.append(opcao);
            }

            return this.lista;
        }
    }

    class BotaoAdicionarItem {

        constructor() {

            this.botao = criar_botao_adicionar_item();

            function criar_botao_adicionar_item() {

                // Cria o elemento
                let botao = document.createElement('button');

                // Estiliza
                botao.style.color = 'white';
                botao.style.fontSize = '1.5em';
                botao.style.fontWeight = 'bold';
                botao.style.backgroundColor = 'green';
                botao.style.border = 'none';
                botao.style.width = '2em';
                botao.style.marginLeft = '10px';

                // ID
                botao.setAttribute('id', 'botao_adicionar_item');

                // Conteúdo
                botao.innerText = '+';


                botao.addEventListener('click', () => {

                    let lista_produtos = document.getElementById('lista-produtos');
    
                    let lista_itens = document.getElementById('lista-itens');
    
                    let opcao_selecionada = lista_produtos.options[lista_produtos.selectedIndex];
    
                    let item =  new ItemNovoPedido(opcao_selecionada);
                    
                    lista_itens.append(item);
                });

                return botao;
            }

            return this.botao;
        }
    }

    class ItemNovoPedido {

        constructor(produto) {
    
            this.item = criar_item();

            function criar_item() {

                let item = document.createElement('div');

                item.style.display = 'flex';
                item.style.justifyContent = 'space-between';
                item.style.backgroundColor = 'rgb(255, 255, 255)';
                item.style.border = '1px solid #E2E2E2';
                item.style.borderRadius = '5px';
                item.style.padding = '5px';
                item.style.marginBottom = '5px';

                item.append(criar_nome_produto());
                item.append(criar_opcoes());

                return item;
            }

            function criar_nome_produto() {

                // Cria o elemento
                let nome = document.createElement('div');

                // Define o ícone + nome
                nome.innerText = `${produto.dataset.nome_produto} (R$ ${produto.dataset.preco})`;

                // Estilo
                nome.style.marginRight = '1em';

                return nome;
            }

            function criar_opcoes() {

                let opcoes = document.createElement('div');

                opcoes.append(criar_input_quantidade());
                opcoes.append(criar_botao_remover_item());

                return opcoes;
            }
   
            function criar_input_quantidade() {

                // Cria o elemento
                let input = document.createElement('input');

                // Estilo
                input.style.width = '3em';

                // Produto ID
                input.dataset.produto_id = produto.dataset.produto_id;

                // Tipo de input
                input.setAttribute('type', 'number');

                // Valor do input
                input.value = 1;

                
                // Quando o valor do input for alterado
                input.addEventListener('change', (evento) => {

                    console.log('Quantidade do produto <' + produto.dataset.nome_produto + '> alterada: ' + evento.target.value);
                })

                return input;
            }

            function criar_botao_remover_item() {

                let botao = document.createElement('button');

                botao.innerHTML = '&times;';
                botao.style.border = 'none';
                botao.style.marginLeft = '10px';
                botao.style.color = 'white';
                botao.style.fontWeight = 'bold';
                botao.style.backgroundColor = 'red';
        
                botao.addEventListener('click', (evento) => {
                    evento.target.parentNode.parentNode.remove();
                })

                return botao;
            }

            return this.item;
        }
    }

    class BotaoConfirmarPedido {
        constructor() {

        }
    }

    class SubTotal {
    
    }
    

    // Cria uma nova instância de formulário de novo pedido
    let formularioNovoPedido = new FormularioNovoPedido(lista_produtos);

    // Seleciona a div container
    let container_formulario = document.getElementById('container_formulario');

    // Cria o formulário e anexa no container
    container_formulario.append(formularioNovoPedido);

});




