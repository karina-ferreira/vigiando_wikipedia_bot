# Vigiando a Wikipédia Bot 🔎

Esse repositório contém o código do trabalho da disciplina de Projeto Final do Master em Jornalismo de Dados, Automação e Data Storytelling do Insper (2022-23). O robô serve para fazer algumas análises sobre verbetes escolhidos da Wikipédia, solicitadas por meio do envio de uma mensagem ao bot do Telegram [Vigiando a Wikipédia 🔎](https://t.me/vigiandowiki_bot). Em seguida, o bot 



* O robô faz uma solicitação para a API da Wikipédia, usando como parâmetro a página de revisões de um verbete que o usuário indicar.
* A API devolve um dicionário, de onde são separados os seguintes dados: data da revisão, usuário que editou, tamanho da edição em caracteres.
* O programa traz como resposta quantas edições foram feitas no verbete e por quantos usuários nos últimos 30 dias. Ele também faz a mesma análise para o período de 30 dias imediatamente anterior. e se , qual usuário editou mais vezes, compara os últimos 30. O programa também indica se entre esses dois períodos houve aumento ou diminuição no tamanho de caracteres do verbete, indicando se as edições foram para acréssimo ou corte. Por fim, a análise entrega a data de criação do verbete e quantas vezes ele foi editado até então.

 
