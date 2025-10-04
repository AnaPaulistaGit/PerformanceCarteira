### Projeto: Performance de Carteira de Investimentos

Este projeto tem como finalidade coletar, processar e visualizar dados do mercado financeiro de forma simples e interativa. 
Utilizando Python com bibliotecas como Pandas, yFinance e Streamlit, ele permite acompanhar índices como o IBOV e avaliar retornos históricos de forma prática.


### Objetivo do projeto Dashboard de ações: </br>

Este projeto representa a união de tecnologia e finanças, mostrando como a análise de dados pode ser aplicada para transformar informações em insights valiosos. E mais:

🚀 Automatização inteligente: elimina a necessidade de buscar dados manualmente em diversas fontes.

📈 Análises claras e objetivas: gráficos e métricas que traduzem rapidamente a performance do mercado.

💡 Acessível e didático: ideal tanto para estudantes quanto para profissionais de finanças e tecnologia.

⚡ Interatividade com Streamlit: uma interface leve que facilita a exploração dos resultados em tempo real.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
#### Manual de Funcionamento - App Preço de açoes
1. Objetivo do app </br>
O aplicativo permite visualizar a evolução histórica dos preços das ações do IBOV e calcular a performance individual e da carteira em um período selecionado.</br>

2. Passo a passo de uso</br>
🔹 Tela Inicial</br>
O app exibe um título e uma breve descrição. Em seguida, os dados das ações começam a ser carregados (pode levar alguns segundos).</br>
🔹 Menu Lateral (Filtros)</br>
Seleção de Ações: Escolha uma ou mais ações da lista disponível. Caso não selecione nenhuma, todas as ações serão exibidas.
Seleção de Período: Ajuste o intervalo de datas para analisar o comportamento das ações no tempo.</br>
🔹 Gráfico </br>
Exibe a variação dos preços das ações escolhidas no período definido.</br>
🔹 Performance</br>
O app calcula e apresenta: A performance individual de cada ativo. A performance consolidada da carteira com todos os ativos selecionados. </br>

Os resultados aparecem destacados em verde (positivo) ou vermelho (negativo).

Clique [aqui](https://performancecarteiraibov.streamlit.app/) e veja como funciona.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
#### Entendendo o desenvolvimento do aplicativo e suas ferramentas

#### Streamlit: como compartilhar uma aplicação de dados facilmente
Já pensou em conseguir tornar seu projeto de dados uma aplicação web apenas utilizando a linguagem Python? 
O Streamlit é um framework de código aberto, criado justamente para ajudar cientistas de dados a colocarem em produção seus projetos sem a necessidade de conhecer ferramentas de front-end ou de deploy de aplicações.
Por meio desse framework é possível transformar um projeto de ciência de dados e machine learning em uma aplicação interativa. 
Para essa aplicação é gerada uma URL pública que, ao ser compartilhada, permite que qualquer pessoa consiga acessar e usufruir sem necessariamente ter que conhecer o código que está por trás.

Considerando todas essas características do Streamlit, essa ferramenta se torna uma excelente maneira de apresentar projetos técnicos para pessoas que são leigas na área. 
Além de deixar a apresentação com uma aparência muito profissional. Para o desenvolvimento do projeto a seguir, será utilizado o editor de código Visual Studio Code.

#### Configurando o ambiente
Para começar, vamos criar um ambiente virtual onde iremos instalar as bibliotecas que serão utilizadas no desenvolvimento do projeto. 
Podemos criar uma pasta onde ficarão os arquivos do nosso projeto, nomeá-la como "PerformanceCarteira", por exemplo, e em seguida, acessá-la por meio do editor de código.
Na pasta podemos criar um arquivo chamado requirements.txt para colocar as bibliotecas que queremos instalar no nosso ambiente virtual: </br>
• pandas </br>
• yfinance </br>
• streamlit </br>
• datetime </br>

Depois disso, para criar, ativar e instalar os pacotes no ambiente virtual , podemos abrir o terminal do próprio editor de texto utilizando o atalho Ctrl + J e executar os seguintes comandos:

#### Criando o ambiente:
► python -m venv venv

#### Ativando o ambiente:
No Windows:
► venv\Scripts\activate 

No Linux ou Mac:
► source venv/bin/activate

#### Instalando os pacotes do requirements.txt:
► pip install -r requirements.txt

Com o ambiente configurado, podemos começar a desenvolver o projeto!
Dentro da pasta do projeto, vamos criar um script chamado performancecarteira.py onde iremos digitar o nosso código python. 

import streamlit as st </br>
--escrevendo um título na página </br>
st.title('Bem vindo ao app Performance de Carteira') </br>

Para conseguirmos visualizar esse código em ação, podemos abrir o terminal e digitar o seguinte comando:

streamlit run performancecarteira.py </br>

Após alguns segundos, uma página deve abrir apresentando o texto que escrevemos:  'Bem vindo ao app Performance de Carteira'

Assim, temos nossa primeira aplicação rodando! No entanto, observe que nesse link está escrito localhost:8501, o que indica que nossa aplicação está rodando apenas localmente, ou seja, ela ainda não está disponível na web para outras pessoas acessarem.

Para desenvolver o projeto Dashboar de açoes, foi utilizada uma base de dados inicial chamada ibov.csv. Você pode acessá-lo clicando no repositório. Com o arquivo baixado, podemos salvá-lo na pasta do nosso projeto.

No arquivo performancecarteira.py podemos apagar o trecho de código escrito anteriormente e fazer as seguintes importações:
import streamlit as st 
import pandas as pd
import yfinance as yf
from datetime import timedelta

Após isso, vamos construir o código das seguintes funçoes: </br>
carregar_tickers_acoes > A função carregar_tickers_acoes() lê a lista de ações do IBOV em um CSV e retorna seus tickers formatados para consulta no Yahoo Finance. </br>
carregar_dados() > A função carregar_dados baixa e retorna os preços históricos ajustados das ações a partir do Yahoo Finance. </br>

OBS.: veja o codigo fonte das funçoes no arquivo performancecarteira.py

À medida que vamos desenvolvendo nosso projeto, é interessante ir acompanhando o progresso também por meio da visualização da página.
No proximo passo criaremos os elementos graficos que vão interagir com o usuario na nossa pagina:
• Menu lateral (sidebar) com seleção de ações (multiselect) e ajuste de período (slider).
• Gráfico de linha exibindo a evolução dos preços das ações.
• Mensagens visuais destacando performances individuais e da carteira em cores (verde, vermelho ou neutro).
• Alertas informativos em caso de ausência de dados ou durante o carregamento.

Apos desenvolvimento do codigo, criamos um repositorio e fazemos upload do nosso projeto para o GitHub.
Com isso, estamos pronto para fazermos o deploy.


#### Solicitando acesso à nuvem do Streamlit

Para conseguirmos fazer o deploy, precisamos solicitar acesso às máquinas virtuais da nuvem do Streamlit. Essa solicitação é realizada diretamente pela documentação.
E a solicitaçao do serviço de deploy é bem simples, basta seguir o passo a passo apresentado pela plataforma.

Informaremos os dados do nosso projeto no GitHub na página "Deploy an app". Na primeira parte do formulário, devemos colocar o repositório onde está nosso projeto. 
Você pode fazer isso colocando seu nome de usuário do GitHub, uma barra e o nome do repositório, ou ainda pode copiar o link do repositório e colar.

Na segunda parte do formulário, a Branch, não é necessário fazer nenhuma alteração agora. Em "Main file path" devemos colocar o nome do arquivo que está no GitHub com o código principal da nossa aplicação. 
No nosso caso, esse é o performancecarteira.py
Feito o preenchimento do formulário, podemos clicar em "Deploy!" para começar a realizar o deploy da nossa aplicação. Esse processo pode demorar alguns minutos para carregar.
Agora a aplicação está finalizada e pronta para ser compartilhada!

Observe que não temos mais aquela url com "localhost" escrita. Isso indica que a aplicação não está rodando apenas localmente na nossa máquina, mas em uma máquina virtual permitindo que qualquer pessoa consiga acessá-la.

Você pode acessar a aplicação criada neste artigo, clicando [aqui](https://performancecarteiraibov.streamlit.app/).








