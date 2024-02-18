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