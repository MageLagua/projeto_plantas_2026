# **Projeto de reconhecimento de plantas**

Esse é um trabalho para a matéria de Serviços de Software da pós graduação de Ciência de Dados e Inteligência Artificial do Instituto Mauá de Tecnologia.

Alunas:
- Nome: Fernanda Ramos
- RA: 25.80198-6
- Nome: Maria Eugênia Lagua
- RA: 12.00311-5

## Estrutura

O projeto tem a seguinte estrutura:

- Um container para um app gradio-prototype que irá apresentar a interface ainda como protótipo para a seleção de um arquivo de imagem para upload
- Um container bff-api que será um Back-For-Front responsável por orquestrar todas as chamadas para o serviço e devolver para o front a informação que ele precisa
- Um container plantnet-api que será responsável por receber o nosso arquivo, buscar na api https://identify.plantnet.org/pt-br e responder qual o nome científico da planta da imagem
- Um container db-api que será o banco de dados com a informação do nome em português e a informação sobre a planta ser venenosa para gatos e cachorros ou não

> O objetivo inicial era utilizar a API https://perenual.com/ que já diz se a planta é venenosa ou não, porém essa API não retornou em tempo hábil nosso pedido de chave de acesso. Então utilizamos o banco de dados que criamos na matéria de Inteligência de Negócio do primeiro módulo da pós-graduação.

### **Gradio Prototype**

- Esse container será um protótipo de frontend apenas para testes iniciais do backend, depois será criado um novo projeto com o frontend final.
- Ele irá utilizar a biblioteca Gradio do python para montar os componentes.
- Ele deve chamar o container bff-api enviando a imagem e apresentar depois a resposta do nome da planta e se ela é venenosa para gatos ou chachorros
- Caso ocorra algum erro no processo isso também será apresentado ao usuário

### **Back-For-Front API**

- Esse container será um Back-For-Front que irá orquestrar as duas outras APIs e retornar o que o front precisa.
- Ele deve chamar o container plantnet-api enviando a imagem para pegar depois o nome científico da planta identificada ou um erro
- Depois ele irá utilizar o nome encontrado na chamada anterior para buscar no db-api o nome em português da planta e se ela é venenosa para gatos ou cachorros ou um erro
- Por último ela irá retornar essas 3 informações ao front

### **Pl@ntNet API**

- Esse será o container que irá realizar a chamada para a API https://identify.plantnet.org/pt-br no endpoint https://my-api.plantnet.org/v2/identify/{project}
- A documentação da API se encontra em https://my.plantnet.org/doc/api/openapi
- Esse container deve enviar a imagem recebida pelo front à API e retornar apenas o nome da planta que vem na variável "bestMatch" da resposta.

### **DB API**

- Esse container será responsável por subir um banco de dados com as informações de flores do arquivo flowers.csv
- Ele tem um endpoint que lista todas as flores do banco que não será utilizado no projeto e é apenas para demonstração
- Ele terá outro endpoint, esse utilizado no projeto, para retornar a primeira flor da lista cujo nome científico seja próximo ao nome encontrado pelo Pl@antNet