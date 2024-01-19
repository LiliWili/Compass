<div align=center>

## Laboratório Glue

</div>

**- Configurando sua conta para utilizar o AWS Glue.**

![configurando o glue](<primeiros passos glue.png>)

#

**- Criando a IAM Role para os jobs do AWS Glue**
![configurando o glue](<etapa da função iam glue.png>)

#

**- Configurando as permissões no AWS Lake Formation**

![configurando o glue](<aws lake formation glue.png>)
![configurando o glue](<concedendo permissoes select describe no lake formation  glue.png>)

#

**- Criando novo job no AWS Glue**

![configurando o glue](<criando um job glue.png>)
![configurando o glue](<input e target glue.png>)

#

**- Executando o script job**

*Ler o arquivo nomes.csv no S3 (lembre-se de realizar upload do arquivo antes)*

![configurando o glue](<rodando codigo de exemplo glue.png>)

#

*Imprima o schema do dataframe gerado no passo anterior.*

![configurando o glue](<imprimindo o schema glue.png>)

#

*Escrever o código necessário para alterar a caixa dos valores da coluna nome para MAIÚSCULO.*

![configurando o glue](<nome maiusculo codigo glue.png>)
![configurando o glue](<nome maiusculo resultado glue.png>)

#

*Imprimir a contagem de linhas presentes no dataframe.*

![configurando o glue](<contagem de linhas codigo glue.png>)
![configurando o glue](<contagem de linhas resultado glue.png>)

#

*Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo. Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe.*

![configurando o glue](<contagem de nome agrupado por nome e sexo codigo glue.png>)
![configurando o glue](<contagem de nome agrupado por nome e sexo resultado glue.png>)

#

*Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu.*
acredito que esse e o masculino estão errados

![configurando o glue](<nome feminino mais comum codigo glue.png>)
![configurando o glue](<nome feminino mais comum resultado glue.png>)

#

*Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu.*

![configurando o glue](<nome masculino mais comum codigo glue.png>)
![configurando o glue](<nome masculino mais comum resultado glue.png>)

#

*Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe. Considere apenas as primeiras 10 linhas, ordenadas pelo ano, de forma crescente.*

![configurando o glue](<total de registro masculino e feminino por ano codigo glue .png>)
![configurando o glue](<total de registro masculino e feminino por ano resultado glue .png>)

#

*Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3.*
*Atenção aos requisitos: A gravação deve ocorrer no subdiretório frequencia_registro_nomes_eua do path s3://<BUCKET>/lab-glue/. O formato deve ser JSON. O particionamento deverá ser realizado pelas colunas sexo e ano (nesta ordem)*

![configurando o glue](<Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3. codigo glue.png>)
![configurando o glue](<tEscrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3. glue.png>)

#

**- Criando novo crawler**

![configurando o glue](<criacao e crawler aparecendo no databse gluelab.png>)
![configurando o glue](<concedendo permissoes select describe no lake formation  glue.png>)