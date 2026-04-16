# **Projeto de reconhecimento de plantas**

Esse é um trabalho para a matéria de Serviços de Software da pós graduação de Ciência de Dados e Inteligência Artificial do Instituto Mauá de Tecnologia

## Estrutura

O projeto tem a seguinte estrutura:

- Um container para um app gradio-prototype que irá apresentar a interface ainda como protótipo para a seleção de um arquivo de imagem para upload
- Um container api-plantnet que será responsável por receber o nosso arquivo, buscar na api https://identify.plantnet.org/pt-br e responder qual a planta da imagem

### **Gradio Prototype**

- Esse container será um protótipo de frontend apenas para testes iniciais do backend, depois será criado um novo projeto com o frontend final.
- Ele irá utilizar a biblioteca Gradio do python para montar os componentes.
- Ele deve chamar o container api-plantnet enviando a imagem e apresentar depois a resposta do nome da planta que aparece na imagem ou um erro.

**API plantnet**

- Esse será o container que irá realizar a chamada para a API https://identify.plantnet.org/pt-br no endpoint https://my-api.plantnet.org/v2/identify/{project}
- A documentação da API se encontra em https://my.plantnet.org/doc/api/openapi
- Esse container deve enviar a imagem recebida pelo front à API e retornar apenas o nome da planta que vem na variável "bestMatch" da resposta.