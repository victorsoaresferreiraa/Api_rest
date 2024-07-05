# Projeto API
## Aprendi flask e swagger 
### Como utilizar o Swagger e como configurar 

# Uma API (Application Programming Interface) é um conjunto de regras e definições que permite a comunicação entre diferentes sistemas de software. Em termos simples, é uma interface que permite que um software interaja com outro.

# Aqui estão alguns pontos-chave sobre APIs:

### Interação entre Sistemas: APIs permitem que diferentes aplicações, sistemas ou serviços se comuniquem entre si, compartilhando dados e funcionalidades de maneira segura e eficiente.

### Abstração: Elas fornecem uma camada de abstração, escondendo a complexidade da implementação e expondo apenas as funcionalidades necessárias. Por exemplo, você pode usar uma API para enviar um e-mail sem precisar saber como o servidor de e-mail está implementado.

### Protocolo e Formato: APIs normalmente seguem protocolos e formatos específicos. Por exemplo, as APIs web frequentemente usam HTTP/HTTPS como protocolo e JSON ou XML como formatos de dados.

### EndPoints: APIs são compostas por diversos endpoints, que são URLs específicas que realizam diferentes operações (como obter dados, enviar dados, atualizar dados, etc.). Cada endpoint realiza uma função específica.

### Métodos HTTP: Em APIs web, os métodos HTTP como GET, POST, PUT, DELETE são utilizados para definir a ação a ser realizada. Por exemplo, GET é usado para obter dados, POST para enviar dados, PUT para atualizar dados e DELETE para excluir dados.

### Autenticação e Autorização: Muitas APIs exigem autenticação (verificação de identidade) e autorização (permissão para acessar recursos). Isso pode ser feito através de chaves de API, tokens, OAuth, etc.

## Exemplo Prático
### Vamos considerar um exemplo simples de uma API de um serviço de livros. Esta API pode ter vários endpoints, como:

### GET /books - Para obter uma lista de livros.
### GET /books/{id} - Para obter detalhes de um livro específico pelo seu ID.
### POST /books - Para adicionar um novo livro.
### PUT /books/{id} - Para atualizar informações de um livro específico.
### DELETE /books/{id} - Para deletar um livro específico.


# O que é rest 
### Rest = Maneira de como vamos fazer, protocologo de arquitetura 
### Resfull = Aplicabilidade do rest