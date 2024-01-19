<div align=center>

**Spark contador de palavras**

**1 - Realizar o pull da imagem jupyter/all-spark-notebook**

![pull da imagem](<pull da imagem jupyter spark.png>)

#

**2 - Criar um container a partir da imagem**

*docker run -it -p 8888:8888 jupyter/all-spark-notebook*
![iniciando container](<iniciando o container jupyter spark.png>)

![comando wget](<Baixando o readme spark.png>)

#

**Usando o Spark Shell, apresente a sequência de comandos Spark necessários para contar a quantidade de ocorrências de cada palavra contida no arquivo README.md de seu repositório git.**

![comandos spark](<fim com resultado spark.png>)


</div>

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Contador de palavras").getOrCreate()
caminho = "/home/jovyan/work/README.MD"
texto = spark.sparkContext.textFile(caminho)
contador = texto.flatMap(lambda line: line.lower().split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
for word, count in contador.collect(): print(f"{word}: {count}")
