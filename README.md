# Vigiando a Wikipédia Bot 🔎

Esse repositório contém o código do trabalho da disciplina de Projeto Final da certificação da primeira parte que compõe o Master em Jornalismo de Dados, Automação e Data Storytelling do Insper (2022-23). O robô serve para fazer algumas análises sobre verbetes escolhidos da Wikipédia, solicitadas por meio do envio de uma mensagem ao bot do Telegram <b>[Vigiando a Wikipédia 🔎](https://t.me/vigiandowiki_bot)</b>. A ferramenta pode ser utilizada para acompanhar disputas de narrativas e possíveis interesses em verbetes de pessoas públicas, políticos, fatos históricos, entre outros.

### 📊 · a análise:
* O robô faz uma solicitação para a API da Wikipédia, usando como parâmetro a página de revisões de um verbete que o usuário indicar.
* A API devolve um dicionário, de onde são separados os seguintes dados: data da revisão, usuário que editou, tamanho da edição em caracteres.
* O programa traz como resposta quantas edições foram feitas no verbete e por quantos usuários nos últimos 30 dias. Ele também faz a mesma análise para o período de 30 dias imediatamente anterior. e se , qual usuário editou mais vezes, compara os últimos 30. O programa também indica se entre esses dois períodos houve aumento ou diminuição no tamanho de caracteres do verbete, indicando se as edições foram para acréssimo ou corte. Por fim, a análise entrega a data de criação do verbete e quantas vezes ele foi editado até então.

### 👩‍💻 · o código: 
Para automatizar o código, utilizamos o webhook, recurso que possibilita que um sistema se comunique com outro e ambos troquem dados em tempo real e sem a nossa interferência. Nesse caso, a troca acontece sempre que o bot recebe uma nova mensagem. Por meio de uma página criada com Flask no Render, as funcionalidades ficam disponíveis online. Além da API da Wikipédia, foram usadas a API do Telegram e bibliotecas que estão disponíveis no arquivo `requeriments.txt` deste repositório. 

### 🔮 · a próxima etapa: 
O robô será integrado com o Google Sheets, onde armazenará a pesquisa do usuário. Uma opção será dada para o usuário caso ele queira acompanhar aquela pesquisa e ser notificado quando novas edições forem feitas. Haverá a opção para cancelar a solicitação a qualquer momento que o usuário queira deixar de receber os dados.

### 📧	· contato:
Dúvidas, sugestões ou outras questões, mande um oi para karinaasferreira@gmail.com.

🤖: <b>"Vigiar as narrativas e preservar a memória." - <i> Bot da Vigiando a Wikipédia</i></b>
