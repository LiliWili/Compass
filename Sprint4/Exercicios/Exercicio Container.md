**1. Construa uma imagem a partir de um arquivo de instruções (Dockerfile) que execute o código carguru.py. Após, execute um container a partir da imagem criada. Registre aqui o conteúdo de seu arquivo Dockerfile e o comando utilizado para execução do container.**

#

FROM python:3<br>
WORKDIR /app<br>
COPY carguru.py .<br>
CMD ["python", "./app/carguru.py"]<br>
<br>

docker build -t carguru:atividade .<br>
docker run -d carguru:atividade

![Imagem do Dockerfile](<Atividade carguru.png>)

#

**2. É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.**

é possível usar o comando - docker start <container>

#


**3. Agora vamos exercitar a criação de um container que permita receber inputs durante sua execução. Seguem as instruções.**

**-- Criar novo script Python que implementa o algoritmo a seguir:**<br>

**1 - Receber uma string via input**<br>
**2 - Gerar o hash  da string por meio do algoritmo SHA-1**<br>
**3 - Imprimir o hash em tela, utilizando o método hexdigest**<br>
**4 - Retornar ao passo 1**<br>

**-- Criar uma imagem Docker chamada mascarar-dados que execute o script Python criado anteriormente**<br>
**--  Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento**<br>
**-- Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização do container neste espaço.**<br>

#

**DOCKERFILE**

FROM python:3<br>
WORKDIR /app<br>
COPY . /app<br>
CMD ["python", "mascarar-dados.py"]<br>

**SCRIPT PYTHON**

import hashlib

while True:

    mascarar = input("Digite uma palavra para mascarar: ")

    objeto_hash = hashlib.sha1(mascarar.encode())

    hash_hex = objeto_hash.hexdigest()

    print(f"Hash da palavra:",{hash_hex})

**COMANDOS**

docker build -t mascarar-dados .<br>
docker run -it mascarar-dados<br>

![Imagem da Atividade mascarar-dados](<Atividade mascarar-dados.png>)

#
