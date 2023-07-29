## Documentação - Desafio Pismo

Este é o guia para execução do Desafio Pismo.

### Passo 1: Construir a imagem Docker

Para começar, abra o terminal ou prompt de comando e navegue até a pasta raiz do projeto. Em seguida, execute o seguinte comando para construir a imagem Docker:

docker build -t desafio_pismo .

### Passo 2: Executar o container Docker

Após a construção da imagem Docker, execute o seguinte comando para executar o container interativamente:

docker run -it desafio_pismo

### Passo 3: Executar o script `run_event_dispatcher.sh`

Dentro do container, você estará no diretório `/app`, onde o script `run_event_dispatcher.sh` está localizado. Antes voce pode checar que a pasta de saida dos arquivos esá vazia executando o comando: `ls ../data/output`. Para executar o script, basta digitar o seguinte comando:

./run_event_dispatcher.sh

Os arquivos parquet gerados são salvos na pasta /app/data/output dentro do container apos a execução do comando acima. Agora voce consegue ver os arquivos gerados executando o comando: `ls ../data/output`.

### Passo 4: Copiar os arquivos Parquet gerados

Após a conclusão do processamento, você pode sair do container usando o comando `exit`.

Em seguida, copie os arquivos Parquet gerados do container para a sua máquina local usando o comando mais abaixo. Mas lembre-se de substituir `<CONTAINER_ID>` pelo ID do container em execução (você pode verificar o ID usando o comando `docker ps -a`). Copie e substitua o CONTAINER_ID com a imagem que possui o nome de `desafio_pismo`.

docker cp <CONTAINER_ID>:/app/data/output/ /caminho/para/destino/

### Passo 5: Visualizar os arquivos Parquet

Por fim, você pode visualizar os dados gerados da forma que preferir ou acesse o site [Parquet Viewer Online](https://parquet-viewer-online.com/result) e faça o upload dos arquivos Parquet gerados no diretório de destino para visualizá-los e analisar os dados.

Isso conclui o guia para executar o projeto e visualizar os resultados no Desafio Pismo. Se você seguir os passos acima, poderá processar os eventos, gerar arquivos Parquet e explorar os dados usando o Parquet Viewer Online.

_______________________________

## Documentação - Dificuldades Durante a Contrução do Desafio

### Dificuldade 1: Costrução dos Dados de Input

A principal dificuldade foi encontrar uma maneira de repetir os eventos e colocar mais de um evento distinto na mesma data. Eu pensei em diversas formas, por exemplo criar um script bash e copiar os que ja esistiam com nomes diferentes ou pelo proprio python, no final realizar a cópia. Mas acredito que esta foi a melhor forma.

Depois que fiz a repetição dos eventos ficou um pouco mais fácil aplicar a mesma lógica para colocar pelo menos 2 eventos na mesma data e assim certificar de que no arquivo parquet contemplava os 2 eventso


### Dificuldade 2: Campo `Data` do Json de Entrada

O primeiro problema que tive com o campo "Data" foi de "_corrupt_record" no arquivo parquet. A princípio não identifiquei o que poderia ser. Depois de algumas pesquisas vi que o erro estava ocorrendo devido a um conflito no uso do nome "Data" para se referir a duas coisas diferentes no DataFrame. O campo "data" estava sendo renomeado para um objeto complexo após a leitura do JSON. Para resolver esse problema, renomeei o campo "data" para um nome temporário antes de aplicar a função from_json. Daí apliquei a função from_json nesse campo temporário e, em seguida, renomeei de volta para "data".


### Dificuldade 4: Campo `TimestampType` do Json de Entrada

Eu recebi um erro ao tentar realizar o particionamento

TypeError: Column is not iterable

Para corrigir o erro, precisei criar colunas adicionais que representavam os valores de ano, mês e dia a partir da coluna timestamp, e, em seguida, usei essas colunas para o particionamento.

### Dificuldade 5: `WORKDIR` do Container

No arquivo Dockerfile inicializei o WORKDIR na pasta /app. Como eu estava realizando testes localmente, sempre apresentava erros ao rodar dentro do container. Resolvi adicionar um script conforma a documentação mais acima. Precisei fazer isso para que fosse possível entrar no Container e buscar os arquivos de saída gerados.

## Documentação - Considerações

Os arquivos JSON de entrada já estão comitados no projeto, porém, se desejar, pode gerá-los novamente tanto dentro do container quanto fora dele. siga os seguintes passos:

1. Liste a pasta /data/input do projeto e, caso haja arquivos, delete-os.
2. Navegue até o folder /data/src
3. Execute o comando `python events_data_provider.py` para gerar os arquivos novamente.
