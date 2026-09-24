# Aula-4-COMP.NUV

##Aula-4---Virtualização-e-Contêineres-na-Nuvem
Este repositório tem como objetivo documentar as atividades práticas e reflexões propostas na disciplina de Sistemas Distribuídos, servindo como registro de aprendizado e evidência das práticas realizadas em laboratório. Sinta-se à vontade para explorar os arquivos e acompanhar a evolução dos conceitos ao longo do semestre.

O que foi proposto em aula
A quarta aula teve como foco apresentar os conceitos de Virtualização e Contêineres na Nuvem, mostrando como vários ambientes podem compartilhar o mesmo hardware com isolamento.

## Atividade Prática — Nosso Primeiro Contêiner
Vamos executar um servidor web Nginx dentro de um contêiner Docker.

Ambiente: Killercoda
Versão do ambiente: Ubuntu 24.04

Plataforma: Killercoda (gratuito, navegador, sem instalação local)

Sistema Operacional do ambiente: Ubuntu 24.04

Acesso: https://killercoda.com/learn

⚠️ Importante: O ambiente do Killercoda utilizado nesta prática é baseado no Ubuntu 24.04. Isso significa que os comandos e comportamentos observados seguem as características dessa versão do sistema operacional. Não utilize senhas, tokens ou dados reais no laboratório. O ambiente gratuito é temporário.


Passo 1: Acessar o ambiente
Acesse https://killercoda.com/learn

Faça login com sua conta gratuita

Procure um cenário de Docker / Containers (ambiente Ubuntu 24.04)

Abra o terminal do cenário e aguarde o ambiente ficar pronto

Passo 2: O Docker está funcionando?
bash
docker --version
docker info | head
Se aparecer a versão do Docker e informações do engine, o ambiente está pronto.

Pergunta: O Docker está instalado no computador da sala ou no ambiente remoto? → No ambiente remoto (Killercoda / Ubuntu 24.04).

Passo 3: Primeiro contêiner
bash
docker run hello-world
O Docker procura a imagem. Se ela não estiver localmente, faz o download e cria um contêiner para executá-la. Acabamos de executar nosso primeiro contêiner.

Passo 4: Quais imagens temos?
bash
docker images
Observe as colunas REPOSITORY, TAG, IMAGE ID e SIZE. A imagem é o modelo usado para criar contêineres.

Anote: Qual imagem apareceu e qual é o tamanho informado?

Passo 5: Subir um servidor web
bash
docker run -d --name web-aula4 -p 8080:80 nginx:alpine
-d → executa em segundo plano

--name web-aula4 → define o nome do contêiner

-p 8080:80 → conecta a porta 8080 do ambiente à porta 80 do contêiner

nginx:alpine → imagem utilizada

Temos agora um servidor web executando dentro de um contêiner.

Passo 6: Verificar o contêiner
bash
docker ps
Localize: CONTAINER ID, IMAGE, STATUS, PORTS, NAMES. Você deverá encontrar o contêiner web-aula4 em execução.

Passo 7: Testar o serviço
bash
curl localhost:8080
Se aparecer HTML da página padrão do Nginx, o servidor respondeu corretamente.

Fluxo: Cliente → porta 8080 → contêiner → Nginx → resposta HTML

Passo 8: Personalizar a página
bash
docker exec web-aula4 sh -c 'echo "<h1>Aula 4 - Computacao em Nuvem</h1><p>Meu primeiro container!</p>" > /usr/share/nginx/html/index.html'
curl localhost:8080
docker exec executa um comando dentro de um contêiner que já está em funcionamento. Se o novo HTML apareceu, você alterou a aplicação dentro do contêiner.

Passo 9: Observar recursos
bash
docker stats --no-stream
Observe CPU %, MEM USAGE / LIMIT e NET I/O. Esses recursos vêm do ambiente hospedeiro.

Conexão com nuvem: Recursos precisam ser medidos, alocados e gerenciados.

Passo 10: Encerrar corretamente
Na nuvem, recursos que não são necessários devem ser encerrados.

bash
docker stop web-aula4
docker rm web-aula4
docker ps -a
stop → interrompe a execução

rm → remove o contêiner

ps -a → mostra contêineres ativos e parados

Boa prática: Não manter recursos desnecessários em execução.
