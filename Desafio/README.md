<div align=center>

## Desafio

</div>


**Etapa-1**
**Tive algumas dificuldades para fazer o upload dos arquivos csv para o bucket mas fui atrás de ajuda dos colegas da squad e consegui resolver, o problema era em algumas pequenas partes do código e uma condição que tinha declarado incorretamente. Após fazer essas correções os arquivos foram enviados corretamente para o bucket**

[Etapa-I](Etapa-1)

#

**Etapa-2**
**Nesta etapa do desafio, tive dificuldades na criação de camadas, eu fazia o processo todo de instalção e upload no lambda mas não conseguia chamar a camada no código então tive que utilizar apenas uma camada que criei, que foi a do boto, as outras camadas eu tive que utilizar a que o proprio lambda oferece, que é a do pandas e urllib, depois de resolver esses problemas fui testar o código. Criei várias versões do código e mesmo assim não consegui cumprir o requisito de ter 100 registros por arquivos mas acredito que isso não ira me atrapalhar muito, apenas não cumpri um dos requisitos mas os dados que preciso estão nos arquivos e vou tentar trabalhar com eles na proxima etapa do desafio.**

[Etapa II](Desafio/Etapa-2)


#

**Etapa-3**
**A etapa número três foi a etapa em que tive algumas dificuldades, mas não foi a mais difícil de ser feita. Errei várias vezes ao fazer o código da camada trusted. Estava enfrentando a mesma dificuldade que várias pessoas tiveram na leitura dos arquivos JSON, mas conversei com o pessoal da minha squad e eles me ajudaram a resolver. Na segunda parte do desafio, tentei fazer o modelo dimensional da maneira que achava ser correta. Não peguei muito o jeito da modelagem dimensional, mas tentei fazer o modelo da API e do antigo arquivo CSV separadamente, pois os dados que coletei da API obviamente não são iguais aos do CSV. Na camada refined, mudei alguns nomes de colunas, retirei alguns dados que não queria e adicionei novas colunas com IDs, deixando igual à modelagem dimensional que eu tinha feito na segunda parte. Particionei os dados em pastas no bucket e finalizei. Eu não sabia muito bem o que fazer na camada refined e tentei perguntar aos colegas da squad. Eles me explicaram, mas não estava vendo tantos erros dentro dos arquivos, então as mudanças não foram muito grandes.**

[Etapa-III](Etapa-3)

#

**Nesta etapa do desafio, utilizei apenas os dados coletados da API por causa da diferença da quantidade de dados, os dados do csv que pegamos na primeira etapa do desafio fornecia poucos dados então preferi usar apenas os da api, ja que eu não tinha conseguido separar os json com apenas 100 dados cada, ficou uma quantidade bem significativa. O Quicksight não foi uma plataforma muito dificil de usar, o curso ajudou bastante na comprensão do que fazer e como deveria ser feito, realmente a unica dificuldade que tive foi em escolher cores que combinavam com os dados dos gráficos e não ficasse só nas mesmas cores. Não fiz nenhum código sql já que utilizei apenas os dados da api então só coloquei os dados lá e fiz a construção do dashboard normalmente. O vídeo foi uma parte bem chatinha de fazer por ser muito curto o tempo, tive que refazer algumas partes várias vezes. Algumas partes do vídeo esta com o audio sobreposto mas não consegui arrumar, no editor os audios são reproduzidos normalmente.**

**Link do video:** [Video da ultima parte do desafio](https://youtu.be/Lgq8mjM4B88)


[Etapa-IV](Etapa-4)